from __future__ import annotations

from enum import Enum


class ResizeType(str, Enum):
    RESIZE = "resize"

    def __str__(self) -> str:
        return str(self.value)
