from enum import Enum


class UptimeType(str, Enum):
    UPTIME = "uptime"

    def __str__(self) -> str:
        return str(self.value)
