from typing import Any, Dict, List, Union

import attr

from binarylane.types import UNSET, Unset
from tests.models.links import Links
from tests.models.meta import Meta
from tests.models.server import Server


@attr.s(auto_attribs=True)
class ServersResponse:
    meta: Meta
    servers: List[Server]
    links: Union[Unset, None, Links] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        meta = self.meta.to_dict()

        servers = []
        for servers_item_data in self.servers:
            servers_item = servers_item_data.to_dict()

            servers.append(servers_item)

        links: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict() if self.links else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "meta": meta,
                "servers": servers,
            }
        )
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict
