from __future__ import annotations

from typing import Any, Dict

import attr

# We have to use the real ActionsLinks, because handler checks for it by type
from binarylane.models.actions_links import ActionsLinks
from tests.models.server import Server


@attr.s(auto_attribs=True)
class CreateServerResponse:
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
