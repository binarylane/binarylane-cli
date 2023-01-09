from __future__ import annotations

from enum import Enum


class RenameType(str, Enum):
    RENAME = "rename"

    def __str__(self) -> str:
        return str(self.value)
