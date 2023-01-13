from __future__ import annotations

import argparse
import datetime
import logging
import typing
from enum import Enum
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, Union

if TYPE_CHECKING:
    from binarylane.console.parsers.parser import CommandParser

logger = logging.getLogger(__name__)

# pylint: disable=too-few-public-methods
class CommandArgument:
    """Represents a strongly typed, command parameter"""

    _name: str
    _type: object
    _dest: str
    _required: Optional[bool]
    _description: Optional[str]
    _action: Optional[Type[argparse.Action]]
    prog: Optional[str]

    raise_on_unsupported = False

    def __init__(
        self,
        name: str,
        _type: object,
        *,
        dest: Optional[str] = None,
        required: Optional[bool] = None,
        description: Optional[str] = None,
        action: Optional[Type[argparse.Action]] = None,
    ) -> None:
        self._name = name
        self._type = _type
        self._dest = dest or name
        self._required = required
        self._description = description
        self._action = action

    def add_to_parser(self, parser: "CommandParser") -> None:
        """Call ArgumentParser.add_argument on parser with appropriate configuration"""
        self.prog = parser.prog

        # argparse keyword arguments are built up in `kwargs` during method execution
        kwargs = self._create_kwargs()

        # type is required for rest of the method
        if self._type is None:
            self._unsupported("missing type.")
            parser.add_argument(self._name, **kwargs)
            return

        # type could be a primitive like 'str' or 'bool', or something complex like `List[Union[int,str]]`.
        # These do not share a common ancestor at runtime
        #
        # We need to determine the correct primitive type(s) to use and corresponding argparse settings
        _type: Any = self._type

        origin: Optional[type] = type
        while origin is not None:
            origin = typing.get_origin(_type)

            if origin is Union:
                _type = self._unbox_union(_type, kwargs)
            elif origin is list:
                inner_type = typing.get_args(_type)[0]

                if inner_type is None:
                    self._unsupported(f"unsupported list type. type={_type} inner_type={inner_type}")
                    return

                _type = inner_type
                # FIXME: Determine if 1 or 0 is required ?
                kwargs["nargs"] = "*"
            elif origin:
                self._unsupported(f"unsupported generic type. type={_type} origin={origin}")
                return

        # special handling for enums (potentially within the Union handled above):
        assert _type is not None
        if issubclass(_type, Enum):
            enum_options: List[str] = list(_type)
            # If there is exactly one valid enum value (e.g. from a discriminated union),
            # set it as default and skip adding the argument
            if len(enum_options) == 1:
                # FIXME: be better to just add to result of parse_args via orderride ?
                parser.set_defaults(**{self._dest: enum_options[0]})
                return
            kwargs["choices"] = enum_options
            kwargs["metavar"] = self._dest.upper()

        # Check we haven't ended up with Request object
        elif _type not in PRIMITIVE_TYPES:
            self._unsupported(f"unsupported type. type={_type}")
            return

        # If this is a positional argument, give it an uppercase metavar
        if self._name[0] not in parser.prefix_chars and not kwargs.get("metavar"):
            kwargs["metavar"] = self._name.upper()

        # Place argument in appropriate group:
        group = parser.arguments_group if self._required is not False else parser.modifiers_group
        group.add_argument(self._name, type=_type, **kwargs)

    def _unbox_union(self, _type: object, kwargs: Dict[str, Any]) -> type:
        # delayed import to avoid circular reference
        from binarylane.types import UNSET, Unset

        # Generally for optional parameters the API has Union[None,Unset,T]
        # We strip Unset and None so that we can provide argument for T
        inner_types = list(typing.get_args(_type))
        if type(None) in inner_types and self._required is False:
            inner_types.remove(type(None))
            kwargs["default"] = None
        if Unset in inner_types:
            inner_types.remove(Unset)
            kwargs["default"] = UNSET
        # FIXME: probably need to add separate arguments for int and str?
        #        Or determine it dynamically based on whether input str
        #        can cast to int ?
        if int in inner_types and str in inner_types:
            self._unsupported(f"union parsing not implemented, using `str`. type={_type}")
            inner_types.remove(int)
        if len(inner_types) != 1:
            raise NotImplementedError(f"Union of {typing.get_args(_type)}")
        return inner_types[0]

    def _unsupported(self, message: str) -> None:
        """Report that command parsing is not likely to work correctly"""
        if CommandArgument.raise_on_unsupported:
            raise NotImplementedError(message)
        logger.warning(f"{self.prog}:{self._dest} - {message}")

    def _create_kwargs(self) -> Dict[str, Any]:
        """Arguments that are passed unmodified to argparse"""
        kwargs: Dict[str, Any] = {}

        # This argument is going to be displayed, warn if a description is not available
        if self._description is None:
            self._unsupported("missing help.")

        if self._dest != self._name:
            kwargs["dest"] = self._dest
        if self._required is not None:
            kwargs["required"] = self._required
        if self._description is not None:
            kwargs["help"] = self._description
        if self._action is not None:
            kwargs["action"] = self._action
        return kwargs


PRIMITIVE_TYPES = {int, str, bool, float, datetime.datetime}
