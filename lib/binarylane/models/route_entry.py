from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="RouteEntry")


@attr.s(auto_attribs=True)
class RouteEntry:
    """
    Attributes:
        router (str): The server that will receive traffic sent to the destination property in this VPC.
        destination (str): The destination address for this route entry. This may be in CIDR format.
        description (Union[Unset, None, str]): An optional description for the route.
    """

    router: str
    destination: str
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        router = self.router
        destination = self.destination
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "router": router,
                "destination": destination,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        router = d.pop("router")

        destination = d.pop("destination")

        description = d.pop("description", UNSET)

        route_entry = cls(
            router=router,
            destination=destination,
            description=description,
        )

        route_entry.additional_properties = d
        return route_entry

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
