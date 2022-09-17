import argparse
import functools
import os
import sys
from enum import Enum
from typing import List, Union


def debug(*args, **kwargs):
    if os.getenv("DEBUG"):
        print(*args, **kwargs, file=sys.stderr)


class CommandParser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        kwargs["formatter_class"] = lambda prog: argparse.HelpFormatter(
            prog,
            max_help_position=100,
            width=None,
        )

        super().__init__(*args, **kwargs)

    def add_argument(self, *args, **kwargs):
        _type = kwargs.get("type")
        if _type is None:
            return super().add_argument(*args, **kwargs)

        dest = kwargs.get("dest", "?")

        # Handle unions:
        if getattr(_type, "__origin__", None) is Union:
            # delayed import to avoid circular reference
            from .client.types import Unset

            inner_types = list(_type.__args__)
            if Unset in inner_types:
                inner_types.remove(Unset)
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

        if getattr(_type, "__origin__", None) is list:
            inner_type = _type.__args__[0]

            if inner_type not in (int, str):
                debug(
                    f"WARN: ignoring {self.prog} {dest} type={_type}"
                )
                return

            _type = inner_type
            # FIXME: Determine if 1 or 0 is required ?
            kwargs["nargs"] = "*"

        # Check we have handled all generic types:
        if getattr(_type, "__origin__", None):
            debug(f"WARN: ignoring {self.prog} {dest} type={_type}")
            return

        kwargs["type"] = _type

        # special handling for enums (potentially within the Union handled above):
        if issubclass(_type, Enum):
            enum_options = list(_type)
            # If there is exactly one valid enum value (e.g. from a discriminated union),
            # set it as default and skip adding the argument
            if len(enum_options) == 1:
                # FIXME: be better to just add to result of parse_args via orderride ?
                self.set_defaults(**{kwargs["dest"]: enum_options[0]})
                return
            kwargs["choices"] = enum_options
            # print('Need to add enum!', enum_options)

        super().add_argument(*args, **kwargs)


prog_parser = CommandParser(
    prog="bl", description="bl is a command-line interface for the BinaryLane API"
)

command_action: "argparse._SubParsersAction" = prog_parser.add_subparsers(
    title="Available Commands", metavar=""
)


def _add_command(
        action: "argparse._SubParsersAction", prefix: str, name: str, help: str = None
):
    def wrap(func):
        command_name = (
            name[len(prefix) + 1:] if name.startswith(prefix + "_") else name
        )

        command_parser = action.add_parser(command_name, help=help)
        handler = func(command_parser)
        command_parser.set_defaults(func=handler)
        return func

    return wrap


def _add_group(
        action: "argparse._SubParsersAction", prefix: str, name: str, help: str = None
):
    def wrap(func):
        command_name = (
            name[len(prefix) + 1:] if name.startswith(prefix + "_") else name
        )

        group_parser = action.add_parser(command_name, help=help)
        group_action = group_parser.add_subparsers(title=f"{name.title()} commands", metavar="")
        func.add_group = functools.partial(_add_group, group_action, command_name)
        func.add_command = functools.partial(_add_command, group_action, command_name)
        return func

    return wrap


add_group = functools.partial(_add_group, command_action, "")


def run(args):
    parsed = prog_parser.parse_args(args)

    # Haven't reached a command
    if not "func" in parsed:
        prog_parser.parse_args(args + ["--help"])
        return

    # Run the command's handler
    handler = parsed.func
    del parsed.func

    from .client import AuthenticatedClient

    client = AuthenticatedClient(
        "https://api.binarylane.com.au",
        open(os.path.expanduser("~/.config/python-blcli")).read().strip(),
    )

    parsed.client = client
    response = handler(**vars(parsed))
    if not response:
        prog_parser.parse_args(args + ["--help"])
        return

    # display response
    display(response)
    return


def display(response):
    response_type = type(response)
    # print(f"-- {response_type} ({response_type.__module__}) --")
    primary = None
    primary_type = None

    for name, _type in response_type.__annotations__.items():
        if name == "additional_properties":
            continue
        # get inner type if it is generic
        if getattr(_type, "__origin__", None):
            _type = _type.__args__[0]

        if response_type.__module__.startswith(_type.__module__) or _type is str:
            primary = name
            primary_type = _type

    if not primary:
        print(
            f"ERROR: unsure how to print {response_type} ({response})", file=sys.stderr
        )

    from terminaltables import SingleTable

    response = getattr(response, primary)
    if isinstance(response, list):
        header = [
            key
            for key in getattr(
                primary_type, "__annotations__", {"item": "value"}
            ).keys()
            if key != "additional_properties"
        ]
        data = [header] + [
            flatten(item if item is str else item.to_dict().values())
            for item in response
        ]
    elif isinstance(response, str):
        data = []
        print(response)
    else:
        data = [["Name", "Value"]] + [
            flatten(item, True) for item in response.to_dict().items()
        ]
    if len(data) > 1:
        print(SingleTable(data).table)


def flatten(values, single_object: bool = False):
    result: List[str] = []
    max_list = 5
    max_str = 80
    trunc = "..."

    for item in values:
        item_type = type(item)
        if item_type is list:
            if len(item) > max_list:
                item = item[:max_list] + [trunc]
            if not single_object:
                item = ", ".join(map(str, item))
            else:
                item = "- " + "\n- ".join(
                    [("  ".join(f'{key}: {value}\n' for key, value in i.items()) if type(i) is dict else str(i)) for i
                     in item]
                ) if item else ''
        if item_type is dict:
            for key in ('display_name', 'name', 'slug', 'id'):
                if key in item:
                    item = item[key]
                    break
            else:
                item = "<object>" if not single_object else "\n".join(
                    [f'{key}: {value}' for key, value in item.items()])
        if item_type is bool:
            item = "Yes" if item else "No"

        item = str(item)
        if len(item) > max_str + len(trunc):
            item = item[:max_str] + trunc
        result.append(item)

    return result


try:
    from argparse import BooleanOptionalAction
except:
    # New to 3.9
    class BooleanOptionalAction(argparse.Action):
        def __init__(
                self,
                option_strings,
                dest,
                default=None,
                type=None,
                choices=None,
                required=False,
                help=None,
                metavar=None,
        ):

            _option_strings = []
            for option_string in option_strings:
                _option_strings.append(option_string)

                if option_string.startswith("--"):
                    option_string = "--no-" + option_string[2:]
                    _option_strings.append(option_string)

            if (
                    help is not None
                    and default is not None
                    and default is not argparse.SUPPRESS
            ):
                help += " (default: %(default)s)"

            super().__init__(
                option_strings=_option_strings,
                dest=dest,
                nargs=0,
                default=default,
                type=type,
                choices=choices,
                required=required,
                help=help,
                metavar=metavar,
            )

        def __call__(self, parser, namespace, values, option_string=None):
            if option_string in self.option_strings:
                setattr(namespace, self.dest, not option_string.startswith("--no-"))

        def format_usage(self):
            return " | ".join(self.option_strings)
