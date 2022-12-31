# pylint: disable=missing-module-docstring

from abc import abstractmethod
from typing import Any, Dict, List

from ..printers import PrinterType, get_printer
from .command_runner import CommandRunner


class ListRunner(CommandRunner):
    """ListRunner displays a received list with user-customisable field list"""

    format: List[str]
    output: str
    header: bool

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

        printers = tuple(item.name.lower() for item in PrinterType)
        self.parser.add_argument(
            "--output",
            dest="runner_output",
            default="table",
            metavar="OUTPUT",
            choices=printers,
            help='Desired output format [%(choices)s] (Default: "%(default)s")',
        )
        self.parser.add_argument(
            "-1",
            "--single-column",
            dest="runner_single_column",
            action="store_true",
            help=f"List one {self.default_format[0]} per line.",
        )
        self.parser.add_argument(
            "--no-header",
            dest="runner_no_header",
            action="store_true",
            help="Display columns without field labels",
        )
        super().run(args)

    def process(self, parsed: Any) -> None:
        self.output = parsed.runner_output
        self.format = parsed.runner_format.split(",")
        self.header = not parsed.runner_no_header

        if parsed.runner_single_column:
            self.format = self.default_format[:1]
            self.output = "plain"
            self.header = False

        super().process(parsed)

    def response(self, received: Any) -> None:
        printer = get_printer(self.output)
        printer.header = self.header
        printer.print_list(received, self.format)
