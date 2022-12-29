# pylint: disable=missing-module-docstring

import importlib
from abc import abstractmethod
from argparse import ArgumentParser
from typing import List, Optional

from ..cli import debug
from .runner import Runner


class PackageRunner(Runner):
    """PackageRunner imports a list of runners from specified package."""

    def __init__(self, parent: Optional[Runner] = None) -> None:
        super().__init__(parent)
        self.parser = ArgumentParser(prog=f"{self.prog}", description=self.format_description())
        self.parser.format_usage()
        self.configure()

    @property
    @abstractmethod
    def package_path(self) -> str:
        """Path of python package containing runners to import during run()"""

    def configure(self) -> None:
        """Configure argument parser"""

        cmd_parser = self.parser.add_subparsers(metavar="<command>", title="required arguments")
        for cls in importlib.import_module(f".{self.package_path}", package=__package__).commands:
            runner = cls(self)
            cmd_parser.add_parser(runner.name, help=runner.format_description()).set_defaults(runner=runner)
        # This is a workaround for python3.8 ArgumentParser unnecessarily crushing the first column width
        cmd_parser.add_parser(" " * 24, help="")

        self.commands = cmd_parser

    def run(self, args: List[str]) -> None:
        debug(f"PackageRunner for {self.name} ({self.package_path}). Received arguments: {args}")

        # We need to hide the --help parameter from argparse, so that we can pass it to a subrunner
        # rather than displaying our own help.
        extra = []
        if self.HELP in args:
            args.remove(self.HELP)
            extra += [self.HELP]

        # See if a runner was selected
        parsed, left = self.parser.parse_known_args(args)
        if "runner" in parsed:
            return parsed.runner.run(left + extra)

        # If not, display help
        return self.parser.print_help()
