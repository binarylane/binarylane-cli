from __future__ import annotations

from enum import Enum


class DataInterval(str, Enum):
    FIVE_MINUTE = "five-minute"
    HALF_HOUR = "half-hour"
    FOUR_HOUR = "four-hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"

    def __str__(self) -> str:
        return str(self.value)
