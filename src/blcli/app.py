"""CLI entrypoint"""
import importlib
import importlib.metadata
import sys
from typing import List, Optional

from .runners import PackageRunner, Runner


class VersionRunner(Runner):
    """Display blcli package version"""

    @property
    def name(self) -> str:
        return "version"

    @property
    def description(self) -> str:
        return "Show the current version"

    def run(self, args: List[str]) -> None:
        package = __package__
        version = self._distribution_version(package) or self._module_version(package) or "dev"

        print(package, version)

    def _distribution_version(self, package: str) -> Optional[str]:
        try:
            return importlib.metadata.distribution(package).version
        except importlib.metadata.PackageNotFoundError:
            return None

    def _module_version(self, package: str) -> Optional[str]:
        try:
            return importlib.import_module("._version", package).__version__
        except ModuleNotFoundError:
            return None


class App(PackageRunner):
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

    @property
    def _runners(self) -> List[Runner]:
        return super()._runners + [VersionRunner()]

    def run(self, args: List[str]) -> None:
        # Allowing doing `bl help command [subcommand...]` instead of --help
        if args and args[0] == "help":
            args = args[1:] + [self.HELP]

        return super().run(args)


def main() -> None:
    """CLI entrypoint"""

    App().run(sys.argv[1:])
