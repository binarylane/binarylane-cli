from __future__ import annotations

from typing import Any, Dict, Union

import attr

from binarylane.types import UNSET, Unset
from tests.models.network_type import NetworkType


@attr.s(auto_attribs=True)
class Network:
    ip_address: str
    type: NetworkType
    netmask: Union[None, Unset, int, str] = UNSET
    gateway: Union[Unset, None, str] = UNSET
    reverse_name: Union[Unset, None, str] = UNSET
    nat_target: Union[Unset, None, str] = UNSET

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
