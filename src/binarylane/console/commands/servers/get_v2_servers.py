from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, List, Optional, Tuple, Union

from binarylane.api.servers.get_v2_servers import sync_detailed
from binarylane.models.links import Links
from binarylane.models.servers_response import ServersResponse
from binarylane.types import UNSET, Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    hostname: Union[Unset, None, str] = UNSET


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "image",
            "vcpus",
            "memory",
            "disk",
            "region",
            "networks",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this server.""",
            "name": """The hostname of this server.""",
            "memory": """The memory in MB of this server.""",
            "vcpus": """The number of virtual CPUs of this server.""",
            "disk": """The total disk in GB of this server.""",
            "created_at": """The date and time in ISO8601 format of this server's initial creation.""",
            "status": """
| Value | Description |
| ----- | ----------- |
| new | The server is currently in the process of building and is not yet available for use. |
| active | The server is available for use. |
| archive | The server is powered off due to cancellation or non payment. |
| off | The server has been powered off, but may be powered back on. |

""",
            "backup_ids": """A list of the currently existing backup image IDs for this server (if any).""",
            "features": """A list of the currently enabled features on this server.""",
            "region": """The region this server is allocated to.""",
            "image": """The base image used to create this server.""",
            "size": """The currently selected size for this server.""",
            "size_slug": """The slug of the currently selected size for this server.""",
            "networks": """A list of the networks of the server.""",
            "disks": """A list of the disks that are currently attached to the server.""",
            "backup_settings": """Detailed backup settings for the server.""",
            "rescue_console": """Details of the rescue console for this server.""",
            "failover_ips": """A list of any assigned failover IP addresses for this server.""",
            "host": """Summary information about the host of this server.""",
            "password_change_supported": """If this is true the password_reset server action can be called to change a user's password. If this is false the password_reset server action will merely clear the root/administrator password allowing the password to be changed via the web console.""",
            "advanced_features": """The currently enabled advanced features, machine type and processor flags.""",
            "vpc_id": """The VPC ID that this server is allocated to. If this value is null the server is in the default (public) network for the region.""",
            "selected_size_options": """An object that details the selected options for the current size.""",
            "kernel": """The currently selected kernel for the server.""",
            "next_backup_window": """The details of the next scheduled backup, if any.""",
            "cancelled_at": """If the server has been cancelled, this is the date and time in ISO8601 format of that cancellation.""",
            "partner_id": """The server ID of the partner of this server, if one has been assigned.""",
            "permalink": """A randomly generated two-word identifier assigned to servers in regions that support this feature.""",
            "attached_backup": """An object that provides details of any backup image currently attached to the server..""",
        }

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All Servers"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "hostname",
            Union[Unset, None, str],
            required=False,
            option_name="hostname",
            description="""Providing a hostname restricts the results to the server that has this hostname (case insensitive). If this parameter is provided at most 1 server will be returned.""",
        )
        return mapping

    @property
    def ok_response_type(self) -> type:
        return ServersResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ServersResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ServersResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[ServersResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                hostname=request.hostname,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, ServersResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.servers += page_response.parsed.servers

        return status_code, response
