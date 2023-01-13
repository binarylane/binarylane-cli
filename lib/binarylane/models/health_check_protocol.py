from __future__ import annotations

from enum import Enum


class HealthCheckProtocol(str, Enum):
    HTTP = "http"
    HTTPS = "https"
    BOTH = "both"

    def __str__(self) -> str:
        return str(self.value)
