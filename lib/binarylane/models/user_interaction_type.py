from __future__ import annotations

from enum import Enum


class UserInteractionType(str, Enum):
    CONTINUE_AFTER_PING_FAILURE = "continue-after-ping-failure"
    ALLOW_UNCLEAN_POWER_OFF = "allow-unclean-power-off"

    def __str__(self) -> str:
        return str(self.value)
