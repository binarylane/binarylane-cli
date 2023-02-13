from __future__ import annotations

import sys
from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union

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

    def print(self, response: Any, fields: Optional[List[str]] = None) -> None:
        """Format response and print to stdout"""
        output = self._format(response, self.header, fields)
        print(output, file=sys.stdout)

    def error(self, response: Any) -> None:
        """Format error response and print to stderr"""
        output = self._format(response, True)
        print(output, file=sys.stderr)

    @abstractmethod
    def _format(self, response: Any, header: bool, fields: Optional[List[str]] = None) -> str:
        """format the response data"""


class _TablePrinter(Printer):
    def _format(self, response: Any, header: bool, fields: Optional[List[str]] = None) -> str:
        """format the response data"""
        formatted = formatter.format_response(response, header, fields)

        if isinstance(formatted["table"], list) and len(formatted["table"]) > 0:
            return self._render(formatted["table"], formatted["title"]) + "\n"

        if isinstance(formatted["title"], str):
            return formatted["title"] + "\n"

        return ""

    @abstractmethod
    def _render(self, data: List[List[str]], title: Union[str, None]) -> str:
        """Class-specific table renderer"""
