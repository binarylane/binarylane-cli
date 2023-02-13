from __future__ import annotations

from typing import List, Union

from binarylane.console.printers.printer import _TablePrinter


class TsvPrinter(_TablePrinter):
    """Output a formatted response as tab-separated values"""

    def _render(self, data: List[List[str]], title: Union[str, None]) -> str:
        title = title + "\n" if title else ""
        return title + "\n".join(["\t".join(item).replace("\n", "\\n") for item in data])
