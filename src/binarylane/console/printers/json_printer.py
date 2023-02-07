from __future__ import annotations

import json
from typing import Any, List, Optional

from binarylane.console.printers.printer import Printer


class JsonPrinter(Printer):
    """Output an API response as 'raw' JSON"""

    def _format(self, response: Any, _header: bool, _fields: Optional[List[str]] = None) -> str:
        return json.dumps(response.to_dict(), indent=2)
