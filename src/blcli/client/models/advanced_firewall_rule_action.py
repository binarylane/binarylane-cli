from enum import Enum


class AdvancedFirewallRuleAction(str, Enum):
    DROP = "drop"
    ACCEPT = "accept"

    def __str__(self) -> str:
        return str(self.value)
