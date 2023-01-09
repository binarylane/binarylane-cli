from __future__ import annotations

from abc import abstractmethod
from argparse import SUPPRESS
from typing import Any, Dict, List

from binarylane.console.runners.command_runner import CommandRunner


class ListRunner(CommandRunner):
    """ListRunner displays a received list with user-customisable field list"""

    _format: List[str]
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

    def _add_fields_help(self) -> None:
        """Add a list of available fields to displayed help"""

        fields_help = self._parser.add_argument_group("Available fields")
        for key, value in self.fields.items():
            # FIXME: Use HelpFormatter to create an epilog instead
            #
            # NOTE: These group arguments will never parse, the group exists purely to provide argparse-formatted help -
            # dest: starts with '_field_` so that it is cannot be same as as anther argument
            # metavar: field name, displayed as-is in argument group's help
            # nargs: SUPPRESS (since python 3.7) will cause it to accept no arguments nor be shown in usage
            # default: SUPPRESS so that f'_field_{key}' is not added to parsed namespace object
            # help: description of the field
            fields_help.add_argument(
                f"_field_{key}", metavar=key, nargs=SUPPRESS, default=SUPPRESS, help=value
            ).required = False

    def run(self, args: List[str]) -> None:
        self._add_fields_help()
        self._parser.add_argument(
            "--format",
            dest="runner_format",
            help="Comma-separated list of fields to display. (Default: %(default)s)",
            metavar="FIELD,FIELD,...",
            default=",".join(self.default_format),
        )

        self._parser.add_argument(
            "-1",
            "--single-column",
            dest="runner_single_column",
            action="store_true",
            help=f"List one {self.default_format[0]} per line.",
        )

        super().run(args)

    def process(self, parsed: Any) -> None:
        self._format = parsed.runner_format.split(",")

        if parsed.runner_single_column:
            self._format = self.default_format[:1]
            self._output = "tsv"
            self._header = False

        super().process(parsed)

    def response(self, status_code: int, received: Any) -> None:
        if status_code != 200:
            super().response(status_code, received)
        elif received:
            self._printer.print(received, self._format)
