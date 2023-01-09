from __future__ import annotations

from enum import Enum


class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit-card"
    PAYPAL = "paypal"

    def __str__(self) -> str:
        return str(self.value)
