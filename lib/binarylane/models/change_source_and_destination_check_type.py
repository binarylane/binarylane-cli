from __future__ import annotations

from enum import Enum


class ChangeSourceAndDestinationCheckType(str, Enum):
    CHANGE_SOURCE_AND_DESTINATION_CHECK = "change_source_and_destination_check"

    def __str__(self) -> str:
        return str(self.value)
