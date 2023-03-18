from __future__ import annotations

from typing import Any, Dict, List, Union

import attr

from binarylane.types import UNSET, Unset
from tests.models.network import Network


@attr.s(auto_attribs=True)
class Networks:
    v4: List[Network]
    v6: List[Network]
    port_blocking: bool
    recent_ddos: bool
    separate_private_network_interface: Union[Unset, None, bool] = UNSET
    source_and_destination_check: Union[Unset, None, bool] = UNSET
    ipv6_reverse_nameservers: Union[Unset, None, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        v4 = []
        for v4_item_data in self.v4:
            v4_item = v4_item_data.to_dict()

            v4.append(v4_item)

        v6 = []
        for v6_item_data in self.v6:
            v6_item = v6_item_data.to_dict()

            v6.append(v6_item)

        port_blocking = self.port_blocking
        recent_ddos = self.recent_ddos
        separate_private_network_interface = self.separate_private_network_interface
        source_and_destination_check = self.source_and_destination_check
        ipv6_reverse_nameservers: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.ipv6_reverse_nameservers, Unset):
            if self.ipv6_reverse_nameservers is None:
                ipv6_reverse_nameservers = None
            else:
                ipv6_reverse_nameservers = self.ipv6_reverse_nameservers

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "v4": v4,
                "v6": v6,
                "port_blocking": port_blocking,
                "recent_ddos": recent_ddos,
            }
        )
        if separate_private_network_interface is not UNSET:
            field_dict["separate_private_network_interface"] = separate_private_network_interface
        if source_and_destination_check is not UNSET:
            field_dict["source_and_destination_check"] = source_and_destination_check
        if ipv6_reverse_nameservers is not UNSET:
            field_dict["ipv6_reverse_nameservers"] = ipv6_reverse_nameservers

        return field_dict
