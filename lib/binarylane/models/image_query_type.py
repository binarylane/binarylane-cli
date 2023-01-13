from __future__ import annotations

from enum import Enum


class ImageQueryType(str, Enum):
    DISTRIBUTION = "distribution"
    BACKUP = "backup"

    def __str__(self) -> str:
        return str(self.value)
