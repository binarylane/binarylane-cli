from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="CreateVpcRequest")


@attr.s(auto_attribs=True)
class CreateVpcRequest:
    """
    Attributes:
        name (str): A name to help identify this VPC.
        route_entries (Union[Unset, None, List[RouteEntryRequest]]): The route entries that control how network traffic
            is directed through the VPC environment.
        ip_range (Union[Unset, None, str]): A private address range that you select during creation, such as the default
            value of 10.240.0.0/16. Because the virtual network is dedicated to your use, you may use whatever IP address
            range you like.
    """

    name: str
    route_entries: Union[Unset, None, List[RouteEntryRequest]] = UNSET
    ip_range: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        route_entries: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.route_entries, Unset):
            if self.route_entries is None:
                route_entries = None
            else:
                route_entries = []
                for route_entries_item_data in self.route_entries:
                    route_entries_item = route_entries_item_data.to_dict()

                    route_entries.append(route_entries_item)

        ip_range = self.ip_range

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if route_entries is not UNSET:
            field_dict["route_entries"] = route_entries
        if ip_range is not UNSET:
            field_dict["ip_range"] = ip_range

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        route_entries = []
        _route_entries = d.pop("route_entries", UNSET)
        for route_entries_item_data in _route_entries or []:
            route_entries_item = RouteEntryRequest.from_dict(route_entries_item_data)

            route_entries.append(route_entries_item)

        ip_range = d.pop("ip_range", UNSET)

        create_vpc_request = cls(
            name=name,
            route_entries=route_entries,
            ip_range=ip_range,
        )

        create_vpc_request.additional_properties = d
        return create_vpc_request

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
