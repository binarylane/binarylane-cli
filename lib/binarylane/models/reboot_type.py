from __future__ import annotations

from enum import Enum


class RebootType(str, Enum):
    REBOOT = "reboot"

    def __str__(self) -> str:
        return str(self.value)
