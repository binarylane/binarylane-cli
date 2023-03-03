from __future__ import annotations

import os
from typing import ClassVar, Optional

from binarylane.console.config.option import Option
from binarylane.console.config.source import Source


class EnvironmentSource(Source):
    prefix: ClassVar[str] = "BL_"

    def __init__(self) -> None:
        self._items = {self._get_name(key): value for key, value in os.environ.items() if key.startswith(self.prefix)}

    def _get_name(self, key: str) -> str:
        return key[len(self.prefix) :].lower().replace("_", "-")

    def get(self, name: Option) -> Optional[str]:
        return self._items.get(name, None)
