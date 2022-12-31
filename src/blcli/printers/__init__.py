"""Printers provide different methods of formatting and displaying API responses"""
from enum import Enum

from .json_printer import JsonPrinter
from .plain_printer import PlainPrinter
from .printer import Printer
from .table_printer import TablePrinter
from .tsv_printer import TsvPrinter


class PrinterType(Enum):
    """Enum of available printer implementations"""

    PLAIN = PlainPrinter
    TABLE = TablePrinter
    TSV = TsvPrinter
    JSON = JsonPrinter


def get_printer(name: str) -> Printer:
    """Returns Printer object of the requested type"""
    try:
        return PrinterType[name.upper()].value()
    except KeyError as exc:
        raise ValueError(f'Invalid PrinterType: "{name}"') from exc
