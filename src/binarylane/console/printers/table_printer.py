from __future__ import annotations

import sys
from typing import List, Union

from terminaltables import DoubleTable, SingleTable  # type: ignore

from binarylane.console.printers.printer import _TablePrinter


class TablePrinter(_TablePrinter):
    """Output a text table with special text characters used to create borders"""

    def __init__(self) -> None:
        super().__init__()
        self.table_class = SingleTable if sys.stdout.isatty() else DoubleTable

    def _render(self, data: List[List[str]], title: Union[str, None]) -> str:
        table = self.table_class(data)
        table.inner_heading_row_border = self.header
        title = title + "\n" if title else ""
        return title + table.table
