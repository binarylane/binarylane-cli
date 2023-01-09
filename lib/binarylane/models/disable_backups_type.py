from __future__ import annotations

from enum import Enum


class DisableBackupsType(str, Enum):
    DISABLE_BACKUPS = "disable_backups"

    def __str__(self) -> str:
        return str(self.value)
