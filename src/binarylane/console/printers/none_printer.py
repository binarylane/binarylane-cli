from __future__ import annotations

from typing import Any, List, Optional

from binarylane.console.printers.printer import Printer


class NonePrinter(Printer):
    def print(self, response: Any, fields: Optional[List[str]] = None) -> None:
        pass
