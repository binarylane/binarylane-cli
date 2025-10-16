from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.load_balancer_rule_protocol import LoadBalancerRuleProtocol

T = TypeVar("T", bound="ForwardingRuleRequest")


@attr.s(auto_attribs=True)
class ForwardingRuleRequest:
    """
    Attributes:
        entry_protocol (LoadBalancerRuleProtocol): The protocol that traffic must match for this load balancer to
            forward traffic according to this rule.

            | Value | Description |
            | ----- | ----------- |
            | http | The load balancer will forward HTTP traffic that matches this rule. |
            | https | The load balancer will forward HTTPS traffic that matches this rule. |

    """

    entry_protocol: LoadBalancerRuleProtocol
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_protocol = self.entry_protocol.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry_protocol": entry_protocol,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry_protocol = LoadBalancerRuleProtocol(d.pop("entry_protocol"))

        forwarding_rule_request = cls(
            entry_protocol=entry_protocol,
        )

        forwarding_rule_request.additional_properties = d
        return forwarding_rule_request

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
