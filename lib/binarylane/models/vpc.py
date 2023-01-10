from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.route_entry import RouteEntry

T = TypeVar("T", bound="Vpc")


@attr.s(auto_attribs=True)
class Vpc:
    """
    Attributes:
        id (int): The ID of this VPC.
        name (str): The name of this VPC.
        ip_range (str): The IPv4 range for this VPC in CIDR format.
        route_entries (List[RouteEntry]): The route entries that control how network traffic is directed through the VPC
            environment.
    """

    id: int
    name: str
    ip_range: str
    route_entries: List[RouteEntry]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        ip_range = self.ip_range
        route_entries = []
        for route_entries_item_data in self.route_entries:
            route_entries_item = route_entries_item_data.to_dict()

            route_entries.append(route_entries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ip_range": ip_range,
                "route_entries": route_entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        ip_range = d.pop("ip_range")

        route_entries = []
        _route_entries = d.pop("route_entries")
        for route_entries_item_data in _route_entries:
            route_entries_item = RouteEntry.from_dict(route_entries_item_data)

            route_entries.append(route_entries_item)

        vpc = cls(
            id=id,
            name=name,
            ip_range=ip_range,
            route_entries=route_entries,
        )

        vpc.additional_properties = d
        return vpc

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
