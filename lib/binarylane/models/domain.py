from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Domain")


@attr.s(auto_attribs=True)
class Domain:
    """
    Attributes:
        name (str): The name of the domain.
        current_nameservers (List[str]): The current authoritative name servers for this domain.
        zone_file (str): The zone file for the selected domain. If the DNS records for this domain are not managed
            locally this is what the zone file would be if the authority was delegated to us.
        ttl (Union[Unset, None, int]): The time to live for records in this domain in seconds. If the DNS records for
            this domain are not managed locally this will be what the TTL would be if the authority was delegated to us.
    """

    name: str
    current_nameservers: List[str]
    zone_file: str
    ttl: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        current_nameservers = self.current_nameservers

        zone_file = self.zone_file
        ttl = self.ttl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "current_nameservers": current_nameservers,
                "zone_file": zone_file,
            }
        )
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        current_nameservers = cast(List[str], d.pop("current_nameservers"))

        zone_file = d.pop("zone_file")

        ttl = d.pop("ttl", UNSET)

        domain = cls(
            name=name,
            current_nameservers=current_nameservers,
            zone_file=zone_file,
            ttl=ttl,
        )

        domain.additional_properties = d
        return domain

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
