from __future__ import annotations

from enum import Enum


class ChangeAdvancedFeaturesType(str, Enum):
    CHANGE_ADVANCED_FEATURES = "change_advanced_features"

    def __str__(self) -> str:
        return str(self.value)
