# pylint: disable=missing-module-docstring

import importlib
from abc import abstractmethod
from typing import Any, Dict, List

from ..cli import CommandParser, debug, display, get_api_token
from .runner import Runner


class CommandRunner(Runner):
    """CommandRunner parses input, executes API operation and displays the result"""

    parser: CommandParser
    parent: Runner

    def __init__(self, parent: Runner) -> None:
        super().__init__(parent)
        self.parser = CommandParser(prog=self.prog, add_help=False)
        self.parser.add_argument(
            "--help", dest="runner_print_help", action="store_true", help="Display command options and descriptions"
        )
        self.configure(self.parser)

    @property
    def prog(self) -> str:
        return self.parent.prog

    @abstractmethod
    def configure(self, parser: CommandParser) -> None:
        """Add supported CLI arguments"""

    @abstractmethod
    def request(self, **kwargs: Dict[str, Any]) -> Any:
        """Perform API operation and return response"""

    def response(self, received: Any) -> None:
        """Format and display response received from API operation"""
        display(received)

    def print_help(self) -> None:
        """Display help for this runner"""
        self.parser.print_help()

    def process(self, parsed: Any) -> None:
        """Process runner-local arguments"""
        if parsed.runner_print_help:
            self.print_help()
            raise SystemExit()
        del parsed.runner_print_help

    def run(self, args: List[str]) -> None:
        debug(f"Command parser for {self.name}. args: {args}")
        parsed = self.parser.parse_args(args)
        debug(f"Parsing succeeded, have {parsed}")

        self.process(parsed)

        authenticated_client = importlib.import_module("..client", __package__).AuthenticatedClient
        client = authenticated_client(
            "https://api.binarylane.com.au",
            get_api_token(),
        )

        parsed.client = client

        self.response(self.request(**vars(parsed)))
