""" CLI implementation """

import argparse
import functools
import importlib
import os
import sys
import typing
from enum import Enum
from typing import Any, Callable, Optional, Union

try:
    # FIXME: Is there a more pythonic way of dealing with this backort ?
    # pylint: disable=unused-import
    from argparse import BooleanOptionalAction  # type: ignore
except ImportError:
    from .actions import BooleanOptionalAction


def debug(*args: str) -> None:
    """Wrapper for print() that only produces output when DEBUG is enabled"""
    if os.getenv("DEBUG"):
        print(*args, file=sys.stderr)


def warn(*args: str) -> None:
    """Wrapper for print() that prefixes output with WARN:"""
    print("WARN: ", *args, file=sys.stderr)


class CommandParser(argparse.ArgumentParser):
    """Enhanced ArgumentParser with support for generic types"""

    def __init__(self, **kwargs: Any):
        kwargs["formatter_class"] = lambda prog: argparse.HelpFormatter(
            prog,
            max_help_position=100,
            width=None,
        )
        kwargs["add_help"] = False

        super().__init__(**kwargs)

    def cli_argument(self, *args: str, **kwargs: Any) -> Optional[argparse.Action]:
        """Add CLI argument to parser"""
        if "description" in kwargs:
            kwargs["help"] = kwargs["description"]
            del kwargs["description"]

        _type = kwargs.get("type")
        if _type is None:
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
                warn(f"unsupported type {self.prog} {dest} type={_type} inner_type={inner_type}")
                return None

            _type = inner_type
            # FIXME: Determine if 1 or 0 is required ?
            kwargs["nargs"] = "*"

        # Check we have handled all generic types:
        if typing.get_origin(_type):
            warn(f"unsupported {self.prog} {dest} type={_type}")
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
            # print('Need to add enum!', enum_options)

        debug(f"Adding: {kwargs}")
        return self.add_argument(*args, **kwargs)


prog_parser = CommandParser(prog="bl", description="bl is a command-line interface for the BinaryLane API")

AddCommandParser = Callable[..., CommandParser]
add_command_parser: AddCommandParser = prog_parser.add_subparsers(title="Available Commands", metavar="").add_parser

AddCommand = Callable[[CommandParser], None]


def _add_command(
    add_parser: AddCommandParser, prefix: str, name: str, description: str = None
) -> Callable[[AddCommand], AddCommand]:
    def wrap(func: AddCommand) -> AddCommand:
        command_name = name[len(prefix) + 1 :] if name.startswith(prefix + "_") else name

        command_parser = add_parser(command_name, help=description)
        handler = func(command_parser)
        command_parser.set_defaults(func=handler)
        return func

    return wrap


AddGroup = Callable[[str, str], None]


def _add_group(
    add_parser: AddCommandParser, prefix: str, name: str, description: str = None
) -> Callable[[AddGroup], AddGroup]:
    def wrap(func: AddGroup) -> AddGroup:
        command_name = name[len(prefix) + 1 :] if name.startswith(prefix + "_") else name

        group_parser = add_parser(command_name, help=description)
        group_action = group_parser.add_subparsers(title=f"{name.title()} commands", metavar="").add_parser
        func.add_group = functools.partial(_add_group, group_action, command_name)  # type: ignore
        func.add_command = functools.partial(_add_command, group_action, command_name)  # type: ignore
        return func

    return wrap


add_group = functools.partial(_add_group, add_command_parser, "")


def get_api_token() -> str:
    """Obtain user's API token from environment variable or configuration file"""
    token = os.getenv("BL_CLI_TOKEN")
    if token:
        return token

    with open(os.path.expanduser("~/.config/python-blcli"), encoding="utf-8") as config_file:
        return config_file.read().strip()
