from __future__ import annotations

from enum import Enum


class DistributionFeature(str, Enum):
    SSH = "ssh"
    REMOTE_DESKTOP = "remote-desktop"
    USER_DATA = "user-data"

    def __str__(self) -> str:
        return str(self.value)
