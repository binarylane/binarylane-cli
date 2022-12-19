from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.health_check_protocol import HealthCheckProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthCheck")


@attr.s(auto_attribs=True)
class HealthCheck:
    """
    Attributes:
        protocol (Union[Unset, None, HealthCheckProtocol]):
            | Value | Description |
            | ----- | ----------- |
            | http | The health check will be performed via HTTP. |
            | https | The health check will be performed via HTTPS. |
            | tcp | This option is not currently supported. |
            | both | The health check will be performed via both HTTP and HTTPS. Failing a health check on one protocol will
            remove the server from the pool of servers only for that protocol. |

        path (Union[Unset, None, str]): Leave null to accept the default '/' path.
        port (Union[Unset, None, int]):
        check_interval_seconds (Union[Unset, None, int]):
        response_timeout_seconds (Union[Unset, None, int]):
        unhealthy_threshold (Union[Unset, None, int]):
        healthy_threshold (Union[Unset, None, int]):
    """

    protocol: Union[Unset, None, HealthCheckProtocol] = UNSET
    path: Union[Unset, None, str] = UNSET
    port: Union[Unset, None, int] = UNSET
    check_interval_seconds: Union[Unset, None, int] = UNSET
    response_timeout_seconds: Union[Unset, None, int] = UNSET
    unhealthy_threshold: Union[Unset, None, int] = UNSET
    healthy_threshold: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol: Union[Unset, None, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value if self.protocol else None

        path = self.path
        port = self.port
        check_interval_seconds = self.check_interval_seconds
        response_timeout_seconds = self.response_timeout_seconds
        unhealthy_threshold = self.unhealthy_threshold
        healthy_threshold = self.healthy_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if path is not UNSET:
            field_dict["path"] = path
        if port is not UNSET:
            field_dict["port"] = port
        if check_interval_seconds is not UNSET:
            field_dict["check_interval_seconds"] = check_interval_seconds
        if response_timeout_seconds is not UNSET:
            field_dict["response_timeout_seconds"] = response_timeout_seconds
        if unhealthy_threshold is not UNSET:
            field_dict["unhealthy_threshold"] = unhealthy_threshold
        if healthy_threshold is not UNSET:
            field_dict["healthy_threshold"] = healthy_threshold

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

        port = d.pop("port", UNSET)

        check_interval_seconds = d.pop("check_interval_seconds", UNSET)

        response_timeout_seconds = d.pop("response_timeout_seconds", UNSET)

        unhealthy_threshold = d.pop("unhealthy_threshold", UNSET)

        healthy_threshold = d.pop("healthy_threshold", UNSET)

        health_check = cls(
            protocol=protocol,
            path=path,
            port=port,
            check_interval_seconds=check_interval_seconds,
            response_timeout_seconds=response_timeout_seconds,
            unhealthy_threshold=unhealthy_threshold,
            healthy_threshold=healthy_threshold,
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
