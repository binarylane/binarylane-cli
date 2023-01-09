from __future__ import annotations

from enum import Enum


class PowerOffType(str, Enum):
    POWER_OFF = "power_off"

    def __str__(self) -> str:
        return str(self.value)
