from typing import Any, Dict, List, Union

from ...client.api.server.server_snapshot_list import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...client.models.snapshots_response import SnapshotsResponse
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "type",
            "public",
            "min_disk_size",
            "size_gigabytes",
            "status",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this image.""",
            "name": """The name of this image.""",
            "type": """
| Value | Description |
| ----- | ----------- |
| custom | An image uploaded by a user. |
| snapshot | A snapshot. Snapshot creation is not currently supported so only distribution images will have this value. |
| backup | A backup of a server. |

""",
            "public": """A public image is available to all users. A private image is available only to the account that created the image.""",
            "regions": """The slugs of the regions where the image is available for use.""",
            "min_disk_size": """For a distribution image this is the minimum disk size in GB required to install the operating system. For a backup image this is the minimum total disk size in GB required to restore the backup.""",
            "size_gigabytes": """For a distribution image this is the disk size used in GB by the operating system on initial install. For a backup image this is the size of the compressed backup image in GB.""",
            "tags": """Tags are not currently supported and this will always be an empty array.""",
            "status": """
| Value | Description |
| ----- | ----------- |
| NEW | The image is new. |
| available | The image is available for use. |
| pending | The image is pending and is not yet available for use. |
| deleted | The image has been deleted and is no longer available for use. |

""",
            "distribution_info": """""",
            "distribution": """If this is an operating system image, this is the name of the distribution. If this is a backup image, this is the name of the distribution the server is using.""",
            "full_name": """If this is an operating system image, this is the name and version of the distribution. If this is a backup image, this is the name and version of the distribution the server is using.""",
            "slug": """If this is an operating system image this is a slug which may be used as an alternative to the ID as a reference.""",
            "created_at": """If this is a backup image this is the date and time in ISO8601 format when the image was created.""",
            "description": """A description that may provide further details or warnings about the image.""",
            "error_message": """If the image creation failed this may provide further information.""",
            "min_memory_megabytes": """This is minimum memory in MB necessary to support this operating system (or the base operating system for a backup image).""",
            "distribution_surcharges": """""",
            "backup_info": """""",
        }

    @property
    def name(self):
        return "server_snapshot_list"

    @property
    def description(self):
        return """List all Snapshots for a Server"""

    def configure(self, parser):
        """Add arguments for server_snapshot_list"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, SnapshotsResponse]:

        page = 0
        per_page = 25
        has_next = True
        response: SnapshotsResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=server_id,
                client=client,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.snapshots += page_response.parsed.snapshots

        return response
