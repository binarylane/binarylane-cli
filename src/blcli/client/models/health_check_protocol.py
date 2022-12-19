from enum import Enum


class HealthCheckProtocol(str, Enum):
    HTTP = "http"
    HTTPS = "https"
    TCP = "tcp"
    BOTH = "both"

    def __str__(self) -> str:
        return str(self.value)
