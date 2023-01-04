# pylint: disable=missing-module-docstring
import importlib
from abc import abstractmethod
from argparse import ArgumentParser, HelpFormatter
from typing import List, Optional

from ..cli import debug
from .runner import Runner


class PackageHelpFormatter(HelpFormatter):
    """Remove suppressed metavar from help"""

    # The 24 character width of the suppressed string ensures a fixed left-column size
    SUPPRESS = "!" * 24

    def format_help(self) -> str:
        return super().format_help().replace(f"  {PackageHelpFormatter.SUPPRESS}\n", "")


class PackageRunner(Runner):
    """PackageRunner imports a list of runners from specified package."""

    parser: ArgumentParser

    def __init__(self, parent: Optional[Runner] = None, prefix: str = None) -> None:
        super().__init__(parent)
        self._prefix = prefix

    @property
    def prog(self) -> str:
        return f"{self.parent.prog} {self._prefix}" if self.parent and self._prefix else super().prog

    @property
    @abstractmethod
    def package_path(self) -> str:
        """Path of python package containing runners to import during run()"""

    @property
    def _runners(self) -> List[Runner]:
        """Runners to provide access to from this package"""
        return [cls(self) for cls in importlib.import_module(f".{self.package_path}", package=__package__).commands]

    def configure(self) -> None:
        """Configure argument parser"""

        cmd_parser = self.parser.add_subparsers(metavar=PackageHelpFormatter.SUPPRESS, title="Commands")
        runners = self._runners

        # First, if we are not in a prefix show all prefix commands:
        if not self._prefix:
            for prefix in {runner.name.split("_")[0] for runner in runners if "_" in runner.name}:
                cmd_parser.add_parser(prefix, help=f"Access {prefix} commands", add_help=False).set_defaults(
                    runner=self.__class__(self, prefix)
                )

            # And then add the un-prefixed commands:
            for runner in runners:
                if "_" in runner.name:
                    continue
                cmd_parser.add_parser(runner.name, help=runner.format_description(), add_help=False).set_defaults(
                    runner=runner
                )

        # Otherwise, add commands from the selected prefix
        else:
            for runner in runners:
                if "_" not in runner.name:
                    continue

                prefix, name = runner.name.split("_")
                if prefix == self._prefix:
                    cmd_parser.add_parser(name, help=runner.format_description()).set_defaults(runner=runner)

    def run(self, args: List[str]) -> None:
        self.parser = ArgumentParser(
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

        if Runner.CHECK in left:
            for runner in self._runners:
                runner.run([Runner.CHECK])
            return None

        # If not, display help
        return self.parser.print_help()
