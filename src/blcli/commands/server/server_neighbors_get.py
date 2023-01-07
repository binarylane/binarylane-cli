from typing import Any, Dict, List, Union

from ...client.api.server.server_neighbors_get import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.server_neighbors_response import ServerNeighborsResponse
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
        return "get"

    @property
    def description(self):
        return """List All Servers That Share a Host with a Server"""

    def configure(self, parser):
        """Add arguments for server_neighbors_get"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server for which neighbours should be listed.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, ServerNeighborsResponse]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
