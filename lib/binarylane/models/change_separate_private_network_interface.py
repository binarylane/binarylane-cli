from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.change_separate_private_network_interface_type import ChangeSeparatePrivateNetworkInterfaceType

T = TypeVar("T", bound="ChangeSeparatePrivateNetworkInterface")


@attr.s(auto_attribs=True)
class ChangeSeparatePrivateNetworkInterface:
    """Enable or Disable a Separate Private Network Interface for a Server in a VPC

    Attributes:
        type (ChangeSeparatePrivateNetworkInterfaceType):
        enabled (bool): The desired enabled status of the separate second network interface.
    """

    type: ChangeSeparatePrivateNetworkInterfaceType
    enabled: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "enabled": enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeSeparatePrivateNetworkInterfaceType(d.pop("type"))

        enabled = d.pop("enabled")

        change_separate_private_network_interface = cls(
            type=type,
            enabled=enabled,
        )

        change_separate_private_network_interface.additional_properties = d
        return change_separate_private_network_interface

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
