"""Printers provide different methods of formatting and displaying API responses"""

from __future__ import annotations

from enum import Enum

from binarylane.console.printers.json_printer import JsonPrinter
from binarylane.console.printers.none_printer import NonePrinter
from binarylane.console.printers.plain_printer import PlainPrinter
from binarylane.console.printers.printer import Printer
from binarylane.console.printers.table_printer import TablePrinter
from binarylane.console.printers.tsv_printer import TsvPrinter

__all__ = [
    "Printer",
    "create_printer",
]


class PrinterType(Enum):
    """Enum of available printer implementations"""

    PLAIN = PlainPrinter
    TABLE = TablePrinter
    TSV = TsvPrinter
    JSON = JsonPrinter
    NONE = NonePrinter


def create_printer(name: str) -> Printer:
    """Returns Printer object of the requested type"""
    try:
        return PrinterType[name.upper()].value()
    except KeyError as exc:
        raise ValueError(f'Invalid PrinterType: "{name}"') from exc
