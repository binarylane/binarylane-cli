from __future__ import annotations

from enum import Enum


class EnableBackupsType(str, Enum):
    ENABLE_BACKUPS = "enable_backups"

    def __str__(self) -> str:
        return str(self.value)
