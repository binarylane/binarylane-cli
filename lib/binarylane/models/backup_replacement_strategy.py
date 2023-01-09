from __future__ import annotations

from enum import Enum


class BackupReplacementStrategy(str, Enum):
    NONE = "none"
    SPECIFIED = "specified"
    OLDEST = "oldest"
    NEWEST = "newest"

    def __str__(self) -> str:
        return str(self.value)
