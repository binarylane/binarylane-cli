# pylint: disable=missing-module-docstring

from typing import Any

from .printer import _TablePrinter


class TsvPrinter(_TablePrinter):
    """Output a formatted response as tab-separated values"""

    def _print(self, data: Any) -> None:
        for item in data:
            print("\t".join(item).replace("\n", "\\n"))
