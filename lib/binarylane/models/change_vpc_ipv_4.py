from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.change_vpc_ipv_4_type import ChangeVpcIpv4Type

T = TypeVar("T", bound="ChangeVpcIpv4")


@attr.s(auto_attribs=True)
class ChangeVpcIpv4:
    """Change the IPv4 Address for a Server in a VPC

    Attributes:
        type (ChangeVpcIpv4Type):
        current_ipv4_address (str): The existing Ipv4 address for the private VPC network adapter you wish to change.
        new_ipv4_address (str): The new Ipv4 address for the private VPC network adapter.
    """

    type: ChangeVpcIpv4Type
    current_ipv4_address: str
    new_ipv4_address: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        current_ipv4_address = self.current_ipv4_address
        new_ipv4_address = self.new_ipv4_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "current_ipv4_address": current_ipv4_address,
                "new_ipv4_address": new_ipv4_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeVpcIpv4Type(d.pop("type"))

        current_ipv4_address = d.pop("current_ipv4_address")

        new_ipv4_address = d.pop("new_ipv4_address")

        change_vpc_ipv_4 = cls(
            type=type,
            current_ipv4_address=current_ipv4_address,
            new_ipv4_address=new_ipv4_address,
        )

        change_vpc_ipv_4.additional_properties = d
        return change_vpc_ipv_4

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
