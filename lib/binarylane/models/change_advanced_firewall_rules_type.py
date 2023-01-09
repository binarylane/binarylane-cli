from __future__ import annotations

from enum import Enum


class ChangeAdvancedFirewallRulesType(str, Enum):
    CHANGE_ADVANCED_FIREWALL_RULES = "change_advanced_firewall_rules"

    def __str__(self) -> str:
        return str(self.value)
