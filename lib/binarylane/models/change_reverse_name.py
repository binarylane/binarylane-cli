from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.change_reverse_name_type import ChangeReverseNameType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ChangeReverseName")


@attr.s(auto_attribs=True)
class ChangeReverseName:
    """Change the Reverse Name for an IPv4 Address on a Server

    Attributes:
        type (ChangeReverseNameType):
        ipv4_address (str): The IPv4 address to set or clear the reverse name for.
        reverse_name (Union[Unset, None, str]): Leave this null to clear the custom reverse name.
    """

    type: ChangeReverseNameType
    ipv4_address: str
    reverse_name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        ipv4_address = self.ipv4_address
        reverse_name = self.reverse_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "ipv4_address": ipv4_address,
            }
        )
        if reverse_name is not UNSET:
            field_dict["reverse_name"] = reverse_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeReverseNameType(d.pop("type"))

        ipv4_address = d.pop("ipv4_address")

        reverse_name = d.pop("reverse_name", UNSET)

        change_reverse_name = cls(
            type=type,
            ipv4_address=ipv4_address,
            reverse_name=reverse_name,
        )

        change_reverse_name.additional_properties = d
        return change_reverse_name

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
