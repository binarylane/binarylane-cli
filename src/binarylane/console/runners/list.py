from __future__ import annotations

from abc import abstractmethod
from typing import Any, Dict, List

from binarylane.console.runners.command import CommandRunner


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

    def run(self, args: List[str]) -> None:
        self._parser.add_group_help(title="Available fields", entries=self.fields)
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

        for field in self._format:
            if field not in self.fields:
                self._parser.error(f"invalid --format value: '{field}'")

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
