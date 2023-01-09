from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from binarylane.models.change_ipv_6_reverse_nameservers_type import ChangeIpv6ReverseNameserversType

T = TypeVar("T", bound="ChangeIpv6ReverseNameservers")


@attr.s(auto_attribs=True)
class ChangeIpv6ReverseNameservers:
    """Update the IPv6 Reverse Name Servers for a Server

    Attributes:
        type (ChangeIpv6ReverseNameserversType):
        ipv6_reverse_nameservers (List[str]): A list of all IPv6 reverse name servers for this server. Any existing
            reverse name servers that are omitted from the list will be removed from the server.
    """

    type: ChangeIpv6ReverseNameserversType
    ipv6_reverse_nameservers: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        ipv6_reverse_nameservers = self.ipv6_reverse_nameservers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "ipv6_reverse_nameservers": ipv6_reverse_nameservers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeIpv6ReverseNameserversType(d.pop("type"))

        ipv6_reverse_nameservers = cast(List[str], d.pop("ipv6_reverse_nameservers"))

        change_ipv_6_reverse_nameservers = cls(
            type=type,
            ipv6_reverse_nameservers=ipv6_reverse_nameservers,
        )

        change_ipv_6_reverse_nameservers.additional_properties = d
        return change_ipv_6_reverse_nameservers

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
