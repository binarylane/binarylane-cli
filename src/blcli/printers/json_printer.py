# pylint: disable=missing-module-docstring

import json
from typing import Any, List, Optional

from .printer import Printer


class JsonPrinter(Printer):
    """Output an API response as 'raw' JSON"""

    def print_list(self, response: List[Any], fields: Optional[List[str]] = None) -> None:
        print(json.dumps(response))

    def _print(self, data: Any) -> None:
        pass
