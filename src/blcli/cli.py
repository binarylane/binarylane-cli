import argparse
import functools
import os

prog_parser = argparse.ArgumentParser(
    prog="bl", description="bl is a command-line interface for the BinaryLane API"
)

subparsers = prog_parser.add_subparsers(title="Available Commands", metavar="")

# parser.add_argument("--version", help="Display version", action="store_true")


def _add_command(parser, name, help=None):
    def wrap(func):
        command = parser.add_parser(name, help=help)
        command.set_defaults(func=func)
        command_parser = command.add_subparsers(title=func.__name__, metavar="")
        func.add_command = functools.partial(_add_command, command_parser)
        return func

    return wrap


add_command = functools.partial(_add_command, subparsers)


def run(args):
    from .client import AuthenticatedClient

    client = AuthenticatedClient(
        "https://api.binarylane.com.au",
        open(os.path.expanduser("~/.config/python-blcli")).read().strip(),
    )

    parsed = prog_parser.parse_args(args)
    if "func" in parsed and parsed.func(client):
        return

    prog_parser.parse_args(args + ["--help"])
