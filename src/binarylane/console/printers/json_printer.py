from __future__ import annotations

import json
from typing import Any, List, Optional

from binarylane.console.printers.printer import Printer


class JsonPrinter(Printer):
    """Output an API response as 'raw' JSON"""

    def print(self, response: Any, fields: Optional[List[str]] = None) -> None:
        print(self.format_response(response))

    def format_response(self, response: Any) -> str:
        return json.dumps(response.to_dict() if hasattr(response, "to_dict") else response)
