from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.advanced_firewall_rule_action import AdvancedFirewallRuleAction
from binarylane.models.advanced_firewall_rule_protocol import AdvancedFirewallRuleProtocol
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="AdvancedFirewallRule")


@attr.s(auto_attribs=True)
class AdvancedFirewallRule:
    """
    Attributes:
        source_addresses (List[str]): The source addresses to match for this rule. Each address may be an individual
            IPv4 address or a range in IPv4 CIDR notation.
        destination_addresses (List[str]): The destination addresses to match for this rule. Each address may be an
            individual IPv4 address or a range in IPv4 CIDR notation.
        protocol (AdvancedFirewallRuleProtocol): The protocol to match for this rule.
        action (AdvancedFirewallRuleAction): The action to take when there is a match on this rule.
        destination_ports (Union[Unset, None, List[str]]): The destination ports to match for this rule. Leave null or
            empty to match on all ports.
        description (Union[Unset, None, str]): A description to assist in identifying this rule. Commonly used to record
            the reason for the rule or the intent behind it, e.g. "Block access to RDP" or "Allow access from HQ".
    """

    source_addresses: List[str]
    destination_addresses: List[str]
    protocol: AdvancedFirewallRuleProtocol
    action: AdvancedFirewallRuleAction
    destination_ports: Union[Unset, None, List[str]] = UNSET
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source_addresses = self.source_addresses

        destination_addresses = self.destination_addresses

        protocol = self.protocol.value

        action = self.action.value

        destination_ports: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.destination_ports, Unset):
            if self.destination_ports is None:
                destination_ports = None
            else:
                destination_ports = self.destination_ports

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_addresses": source_addresses,
                "destination_addresses": destination_addresses,
                "protocol": protocol,
                "action": action,
            }
        )
        if destination_ports is not UNSET:
            field_dict["destination_ports"] = destination_ports
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        source_addresses = cast(List[str], d.pop("source_addresses"))

        destination_addresses = cast(List[str], d.pop("destination_addresses"))

        protocol = AdvancedFirewallRuleProtocol(d.pop("protocol"))

        action = AdvancedFirewallRuleAction(d.pop("action"))

        destination_ports = cast(List[str], d.pop("destination_ports", UNSET))

        description = d.pop("description", UNSET)

        advanced_firewall_rule = cls(
            source_addresses=source_addresses,
            destination_addresses=destination_addresses,
            protocol=protocol,
            action=action,
            destination_ports=destination_ports,
            description=description,
        )

        advanced_firewall_rule.additional_properties = d
        return advanced_firewall_rule

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
