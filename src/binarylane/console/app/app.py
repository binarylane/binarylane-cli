from __future__ import annotations

from typing import List, Sequence
from binarylane.pycompat.functools import cached_property

from binarylane.console.app.lazy_loader import LazyLoader
from binarylane.console.runners import Runner
from binarylane.console.runners.package import PackageRunner


# FIXME: Combination of PackageRunner._prefix and App's overrides is difficult to support correctly
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
        if self._prefix:
            return super().description
        return "bl is a command-line interface for the BinaryLane API"

    @property
    def package_path(self) -> str:
        return ".commands"

    @property
    def runners(self) -> Sequence[Runner]:
        if self._prefix:
            return super().runners
        return list(super().runners) + self.app_runners

    @cached_property
    def app_runners(self) -> List[Runner]:
        return [
            LazyLoader(self, ".app.configure", "configure", "Configure access to BinaryLane API"),
            LazyLoader(self, ".app.version", "version", "Show the current version"),
        ]

    def run(self, args: List[str]) -> None:
        # Allowing doing `bl help command [subcommand...]` instead of --help
        if args and args[0] == "help":
            args = args[1:] + [self.HELP]

        return super().run(args)
