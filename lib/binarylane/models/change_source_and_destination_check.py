from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.change_source_and_destination_check_type import ChangeSourceAndDestinationCheckType

T = TypeVar("T", bound="ChangeSourceAndDestinationCheck")


@attr.s(auto_attribs=True)
class ChangeSourceAndDestinationCheck:
    """Enable or Disable Network Source and Destination Checks for a Server in a VPC

    Attributes:
        type (ChangeSourceAndDestinationCheckType):
        enabled (bool): The desired enabled status of the source and destination checks for network packets.
    """

    type: ChangeSourceAndDestinationCheckType
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
        type = ChangeSourceAndDestinationCheckType(d.pop("type"))

        enabled = d.pop("enabled")

        change_source_and_destination_check = cls(
            type=type,
            enabled=enabled,
        )

        change_source_and_destination_check.additional_properties = d
        return change_source_and_destination_check

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
