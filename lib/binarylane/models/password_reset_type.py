from __future__ import annotations

from enum import Enum


class PasswordResetType(str, Enum):
    PASSWORD_RESET = "password_reset"

    def __str__(self) -> str:
        return str(self.value)
