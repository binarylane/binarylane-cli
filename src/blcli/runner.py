""" Runner represents the overall CLI: behaviour - parse input, perform an action, and display result """
from __future__ import annotations

import importlib
import re
from abc import ABC, abstractmethod
from argparse import ArgumentParser
from typing import Any, Dict, List, Optional

from .cli import CommandParser, debug, display, get_api_token


class Runner(ABC):
    """Abstract base class for all Runner implementations"""

    parent: Optional[Runner]

    def __init__(self, parent: Optional[Runner] = None) -> None:
        self.parent = parent

    @property
    def prog(self) -> str:
        """The 'program' name is used in help output to identify this runner"""
        return (self.parent.prog + " " if self.parent else "") + self.name

    @property
    @abstractmethod
    def name(self) -> str:
        """CLI name that is used to invoke the runner"""

    @property
    @abstractmethod
    def description(self) -> str:
        """Description of what this runner does"""

    def format_description(self) -> str:
        """Many API operation summaries are title-cased (like a headline), rather than as a sentence."""
        return re.sub(" ([A-Z])([a-z])", lambda m: " " + m.group(1).lower() + m.group(2), self.description)

    @abstractmethod
    def run(self, args: List[str]) -> None:
        """Subclasses implement their primary behaviour here"""

    def __call__(self, args: List[str]) -> None:
        self.run(args)


class PackageRunner(Runner):
    """PackageRunner imports a list of runners from specified package."""

    @property
    @abstractmethod
    def package_path(self) -> str:
        """Path of python package containing runners to import during run()"""

    def run(self, args: List[str]) -> None:
        debug(f"PackageRunner for {self.name} ({self.package_path}). Received arguments: {args}")
        root_parser = ArgumentParser(prog=f"{self.prog}", description=self.format_description())
        root_parser.format_usage()
        cmd_parser = root_parser.add_subparsers(metavar="<command>", title="required arguments")

        for cls in importlib.import_module(self.package_path, package=__package__).commands:
            runner = cls(self)
            cmd_parser.add_parser(runner.name, help=runner.format_description()).set_defaults(runner=runner)

        # This is a workaround for python3.8 ArgumentParser unnecessarily crushing the first column width
        cmd_parser.add_parser(" " * 24, help="")
        parsed, left = root_parser.parse_known_args(args)

        # See if a runner was selected
        if "runner" in parsed:
            return parsed.runner.run(left)

        return root_parser.print_help()


class ModuleRunner(Runner):
    """ModuleRunner imports a runner from specified module."""

    @property
    @abstractmethod
    def module_path(self) -> str:
        """Path of python module containing runner to import during run()"""

    def run(self, args: List[str]) -> None:
        debug(f"ModuleRunner for {self.name} ({self.module_path}). Received arguments: {args}")
        cls = importlib.import_module(self.module_path, package=__package__).Command
        command = cls()
        command.run(args)


class CommandRunner(Runner):
    """CommandRunner parses input, executes API operation and displays the result"""

    parser: CommandParser

    def __init__(self, parent: Optional[Runner] = None) -> None:
        super().__init__(parent)
        self.parser = CommandParser()
        self.configure(self.parser)

    @abstractmethod
    def configure(self, parser: CommandParser) -> None:
        """Add supported CLI arguments"""

    @abstractmethod
    def request(self, **kwargs: Dict[str, Any]) -> Any:
        """Perform API operation and return response"""

    def run(self, args: List[str]) -> None:
        debug(f"Command parser for {self.name}. args: {args}")
        parsed = self.parser.parse_args(args)
        debug(f"Parsing succeeded, have {parsed}")

        authenticated_client = importlib.import_module(".client", __package__).AuthenticatedClient
        client = authenticated_client(
            "https://api.binarylane.com.au",
            get_api_token(),
        )

        parsed.client = client

        response = self.request(**vars(parsed))
        display(response)


class AppRunner(PackageRunner):
    """
    AppRunner is the 'root' runner for the application. In normal usage, all command line arguments are passed
    directly to run(). Apart from global flags, the primary function of this class is to invoke the
    appropriate runner for the supplied arguments.
    """

    @property
    def name(self) -> str:
        return "bl"

    @property
    def description(self) -> str:
        return "bl is a command-line interface for the BinaryLane API"

    @property
    def package_path(self) -> str:
        return ".commands"
