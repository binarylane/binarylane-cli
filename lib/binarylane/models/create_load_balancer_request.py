from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.forwarding_rule import ForwardingRule
from binarylane.models.health_check import HealthCheck
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="CreateLoadBalancerRequest")


@attr.s(auto_attribs=True)
class CreateLoadBalancerRequest:
    """
    Attributes:
        name (str): The hostname of the load balancer.
        forwarding_rules (Union[Unset, None, List[ForwardingRule]]): The rules that control which traffic the load
            balancer will forward to servers in the pool. Leave null to accept a default "HTTP" only forwarding rule.
        health_check (Union[Unset, None, HealthCheck]): The rules that determine which servers are considered 'healthy'
            and in the server pool for the load balancer. Leave this null to accept appropriate defaults based on the
            forwarding_rules.
        server_ids (Union[Unset, None, List[int]]): A list of server IDs to assign to this load balancer.
        region (Union[Unset, None, str]): Leave null to create an anycast load balancer.
    """

    name: str
    forwarding_rules: Union[Unset, None, List[ForwardingRule]] = UNSET
    health_check: Union[Unset, None, HealthCheck] = UNSET
    server_ids: Union[Unset, None, List[int]] = UNSET
    region: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        forwarding_rules: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.forwarding_rules, Unset):
            if self.forwarding_rules is None:
                forwarding_rules = None
            else:
                forwarding_rules = []
                for forwarding_rules_item_data in self.forwarding_rules:
                    forwarding_rules_item = forwarding_rules_item_data.to_dict()

                    forwarding_rules.append(forwarding_rules_item)

        health_check: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.health_check, Unset):
            health_check = self.health_check.to_dict() if self.health_check else None

        server_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.server_ids, Unset):
            if self.server_ids is None:
                server_ids = None
            else:
                server_ids = self.server_ids

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if forwarding_rules is not UNSET:
            field_dict["forwarding_rules"] = forwarding_rules
        if health_check is not UNSET:
            field_dict["health_check"] = health_check
        if server_ids is not UNSET:
            field_dict["server_ids"] = server_ids
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        forwarding_rules = []
        _forwarding_rules = d.pop("forwarding_rules", UNSET)
        for forwarding_rules_item_data in _forwarding_rules or []:
            forwarding_rules_item = ForwardingRule.from_dict(forwarding_rules_item_data)

            forwarding_rules.append(forwarding_rules_item)

        _health_check = d.pop("health_check", UNSET)
        health_check: Union[Unset, None, HealthCheck]
        if _health_check is None:
            health_check = None
        elif isinstance(_health_check, Unset):
            health_check = UNSET
        else:
            health_check = HealthCheck.from_dict(_health_check)

        server_ids = cast(List[int], d.pop("server_ids", UNSET))

        region = d.pop("region", UNSET)

        create_load_balancer_request = cls(
            name=name,
            forwarding_rules=forwarding_rules,
            health_check=health_check,
            server_ids=server_ids,
            region=region,
        )

        create_load_balancer_request.additional_properties = d
        return create_load_balancer_request

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
