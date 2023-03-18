from __future__ import annotations

from enum import Enum


class ServerStatus(str, Enum):
    NEW = "new"
    ACTIVE = "active"
    ARCHIVE = "archive"
    OFF = "off"

    def __str__(self) -> str:
        return str(self.value)
