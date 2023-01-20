from __future__ import annotations

import sys
from typing import Any

from terminaltables import DoubleTable, SingleTable  # type: ignore

from binarylane.console.printers.printer import _TablePrinter


class TablePrinter(_TablePrinter):
    """Output a text table with special text characters used to create borders"""

    def __init__(self) -> None:
        super().__init__()
        self.table_class = SingleTable if sys.stdout.isatty() else DoubleTable

    def _print(self, data: Any) -> None:
        table = self.table_class(data)
        table.inner_heading_row_border = self.header
        print(table.table)
