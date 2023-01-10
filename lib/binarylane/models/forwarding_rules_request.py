from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.forwarding_rule import ForwardingRule

T = TypeVar("T", bound="ForwardingRulesRequest")


@attr.s(auto_attribs=True)
class ForwardingRulesRequest:
    """
    Attributes:
        forwarding_rules (List[ForwardingRule]): The rules that control which traffic the load balancer will forward to
            servers in the pool.
    """

    forwarding_rules: List[ForwardingRule]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        forwarding_rules = []
        for forwarding_rules_item_data in self.forwarding_rules:
            forwarding_rules_item = forwarding_rules_item_data.to_dict()

            forwarding_rules.append(forwarding_rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "forwarding_rules": forwarding_rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        forwarding_rules = []
        _forwarding_rules = d.pop("forwarding_rules")
        for forwarding_rules_item_data in _forwarding_rules:
            forwarding_rules_item = ForwardingRule.from_dict(forwarding_rules_item_data)

            forwarding_rules.append(forwarding_rules_item)

        forwarding_rules_request = cls(
            forwarding_rules=forwarding_rules,
        )

        forwarding_rules_request.additional_properties = d
        return forwarding_rules_request

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
