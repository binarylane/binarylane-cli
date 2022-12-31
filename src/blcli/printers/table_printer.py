# pylint: disable=missing-module-docstring

from typing import Any

from terminaltables import SingleTable

from .printer import _TablePrinter


class TablePrinter(_TablePrinter):
    """Output a text table with special text characters used to create borders"""

    def _print(self, data: Any) -> None:
        table = SingleTable(data)
        table.inner_heading_row_border = self.header
        print(table.table)
