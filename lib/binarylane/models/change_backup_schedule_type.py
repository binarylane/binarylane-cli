from __future__ import annotations

from enum import Enum


class ChangeBackupScheduleType(str, Enum):
    CHANGE_BACKUP_SCHEDULE = "change_backup_schedule"

    def __str__(self) -> str:
        return str(self.value)
