from __future__ import annotations

from typing import Optional

from binarylane.console.config.option import Option
from binarylane.console.config.source import Source


class RuntimeSource(Source):
    name: Option
    value: str

    def __init__(self, name: Option, value: str) -> None:
        self.name = name
        self.value = value

    def get(self, name: Option) -> Optional[str]:
        return self.value if self.name == name else None
