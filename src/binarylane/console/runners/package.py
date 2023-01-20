from __future__ import annotations

import importlib
import logging
from abc import abstractmethod
from argparse import ArgumentParser, HelpFormatter
from functools import cached_property
from typing import List, NoReturn, Optional, Sequence

from binarylane.console.runners import Runner
from binarylane.console.runners.module import ModuleRunner

logger = logging.getLogger(__name__)

# The 24 character width of the metavar ensures a fixed left-column size
COMMAND_METAVAR = "!" * 24


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
    _prefix: Optional[str]
    _runners: List[Runner]

    def __init__(self, parent: Optional[Runner] = None, prefix: Optional[str] = None) -> None:
        super().__init__(parent)
        self._prefix = prefix
        self._runners = []

    @property
    def prog(self) -> str:
        return f"{self._parent.prog} {self._prefix}" if self._parent and self._prefix else super().prog

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
        """List of runners provided by this package"""
        return self.module_runners

    def _get_prefixes(self) -> Sequence[str]:
        """Get unique set of prefixes for runners in this package.

        A runner has a "prefix" if its name contains an underscore, in which case the prefix the leading string.
        - runner for 'domain_list' has prefix of 'domain'
        - runner for 'list' does not have a prefix

        The resulting sequence may be empty if there are no runners with an underscore in the name.
        """
        return sorted({runner.name.split("_")[0] for runner in self.runners if "_" in runner.name})

    def _get_unprefixed_runners(self) -> Sequence[Runner]:
        """Return all runners from package_runners that do not have a prefix"""
        return [runner for runner in self.runners if "_" not in runner.name]

    def _get_prefix_runners(self, prefix: str) -> Sequence[Runner]:
        """Filter package_runners by the supplied prefix."""
        return [runner for runner in self.runners if "_" in runner.name and runner.name.split("_")[0] == prefix]

    def configure(self) -> None:
        """Configure argument parser"""

        # If we are not in a prefix:
        if not self._prefix:
            # Add any required prefix runners:
            for prefix in self._get_prefixes():
                self._runners.append(self.__class__(self, prefix))
            # And then the un-prefixed commands:
            self._runners += self._get_unprefixed_runners()
        # Otherwise, add commands from the selected prefix:
        else:
            self._runners += self._get_prefix_runners(self._prefix)

        # Add runners for this prefix to parser:
        cmd_parser = self.parser.add_subparsers(metavar=COMMAND_METAVAR, title="Commands")
        for runner in self._runners:
            cmd_parser.add_parser(
                runner.name.split("_")[-1], help=runner.format_description(), add_help=False
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
