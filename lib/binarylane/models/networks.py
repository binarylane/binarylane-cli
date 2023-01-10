from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.network import Network
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Networks")


@attr.s(auto_attribs=True)
class Networks:
    """
    Attributes:
        v4 (List[Network]): A list of the IPv4 networks for this server.
        v6 (List[Network]): A list of the IPv6 networks for this server.
        port_blocking (bool): Whether the default port blocking is enabled for this server.
        recent_ddos (bool): If this is true this server has been the target of a recent DDOS attack. An email will have
            been sent to your email address when the DDOS was detected (and if it has ended, when it ended) with more
            details.
        separate_private_network_interface (Union[Unset, None, bool]): Whether a separate private network interface is
            provided for the server's VPC traffic.
        source_and_destination_check (Union[Unset, None, bool]): If enabled, this server is only able to send and
            receive data packets directly addressed to an IP address assigned to this server.
        ipv6_reverse_nameservers (Union[Unset, None, List[str]]): Any configured IPv6 reverse nameservers for this
            server. Please see our documentation for how this interacts with IPv6 nameserver settings at the account level.
    """

    v4: List[Network]
    v6: List[Network]
    port_blocking: bool
    recent_ddos: bool
    separate_private_network_interface: Union[Unset, None, bool] = UNSET
    source_and_destination_check: Union[Unset, None, bool] = UNSET
    ipv6_reverse_nameservers: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

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
        field_dict.update(self.additional_properties)
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

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        v4 = []
        _v4 = d.pop("v4")
        for v4_item_data in _v4:
            v4_item = Network.from_dict(v4_item_data)

            v4.append(v4_item)

        v6 = []
        _v6 = d.pop("v6")
        for v6_item_data in _v6:
            v6_item = Network.from_dict(v6_item_data)

            v6.append(v6_item)

        port_blocking = d.pop("port_blocking")

        recent_ddos = d.pop("recent_ddos")

        separate_private_network_interface = d.pop("separate_private_network_interface", UNSET)

        source_and_destination_check = d.pop("source_and_destination_check", UNSET)

        ipv6_reverse_nameservers = cast(List[str], d.pop("ipv6_reverse_nameservers", UNSET))

        networks = cls(
            v4=v4,
            v6=v6,
            port_blocking=port_blocking,
            recent_ddos=recent_ddos,
            separate_private_network_interface=separate_private_network_interface,
            source_and_destination_check=source_and_destination_check,
            ipv6_reverse_nameservers=ipv6_reverse_nameservers,
        )

        networks.additional_properties = d
        return networks

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
