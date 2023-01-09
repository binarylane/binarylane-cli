from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List, Optional

from binarylane.console.printers import formatter


class Printer(ABC):
    """A Printer is responsible for formatting a structured API response and printing it to stdout"""

    _header: bool

    def __init__(self) -> None:
        self._header = True

    @property
    def header(self) -> bool:
        """Boolean specifying whether output should include field names in a header."""
        return self._header

    @header.setter
    def header(self, value: bool) -> None:
        self._header = value

    @abstractmethod
    def print(self, response: Any, fields: Optional[List[str]] = None) -> None:
        """Format response and print to stdout"""


class _TablePrinter(Printer):
    def print(self, response: Any, fields: Optional[List[str]] = None) -> None:
        data = formatter.format_response(response, self.header, fields)

        if isinstance(data, str):
            print(data)
        else:
            self._print(data)

    @abstractmethod
    def _print(self, data: Any) -> None:
        """Class-specific printer behaviour"""
