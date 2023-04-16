from __future__ import annotations

import fnmatch
import re
from abc import abstractmethod
from typing import TYPE_CHECKING, Dict, List

from binarylane.console.runners.command import CommandRunner

if TYPE_CHECKING:
    from binarylane.console.parser import Namespace, Parser


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

    def configure(self, parser: Parser) -> None:
        super().configure(parser)

        parser.add_group_help(title="Available fields", entries=self.fields)
        parser.add_argument(
            "--format",
            dest="runner_format",
            help='Comma-separated list of fields to display. Wildcards are supported: \
                e.g. --format "*" will display all fields. (default: "%(default)s")',
            metavar="FIELD,...",
            default=",".join(self.default_format),
        )
        parser.add_argument(
            "-1",
            "--single-column",
            dest="runner_single_column",
            action="store_true",
            help=f"List one {self.default_format[0]} per line.",
        )

    def _matching_fields(self, glob: str) -> List[str]:
        regex = fnmatch.translate(glob)
        matches = [field for field in self.fields if re.match(regex, field)]
        if not matches:
            self._parser.error(f"invalid --format value: '{glob}'")
        return matches

    def process(self, parsed: Namespace) -> None:
        super().process(parsed)

        # --format is a comma-separated list of fields. Field may be a "glob" (containing ? and/or *) to match multiple
        # field names. We want the resulting list of fields to:
        # 1. ordered in the same order as the supplied --format
        # 2. when a glob is used, ordered the same way as the "Available Fields" help
        # 3. not contain any duplicate fields
        # set() does not maintain insertion order, but dict() does, so we create a dict and then extract the keys()
        fmt: str = parsed.runner_format
        self._format = list({match: None for item in fmt.split(",") for match in self._matching_fields(item)}.keys())

        if parsed.runner_single_column:
            self._format = self.default_format[:1]
            self._output = "tsv"
            self._header = False
