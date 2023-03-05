from __future__ import annotations

import argparse
from typing import List, Sequence
from binarylane.pycompat.functools import cached_property

from binarylane.console.app.lazy_loader import LazyLoader
from binarylane.console.runners import Runner
from binarylane.console.runners.package import PackageRunner


# FIXME: Combination of PackageRunner._prefix and App's overrides is difficult to support correctly
class AppRunner(PackageRunner):
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
            LazyLoader(self.context, ".app.configure", "configure", "Configure access to BinaryLane API"),
            LazyLoader(self.context, ".app.version", "version", "Show the current version"),
        ]

    def run(self, args: List[str]) -> None:
        # Allowing doing `bl help command [subcommand...]` instead of --help
        if args and args[0] == "help":
            args = args[1:] + [self.HELP]

        return super().run(args)

    def configure(self) -> None:
        super().configure()
        config_section, api_url = self.context.config_section, self.context.api_url
        self._options.add_argument(
            "--context", metavar="NAME", help=f'Name of authentication context to use (default: "{config_section}")'
        )
        self._options.add_argument("--api-token", metavar="VALUE", help="API token to use with BinaryLane API")
        self._options.add_argument("--api-url", metavar="URL", help=f'URL of BinaryLane API (default: "{api_url}")')

    def process(self, parsed: argparse.Namespace) -> None:
        # Only run this once, at the top level
        if not self._prefix:
            self.context.initialize(commandline=parsed)
