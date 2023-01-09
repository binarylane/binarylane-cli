from __future__ import annotations

from enum import Enum


class PowerOnType(str, Enum):
    POWER_ON = "power_on"

    def __str__(self) -> str:
        return str(self.value)
