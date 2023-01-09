from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.actions_links import ActionsLinks
from binarylane.models.server import Server

T = TypeVar("T", bound="CreateServerResponse")


@attr.s(auto_attribs=True)
class CreateServerResponse:
    """
    Attributes:
        server (Server):
        links (ActionsLinks):
    """

    server: Server
    links: ActionsLinks
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server = self.server.to_dict()

        links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "server": server,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server = Server.from_dict(d.pop("server"))

        links = ActionsLinks.from_dict(d.pop("links"))

        create_server_response = cls(
            server=server,
            links=links,
        )

        create_server_response.additional_properties = d
        return create_server_response

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
