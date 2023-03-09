from __future__ import annotations

from enum import Enum


class NetworkType(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
