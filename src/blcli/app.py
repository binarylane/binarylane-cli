"""CLI entrypoint"""
import sys
from typing import List

from .runner import AppRunner


class App:
    """Class representing the app as a whole"""

    def __init__(self) -> None:
        self.runner = AppRunner()

    def __call__(self, args: List[str]) -> None:
        self.runner(args)


def main() -> None:
    """CLI entrypoint"""

    # Currently this is what triggers all the argparse construction, so its slow:
    # debug_time(lambda: importlib.import_module(".client", package=__package__), "import .client")
    # debug_time(lambda: cli.run(sys.argv[1:]), "cli.run()")

    app = App()
    app(sys.argv[1:])
