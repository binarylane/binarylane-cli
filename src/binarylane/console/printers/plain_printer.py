from __future__ import annotations

from typing import List, Union

from terminaltables import SingleTable  # type: ignore

from binarylane.console.printers.printer import _TablePrinter


class PlainPrinter(_TablePrinter):
    """Output a plain (borderless) table"""

    def _render(self, data: List[List[str]], title: Union[str, None]) -> str:
        table = SingleTable(data)
        table.inner_heading_row_border = False
        table.outer_border = False
        table.inner_column_border = False
        table.title = title
        return table.table
