# pylint: disable=missing-module-docstring

from abc import abstractmethod
from typing import Any, Dict, List

from ..cli import display
from .command_runner import CommandRunner


class ListRunner(CommandRunner):
    """ListRunner displays a received list with user-customisable field list"""

    format: List[str]

    @property
    @abstractmethod
    def default_format(self) -> List[str]:
        """Default list of fields from response object to display"""

    @property
    @abstractmethod
    def fields(self) -> Dict[str, str]:
        """Map of field name: description for all available fields"""

    def print_help(self) -> None:
        fields_help = self.parser.add_subparsers(metavar="", title="available fields")
        for key, value in self.fields.items():
            fields_help.add_parser(key, help=value)
        # This is a workaround for python3.8 ArgumentParser unnecessarily crushing the first column width
        fields_help.add_parser(" " * 24, help="")

        return super().print_help()

    def run(self, args: List[str]) -> None:
        self.parser.add_argument(
            "--format",
            dest="runner_format",
            help="Comma-separated list of fields to display. (Default: %(default)s)",
            metavar="FIELD,FIELD,...",
            default=",".join(self.default_format),
        )
        super().run(args)

    def process(self, parsed: Any) -> None:
        super().process(parsed)

        self.format = parsed.runner_format.split(",")
        del parsed.runner_format

    def response(self, received: Any) -> None:
        display(received, self.format)
