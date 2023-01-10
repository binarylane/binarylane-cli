from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.server import Server

T = TypeVar("T", bound="ServerNeighborsResponse")


@attr.s(auto_attribs=True)
class ServerNeighborsResponse:
    """
    Attributes:
        servers (List[Server]):
    """

    servers: List[Server]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        servers = []
        for servers_item_data in self.servers:
            servers_item = servers_item_data.to_dict()

            servers.append(servers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "servers": servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        servers = []
        _servers = d.pop("servers")
        for servers_item_data in _servers:
            servers_item = Server.from_dict(servers_item_data)

            servers.append(servers_item)

        server_neighbors_response = cls(
            servers=servers,
        )

        server_neighbors_response.additional_properties = d
        return server_neighbors_response

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
