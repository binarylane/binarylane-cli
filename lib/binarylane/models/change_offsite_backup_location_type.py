from __future__ import annotations

from enum import Enum


class ChangeOffsiteBackupLocationType(str, Enum):
    CHANGE_OFFSITE_BACKUP_LOCATION = "change_offsite_backup_location"

    def __str__(self) -> str:
        return str(self.value)
