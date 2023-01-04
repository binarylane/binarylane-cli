from typing import Any, Dict, List, Union

from ...client.api.server.server_list import sync_detailed
from ...client.client import Client
from ...client.models.servers_response import ServersResponse
from ...client.types import UNSET, Unset
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "memory",
            "vcpus",
            "disk",
            "locked",
            "created_at",
            "status",
            "size_slug",
            "password_change_supported",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this server.""",
            "name": """The hostname of this server.""",
            "memory": """The memory in MB of this server.""",
            "vcpus": """The number of virtual CPUs of this server.""",
            "disk": """The total disk in GB of this server.""",
            "locked": """If this server is locked no actions may be performed.""",
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
            "snapshot_ids": """Snapshots are not currently supported and this will always be an empty array.""",
            "features": """A list of the currently enabled features on this server.""",
            "region": """""",
            "image": """""",
            "size": """""",
            "size_slug": """The slug of the currently selected size for this server.""",
            "networks": """""",
            "tags": """Tags are not currently supported and this will always be an empty array.""",
            "volume_ids": """Volumes are not currently supported and this will always be an empty array.""",
            "disks": """A list of the disks that are currently attached to the server.""",
            "backup_settings": """""",
            "rescue_console": """""",
            "failover_ips": """A list of any assigned failover IP addresses for this server.""",
            "host": """""",
            "password_change_supported": """If this is true the password_reset server action can be called to change a user's password. If this is false the password_reset server action will merely clear the root/administrator password allowing the password to be changed via the web console.""",
            "advanced_features": """""",
            "vpc_id": """The VPC ID that this server is allocated to. If this value is null the server is in the default (public) network for the region.""",
            "selected_size_options": """""",
            "kernel": """""",
            "next_backup_window": """""",
            "cancelled_at": """If the server has been cancelled, this is the date and time in ISO8601 format of that cancellation.""",
            "partner_id": """The server ID of the partner of this server, if one has been assigned.""",
            "permalink": """A randomly generated two-word identifier assigned to servers in regions that support this feature.""",
            "attached_backup": """""",
        }

    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """List All Servers"""

    def configure(self, parser):
        """Add arguments for server_list"""

        parser.cli_argument(
            "--tag-name",
            dest="tag_name",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

    def request(
        self,
        client: Client,
        tag_name: Union[Unset, None, str] = UNSET,
    ) -> Union[Any, ServersResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: ServersResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                tag_name=tag_name,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.servers += page_response.parsed.servers

        return response
