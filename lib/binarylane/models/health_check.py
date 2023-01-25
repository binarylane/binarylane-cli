from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.health_check_protocol import HealthCheckProtocol
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="HealthCheck")


@attr.s(auto_attribs=True)
class HealthCheck:
    """
    Attributes:
        protocol (Union[Unset, None, HealthCheckProtocol]): Leave null to accept the default HTTP protocol.
        path (Union[Unset, None, str]): Leave null to accept the default '/' path.
    """

    protocol: Union[Unset, None, HealthCheckProtocol] = UNSET
    path: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol: Union[Unset, None, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value if self.protocol else None

        path = self.path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if path is not UNSET:
            field_dict["path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, None, HealthCheckProtocol]
        if _protocol is None:
            protocol = None
        elif isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = HealthCheckProtocol(_protocol)

        path = d.pop("path", UNSET)

        health_check = cls(
            protocol=protocol,
            path=path,
        )

        health_check.additional_properties = d
        return health_check

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
