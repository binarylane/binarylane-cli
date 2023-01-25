from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from binarylane.models.forwarding_rule import ForwardingRule
from binarylane.models.health_check import HealthCheck
from binarylane.models.load_balancer_status import LoadBalancerStatus
from binarylane.models.region import Region
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancer")


@attr.s(auto_attribs=True)
class LoadBalancer:
    """
    Attributes:
        id (int): The ID of the load balancer.
        name (str): The hostname of the load balancer.
        ip (str): The IPv4 address of the load balancer.
        status (LoadBalancerStatus):
            | Value | Description |
            | ----- | ----------- |
            | new | The load balancer is currently being built and is not ready to accept connections. |
            | active | The load balancer is available. |
            | errored | The load balancer is in an errored state. |

        created_at (datetime.datetime): The date and time in ISO8601 format of the creation of the load balancer.
        forwarding_rules (List[ForwardingRule]): The rules that control which traffic the load balancer will forward to
            servers in the pool.
        health_check (HealthCheck): The rules that determine which servers are considered 'healthy' and in the server
            pool for the load balancer.
        server_ids (List[int]): The server IDs of the servers that are currently in the load balancer pool (regardless
            of their current 'health').
        region (Union[Unset, None, Region]): The region the load balancer is located in. If this value is null the load
            balancer is an 'AnyCast' load balancer.
    """

    id: int
    name: str
    ip: str
    status: LoadBalancerStatus
    created_at: datetime.datetime
    forwarding_rules: List[ForwardingRule]
    health_check: HealthCheck
    server_ids: List[int]
    region: Union[Unset, None, Region] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        ip = self.ip
        status = self.status.value

        created_at = self.created_at.isoformat()

        forwarding_rules = []
        for forwarding_rules_item_data in self.forwarding_rules:
            forwarding_rules_item = forwarding_rules_item_data.to_dict()

            forwarding_rules.append(forwarding_rules_item)

        health_check = self.health_check.to_dict()

        server_ids = self.server_ids

        region: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict() if self.region else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ip": ip,
                "status": status,
                "created_at": created_at,
                "forwarding_rules": forwarding_rules,
                "health_check": health_check,
                "server_ids": server_ids,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        ip = d.pop("ip")

        status = LoadBalancerStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        forwarding_rules = []
        _forwarding_rules = d.pop("forwarding_rules")
        for forwarding_rules_item_data in _forwarding_rules:
            forwarding_rules_item = ForwardingRule.from_dict(forwarding_rules_item_data)

            forwarding_rules.append(forwarding_rules_item)

        health_check = HealthCheck.from_dict(d.pop("health_check"))

        server_ids = cast(List[int], d.pop("server_ids"))

        _region = d.pop("region", UNSET)
        region: Union[Unset, None, Region]
        if _region is None:
            region = None
        elif isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        load_balancer = cls(
            id=id,
            name=name,
            ip=ip,
            status=status,
            created_at=created_at,
            forwarding_rules=forwarding_rules,
            health_check=health_check,
            server_ids=server_ids,
            region=region,
        )

        load_balancer.additional_properties = d
        return load_balancer

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
