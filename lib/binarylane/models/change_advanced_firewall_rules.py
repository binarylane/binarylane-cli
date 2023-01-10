from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.advanced_firewall_rule import AdvancedFirewallRule
from binarylane.models.change_advanced_firewall_rules_type import ChangeAdvancedFirewallRulesType

T = TypeVar("T", bound="ChangeAdvancedFirewallRules")


@attr.s(auto_attribs=True)
class ChangeAdvancedFirewallRules:
    """Change the Advanced Firewall Rules for a Server

    Attributes:
        type (ChangeAdvancedFirewallRulesType):
        firewall_rules (List[AdvancedFirewallRule]): A list of rules for the server. NB: that any existing rules that
            are not included will be removed. Submit an empty list to clear all rules.
    """

    type: ChangeAdvancedFirewallRulesType
    firewall_rules: List[AdvancedFirewallRule]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        firewall_rules = []
        for firewall_rules_item_data in self.firewall_rules:
            firewall_rules_item = firewall_rules_item_data.to_dict()

            firewall_rules.append(firewall_rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "firewall_rules": firewall_rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeAdvancedFirewallRulesType(d.pop("type"))

        firewall_rules = []
        _firewall_rules = d.pop("firewall_rules")
        for firewall_rules_item_data in _firewall_rules:
            firewall_rules_item = AdvancedFirewallRule.from_dict(firewall_rules_item_data)

            firewall_rules.append(firewall_rules_item)

        change_advanced_firewall_rules = cls(
            type=type,
            firewall_rules=firewall_rules,
        )

        change_advanced_firewall_rules.additional_properties = d
        return change_advanced_firewall_rules

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
