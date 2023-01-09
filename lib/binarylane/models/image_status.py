from __future__ import annotations

from enum import Enum


class ImageStatus(str, Enum):
    NEW = "NEW"
    AVAILABLE = "available"
    PENDING = "pending"
    DELETED = "deleted"

    def __str__(self) -> str:
        return str(self.value)
