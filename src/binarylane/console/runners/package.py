from __future__ import annotations

import importlib
import logging
from abc import abstractmethod
from argparse import ArgumentParser, HelpFormatter
from typing import List, NoReturn, Optional, Sequence
from binarylane.pycompat.functools import cached_property

from binarylane.console.runners import Runner
from binarylane.console.runners.module import ModuleRunner

logger = logging.getLogger(__name__)

# The 24 character width of the metavar ensures a fixed left-column size
COMMAND_METAVAR = "!" * 24

SEPARATOR = " "


class PackageHelpFormatter(HelpFormatter):
    """Remove command metavar from help"""

    def format_help(self) -> str:
        return super().format_help().replace(f"  {COMMAND_METAVAR}\n", "")


class PackageParser(ArgumentParser):
    def error(self, message: str) -> NoReturn:
        """Use normal COMMAND metavar when reporting an error"""
        super().error(message.replace(COMMAND_METAVAR, "COMMAND"))


class PackageRunner(Runner):
    """PackageRunner imports a list of runners from specified package."""

    parser: ArgumentParser
    _prefix: str
    _runners: List[Runner]

    def __init__(self, parent: Optional[Runner] = None, prefix: str = "") -> None:
        super().__init__(parent)
        self._prefix = prefix
        self._runners = []

    @property
    def prog(self) -> str:
        if not self._parent or not self._prefix:
            return super().prog
        return f"{self._parent.prog} {self._prefix.split(SEPARATOR)[-1]}"

    @property
    def name(self) -> str:
        return self.package_name if not self._prefix else self._prefix

    @property
    def description(self) -> str:
        return f"Access {self.name} commands"

    @property
    @abstractmethod
    def package_name(self) -> str:
        """Unqualified name of python package"""

    @property
    @abstractmethod
    def package_path(self) -> str:
        """Path of python package containing runners to import during run()"""

    @cached_property
    def module_runners(self) -> List[ModuleRunner]:
        """Runners to provide access to from this package"""
        return [cls(self) for cls in importlib.import_module(f".{self.package_path}", package=__package__).commands]

    @property
    def runners(self) -> Sequence[Runner]:
        """List of runners provided by this package, filtered by current prefix"""

        prefix = self._prefix + SEPARATOR if self._prefix else ""
        return [runner for runner in self.module_runners if runner.name.startswith(prefix)]

    def _get_name(self, runner: Runner) -> str:
        prefix_length = len(self._prefix) + 1 if self._prefix else 0
        return runner.name[prefix_length:]

    @staticmethod
    def _get_command(runner: Runner) -> str:
        return runner.name.split(SEPARATOR)[-1]

    def _get_branches(self) -> Sequence[str]:
        """Get unique set of prefixes (non-leaf commands) for runners under the current prefix.

        The result may be empty if all commands for current prefix are leaves.
        """
        return sorted(
            {self._get_name(runner).split(" ")[0] for runner in self.runners if " " in self._get_name(runner)}
        )

    def _get_leaves(self) -> Sequence[Runner]:
        """Return all leaf runners that can be executed from current prefix"""
        return [runner for runner in self.runners if SEPARATOR not in self._get_name(runner)]

    def configure(self) -> None:
        """Configure argument parser"""

        # Add un-prefixed (leaf) commands:
        self._runners += self._get_leaves()
        # Add prefix runners for subcommands:
        for prefix in self._get_branches():
            branch_name = f"{self._prefix} {prefix}" if self._prefix else prefix
            self._runners.append(self.__class__(self, branch_name))

        self._runners.sort(key=self._get_command)

        # Add runners for this prefix to parser:
        cmd_parser = self.parser.add_subparsers(metavar=COMMAND_METAVAR, title="Available Commands")
        for runner in self._runners:
            cmd_parser.add_parser(
                self._get_command(runner), help=runner.format_description(), add_help=False
            ).set_defaults(runner=runner)

    def run(self, args: List[str]) -> None:
        self.parser = PackageParser(
            prog=f"{self.prog}",
            description=self.format_description(),
            usage=f"{self.prog} [OPTIONS] COMMAND",
            add_help=False,
            formatter_class=PackageHelpFormatter,
            allow_abbrev=False,
        )

        options = self.parser.add_argument_group(title="Options")
        options.add_argument("--help", help="Display available commands and descriptions", action="help")
        self.configure()

        logger.debug("PackageRunner for %s (%s). Received arguments: %s", self.name, self.package_path, args)

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

        if Runner.CHECK in left:
            for runner in self._runners:
                runner.run([Runner.CHECK])
            return None

        # Runner was not selected, perform a full parse so that we error on invalid arguments
        self.parser.parse_args(args)

        # If all arguments were valid, display help
        return self.parser.print_help()
