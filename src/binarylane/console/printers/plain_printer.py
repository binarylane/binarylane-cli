from __future__ import annotations

from typing import Any

from terminaltables import SingleTable  # type: ignore

from binarylane.console.printers.printer import _TablePrinter


class PlainPrinter(_TablePrinter):
    """Output a plain (borderless) table"""

    def _print(self, data: Any) -> None:
        table = SingleTable(data)
        table.inner_heading_row_border = False
        table.outer_border = False
        table.inner_column_border = False
        print(table.table)
