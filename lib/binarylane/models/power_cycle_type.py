from __future__ import annotations

from enum import Enum


class PowerCycleType(str, Enum):
    POWER_CYCLE = "power_cycle"

    def __str__(self) -> str:
        return str(self.value)
