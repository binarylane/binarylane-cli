from functools import cached_property
from typing import List, Sequence

from ..runners import PackageRunner, Runner
from .configure import ConfigureRunner
from .version import VersionRunner


class App(PackageRunner):
    """
    AppRunner is the 'root' runner for the application. In normal usage, all command line arguments are passed
    directly to run(). Apart from global flags, the primary function of this class is to invoke the
    appropriate runner for the supplied arguments.
    """

    @property
    def package_name(self) -> str:
        return "bl"

    @property
    def description(self) -> str:
        return "bl is a command-line interface for the BinaryLane API"

    @property
    def package_path(self) -> str:
        return ".commands"

    @property
    def runners(self) -> Sequence[Runner]:
        return list(super().runners) + self.app_runners

    @cached_property
    def app_runners(self) -> List[Runner]:
        """Additional runners to include"""
        return [VersionRunner(self), ConfigureRunner(self)]

    def run(self, args: List[str]) -> None:
        # Allowing doing `bl help command [subcommand...]` instead of --help
        if args and args[0] == "help":
            args = args[1:] + [self.HELP]

        return super().run(args)
