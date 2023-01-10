from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.route_entry_request import RouteEntryRequest
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="UpdateVpcRequest")


@attr.s(auto_attribs=True)
class UpdateVpcRequest:
    """Any properties that are not included will be cleared.

    Attributes:
        name (str): A name to help identify this VPC.
        route_entries (Union[Unset, None, List[RouteEntryRequest]]): The route entries that control how network traffic
            is directed through the VPC environment.
    """

    name: str
    route_entries: Union[Unset, None, List[RouteEntryRequest]] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if route_entries is not UNSET:
            field_dict["route_entries"] = route_entries

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

        update_vpc_request = cls(
            name=name,
            route_entries=route_entries,
        )

        update_vpc_request.additional_properties = d
        return update_vpc_request

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
