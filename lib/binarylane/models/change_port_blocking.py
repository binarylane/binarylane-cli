from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.change_port_blocking_type import ChangePortBlockingType

T = TypeVar("T", bound="ChangePortBlocking")


@attr.s(auto_attribs=True)
class ChangePortBlocking:
    """Change the Port Blocking for a Server

    Attributes:
        type (ChangePortBlockingType):
        enabled (bool): The desired enabled status for port blocking.
    """

    type: ChangePortBlockingType
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
        type = ChangePortBlockingType(d.pop("type"))

        enabled = d.pop("enabled")

        change_port_blocking = cls(
            type=type,
            enabled=enabled,
        )

        change_port_blocking.additional_properties = d
        return change_port_blocking

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
