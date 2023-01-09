from __future__ import annotations

from enum import Enum


class ChangePortBlockingType(str, Enum):
    CHANGE_PORT_BLOCKING = "change_port_blocking"

    def __str__(self) -> str:
        return str(self.value)
