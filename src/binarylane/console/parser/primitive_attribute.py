from __future__ import annotations

import argparse
import logging
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, Union
from binarylane.pycompat import typing

from binarylane.types import UNSET, Unset

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.parser.attribute import Attribute

NoneType = type(None)

if TYPE_CHECKING:
    from binarylane.console.parser.object_attribute import ObjectAttribute
    from binarylane.console.parser.parser import Parser

logger = logging.getLogger(__name__)

PRIMITIVE_TYPES = {int, str, bool, float, datetime, Enum}


def is_primitive_type(type_: type) -> bool:
    return any(issubclass(type_, t) for t in PRIMITIVE_TYPES)


class PrimitiveAttribute(Attribute):
    """Represents a strongly typed, command parameter"""

    _alternate_types: List[type]
    _dest: str
    _action: Optional[Type[argparse.Action]]
    _default_value: object = UNSET

    def __init__(
        self,
        attribute_name: str,
        attribute_type_hint: object,
        *,
        option_name: Optional[str],
        dest: Optional[str] = None,
        required: bool,
        description: Optional[str] = None,
        action: Optional[Type[argparse.Action]] = None,
        metavar: Optional[str] = None,
        parent: Optional[ObjectAttribute] = None,
    ) -> None:
        # Partial construction needed to perform unboxing:
        self._array = False
        self._alternate_types = []
        self.required = required
        attribute_type = self._unbox_type(attribute_type_hint)

        # Can now init attribute
        super().__init__(
            attribute_name,
            attribute_type,
            required=required,
            option_name=option_name,
            description=description,
        )

        self._dest = dest or option_name or attribute_name
        self._action = action
        self._metavar = metavar or (option_name or attribute_name).upper()
        self.parent = parent

    @property
    def usage(self) -> Optional[str]:
        if self.has_default_value:
            return None

        if not self.option_name:
            return self._metavar
        usage = f"--{self.option_name} {self._metavar}"
        return usage

    @property
    def has_default_value(self) -> bool:
        return self._default_value is not UNSET

    def configure(self, parser: Parser) -> None:
        """Call Parser.add_argument on parser with appropriate configuration"""

        # argparse keyword arguments are built up in `kwargs` during method execution
        kwargs = self._create_kwargs()

        # special handling for enums (potentially within the Union handled above):
        if issubclass(self.attribute_type, Enum):
            enum_options: List[str] = list(self.attribute_type)
            # If there is exactly one valid enum value (e.g. from a discriminated union),
            # set it as default and skip adding the argument
            if len(enum_options) == 1:
                self._default_value = enum_options[0]
                return
            kwargs["choices"] = enum_options
            kwargs["help"] += " (One of: %(choices)s)"
            if not kwargs.get("metavar"):
                self._unsupported("missing metavar")
                kwargs["metavar"] = self._dest.upper()

        # enum is allowed multiple description lines to show markdown, everything else gets a single line.
        elif self.description:
            kwargs["help"] = self.description.strip(" \t\r\n").split("\n")[0]

        # If this is a positional argument, give it an uppercase metavar
        if self.option_name and not kwargs.get("metavar"):
            self._unsupported("missing metavar")
            kwargs["metavar"] = self.option_name.upper()

        # This argument is going to be displayed, warn if a description is not available
        if self.description is None:
            self._unsupported("missing help", False)

        parser.add_to_group(self.group_name or bool(self.required), self.name_or_flag, self.attribute_type, **kwargs)

    def construct(self, _parser: Parser, parsed: argparse.Namespace) -> object:
        value: object = getattr(parsed, self._dest, self._default_value)
        if value in (None, UNSET):
            if not self.required:
                return UNSET
            raise ValueError(f"{self.option_name} is a required value")

        if self.attribute_type is None:
            self._unsupported(f"{self.option_name} does not have a type")
            return value

        if isinstance(value, list):
            result = []
            for item in value:
                if isinstance(item, list):
                    result += [self._construct(nested) for nested in item]
                else:
                    result.append(self._construct(item))
            return result

        return self._construct(value)

    def _construct(self, value: object) -> object:
        if self.attribute_type is None:
            logger.warning("%s does not have a primitive type, assuming str", self.option_name)
            return value

        # Ensure value is of correct type
        if not isinstance(value, self.attribute_type):
            raise TypeError(f"{self.option_name} has {type(value)} instead of {self.attribute_type}")

        # If we have alternative types, see if any are valid:
        for type_ in self._alternate_types:
            try:
                return type_(value)
            except ValueError:
                pass

        # Otherwise return it as-is
        return value

    def _unbox_type(self, type_hint: object) -> type:
        # type_int could be a type like 'str' or 'bool', or a GenericAlias like `List[Union[int,str]]`.
        # We need to determine the correct primitive type(s) to use and corresponding argparse settings.

        type_: object = type_hint
        origin: Optional[object] = type_  # any 'not None' value is needed, to start the loop
        while origin is not None:
            origin = typing.get_origin(type_)

            if origin is Union:
                type_ = self._unbox_union(type_)
            elif origin is list:
                type_ = self._unbox_list(type_)
            elif origin:
                raise NotImplementedError(f"unsupported generic type. type={type_} origin={origin}")

        # Should now have an actual type, rather than a GenericAlias
        if not isinstance(type_, type):
            raise NotImplementedError(f"unsupported type hint. type={type_} hint={type_hint}")

        # Check we haven't ended up with a class or similar
        if not is_primitive_type(type_):
            raise NotImplementedError(f"unsupported non-primitive type. type={type_}")

        return type_

    def _unbox_list(self, type_hint: object) -> object:
        inner_type = typing.get_args(type_hint)[0]

        # This should not be possible, but null check required for type safety
        if inner_type is None:
            raise NotImplementedError(f"unsupported list type. type={type_hint} inner_type={inner_type}")

        self._array = True
        return inner_type

    def _unbox_union(self, type_hint: object) -> type:
        # Generally for optional parameters the API has Union[None,Unset,T]
        # We strip Unset and None so that we can provide argument for T
        inner_types = list(typing.get_args(type_hint))
        none = NoneType in inner_types
        unset = Unset in inner_types

        # Currently all non-required attributes in BinaryLane API include both None and Unset in the type hint,
        # the following will warn if that ever changes:
        if none:
            inner_types.remove(NoneType)
            if not unset:
                self._unsupported(f"Union includes None, but not Unset. type={type_hint}", False)
            if self.required:
                self._unsupported(f"Attribute is required but Union includes None. type={type_hint}")
        if unset:
            inner_types.remove(Unset)
            if not none:
                self._unsupported(f"Union includes Unset, but not None. type={type_hint}", False)

        # BinaryLane API has some Union[int,str] where there is no overlap - i.e. if int(1) is valid input, then
        # str("1") is not valid. As such, we can request parse a string, and try converting to other primitive types
        # in the union during construction.
        if len(inner_types) > 1 and str in inner_types and all(is_primitive_type(t) for t in inner_types):
            inner_types.remove(str)
            self._alternate_types = list(inner_types)
            inner_types = [str]

        if len(inner_types) != 1:
            raise NotImplementedError(f"Union of {typing.get_args(type_hint)}")

        return inner_types[0]

    def _create_kwargs(self) -> Dict[str, Any]:
        """Arguments that are passed unmodified to argparse"""
        kwargs: Dict[str, Any] = {}

        if self._dest != self.option_name and self.option_name:
            kwargs["dest"] = self._dest
        if self.description is not None:
            kwargs["help"] = self.description
        if self._action is not None:
            kwargs["action"] = self._action
        if self._metavar is not None:
            kwargs["metavar"] = self._metavar
        if self.required is not None:
            kwargs["required"] = self.required

        # For array input, support both "--ssh-keys 1 2 3" and "--ssh-keys 1 --ssh-keys 2"
        # Since nargs is zero or more, Empty array can be created via just "--ssh-keys"
        if self._array:
            kwargs["nargs"] = argparse.ZERO_OR_MORE
            kwargs["action"] = "append"

        # Use --name , --no-name for booleans rather than --name [true|false]
        if self.attribute_type is bool:
            kwargs["action"] = BooleanOptionalAction

        return kwargs
