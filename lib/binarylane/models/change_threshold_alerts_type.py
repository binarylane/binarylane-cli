from __future__ import annotations

from enum import Enum


class ChangeThresholdAlertsType(str, Enum):
    CHANGE_THRESHOLD_ALERTS = "change_threshold_alerts"

    def __str__(self) -> str:
        return str(self.value)
