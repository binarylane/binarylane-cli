""" CLI implementation """

import argparse
import importlib
import os
import sys
import typing
from enum import Enum
from typing import Any, Iterable, Optional, Union

try:
    # FIXME: Is there a more pythonic way of dealing with this backort ?
    # pylint: disable=unused-import
    from argparse import BooleanOptionalAction  # type: ignore
except ImportError:
    from .actions import BooleanOptionalAction


PRIMITIVE_TYPES = {int, str, bool, float}


def debug(*args: str) -> None:
    """Wrapper for print() that only produces output when DEBUG is enabled"""
    if os.getenv("DEBUG"):
        print(*args, file=sys.stderr)


def warn(*args: str) -> None:
    """Wrapper for print() that prefixes output with WARN:"""
    print("WARN: ", *args, file=sys.stderr)


def error(*args: str) -> None:
    """Wrapper for print() that prefixes output with ERROR:"""
    print("ERROR: ", *args, file=sys.stderr)


class CommandHelpFormatter(argparse.HelpFormatter):
    """Modified HelpFormatter that hides common options in displayed usage"""

    def add_usage(
        self,
        usage: Optional[str],
        actions: Iterable[argparse.Action],
        groups: Iterable[argparse._ArgumentGroup],
        prefix: Optional[str] = None,
    ) -> None:
        actions = [argparse.Action(["OPTIONS"], "")] + [
            action for action in actions if not action.dest.startswith("runner_")
        ]
        super().add_usage(usage, actions, groups, prefix)


class CommandParser(argparse.ArgumentParser):
    """Enhanced ArgumentParser with support for generic types"""

    def __init__(self, **kwargs: Any):
        kwargs["formatter_class"] = CommandHelpFormatter
        kwargs["add_help"] = False
        kwargs["allow_abbrev"] = False
        super().__init__(**kwargs)

        self._command_require = self.add_argument_group(title="Arguments")
        self._command_options = self.add_argument_group(title="Modifiers")
        self._optionals.title = "Options"

    # FIXME: refactor + remove usage of 'kwargs' as we know what our supported arguments are
    # pylint: disable=too-many-branches
    def cli_argument(self, *args: str, **kwargs: Any) -> Optional[argparse.Action]:
        """Add CLI argument to parser"""

        dest = kwargs.get("dest", "?")

        if "description" in kwargs:
            kwargs["help"] = kwargs["description"]
            del kwargs["description"]

        if kwargs.get("help") in {None, str(None)}:
            warn(f"{self.prog} - missing help for {dest}")

        _type = kwargs.get("type")
        if _type is None:
            warn(f"{self.prog} - missing type for {dest}")
            return self.add_argument(*args, **kwargs)

        dest = kwargs.get("dest", "?")

        # Handle unions:
        if typing.get_origin(_type) is Union:
            # delayed import to avoid circular reference
            unset = importlib.import_module(".client.types", __package__).Unset

            # Generally for optional parameters the API has Union[None,Unset,T]
            # We strip Unset and None so that we can provide argument for T
            inner_types = list(typing.get_args(_type))
            if unset in inner_types:
                inner_types.remove(unset)
            if type(None) in inner_types and not kwargs.get("required", True):
                inner_types.remove(type(None))

            # FIXME: probably need to add separate arguments for int and str?
            #        Or determine it dynamically based on whether input str
            #        can cast to int ?
            if int in inner_types and str in inner_types:
                inner_types.remove(int)

            if len(inner_types) != 1:
                raise NotImplementedError(f"Union of {_type.__args__}")
            _type = inner_types[0]

        # Note this intentionally includes Union[List[T], ...] after unwrapping the Union above
        if typing.get_origin(_type) is list:
            inner_type = typing.get_args(_type)[0]

            if inner_type not in (int, str):
                warn(f"{self.prog} - unsupported list type for {dest}: type={_type} inner_type={inner_type}")
                return None

            _type = inner_type
            # FIXME: Determine if 1 or 0 is required ?
            kwargs["nargs"] = "*"

        # Check we have handled all generic types:
        if typing.get_origin(_type):
            warn(f"{self.prog} - unsupported generic type {dest}: type={_type}")
            return None

        kwargs["type"] = _type

        # special handling for enums (potentially within the Union handled above):
        if issubclass(_type, Enum):
            enum_options = list(_type)
            # If there is exactly one valid enum value (e.g. from a discriminated union),
            # set it as default and skip adding the argument
            if len(enum_options) == 1:
                # FIXME: be better to just add to result of parse_args via orderride ?
                self.set_defaults(**{kwargs["dest"]: enum_options[0]})
                return None
            kwargs["choices"] = enum_options
            kwargs["metavar"] = kwargs["dest"].upper()

        # Check we haven't ended up with Request object
        elif kwargs["type"] not in PRIMITIVE_TYPES:
            warn(f"{self.prog} - unsupported type for {dest}: type={_type}")
            return None

        # If this is a positional argument, give it an uppercase metavar
        if args[0][0] not in self.prefix_chars and not kwargs.get("metavar"):
            kwargs["metavar"] = args[0].upper()

        # Place argument in appropriate group:
        group = self._command_require if kwargs.get("required", True) else self._command_options
        return group.add_argument(*args, **kwargs)


def get_api_token() -> str:
    """Obtain user's API token from environment variable or configuration file"""
    token = os.getenv("BL_CLI_TOKEN")
    if token:
        return token

    with open(os.path.expanduser("~/.config/python-blcli"), encoding="utf-8") as config_file:
        return config_file.read().strip()
