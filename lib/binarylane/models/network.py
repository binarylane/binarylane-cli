from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.network_type import NetworkType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Network")


@attr.s(auto_attribs=True)
class Network:
    """
    Attributes:
        ip_address (str): The IP address for this network.
        type (NetworkType):
            | Value | Description |
            | ----- | ----------- |
            | private | A private (non internet accessible) network. |
            | public | A public (internet accessible) network. |

        netmask (Union[None, Unset, int, str]): The netmask for this network. Example: 5.
        gateway (Union[Unset, None, str]): The gateway for this network.
        reverse_name (Union[Unset, None, str]): The reverse name (if any) for this network.
        nat_target (Union[Unset, None, str]): If this is not null this property is the private IP address which receives
            packets from this network.
    """

    ip_address: str
    type: NetworkType
    netmask: Union[None, Unset, int, str] = UNSET
    gateway: Union[Unset, None, str] = UNSET
    reverse_name: Union[Unset, None, str] = UNSET
    nat_target: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip_address = self.ip_address
        type = self.type.value

        netmask: Union[None, Unset, int, str]
        if isinstance(self.netmask, Unset):
            netmask = UNSET
        elif self.netmask is None:
            netmask = None

        else:
            netmask = self.netmask

        gateway = self.gateway
        reverse_name = self.reverse_name
        nat_target = self.nat_target

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ip_address": ip_address,
                "type": type,
            }
        )
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if reverse_name is not UNSET:
            field_dict["reverse_name"] = reverse_name
        if nat_target is not UNSET:
            field_dict["nat_target"] = nat_target

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip_address = d.pop("ip_address")

        type = NetworkType(d.pop("type"))

        def _parse_netmask(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        netmask = _parse_netmask(d.pop("netmask", UNSET))

        gateway = d.pop("gateway", UNSET)

        reverse_name = d.pop("reverse_name", UNSET)

        nat_target = d.pop("nat_target", UNSET)

        network = cls(
            ip_address=ip_address,
            type=type,
            netmask=netmask,
            gateway=gateway,
            reverse_name=reverse_name,
            nat_target=nat_target,
        )

        network.additional_properties = d
        return network

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
