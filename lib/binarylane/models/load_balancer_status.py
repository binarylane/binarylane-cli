from __future__ import annotations

from enum import Enum


class LoadBalancerStatus(str, Enum):
    NEW = "new"
    ACTIVE = "active"
    ERRORED = "errored"

    def __str__(self) -> str:
        return str(self.value)
