from __future__ import annotations

from enum import Enum


class PingType(str, Enum):
    PING = "ping"

    def __str__(self) -> str:
        return str(self.value)
