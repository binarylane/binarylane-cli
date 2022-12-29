"""CLI entrypoint"""
import sys
from typing import List

from .runners import PackageRunner


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

    def run(self, args: List[str]) -> None:
        # Allowing doing `bl help command [subcommand...]` instead of --help
        if args and args[0] == "help":
            args = args[1:] + [self.HELP]

        return super().run(args)


def main() -> None:
    """CLI entrypoint"""

    App().run(sys.argv[1:])
