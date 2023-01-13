from __future__ import annotations

from enum import Enum


class LoadBalancerRuleProtocol(str, Enum):
    HTTP = "http"
    HTTPS = "https"

    def __str__(self) -> str:
        return str(self.value)
