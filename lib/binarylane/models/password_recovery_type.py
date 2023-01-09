from __future__ import annotations

from enum import Enum


class PasswordRecoveryType(str, Enum):
    MANUAL = "manual"
    OFFLINE_CLEAR = "offline-clear"
    OFFLINE_CHANGE = "offline-change"
    ONLINE_CHANGE = "online-change"

    def __str__(self) -> str:
        return str(self.value)
