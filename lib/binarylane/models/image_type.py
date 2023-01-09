from __future__ import annotations

from enum import Enum


class ImageType(str, Enum):
    CUSTOM = "custom"
    SNAPSHOT = "snapshot"
    BACKUP = "backup"

    def __str__(self) -> str:
        return str(self.value)
