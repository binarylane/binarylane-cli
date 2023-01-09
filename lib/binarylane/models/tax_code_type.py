from __future__ import annotations

from enum import Enum


class TaxCodeType(str, Enum):
    NONE = "none"
    SCALAR = "scalar"

    def __str__(self) -> str:
        return str(self.value)
