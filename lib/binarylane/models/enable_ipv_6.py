from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.enable_ipv_6_type import EnableIpv6Type

T = TypeVar("T", bound="EnableIpv6")


@attr.s(auto_attribs=True)
class EnableIpv6:
    """Enable IPv6 for a Server

    Attributes:
        type (EnableIpv6Type):
    """

    type: EnableIpv6Type
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = EnableIpv6Type(d.pop("type"))

        enable_ipv_6 = cls(
            type=type,
        )

        enable_ipv_6.additional_properties = d
        return enable_ipv_6

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
