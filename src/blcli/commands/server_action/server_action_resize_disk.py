from typing import Any, Union

from ...client.api.server_action.server_action_resize_disk import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.resize_disk import ResizeDisk
from ...client.models.resize_disk_type import ResizeDiskType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "resize-disk"

    @property
    def description(self):
        return """Alter the Size of an Existing Disk for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_resize-disk"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ResizeDiskType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--disk-id",
            dest="disk_id",
            type=str,
            required=True,
            description="""The ID of the existing disk. See server.disks for a list of IDs.""",
        )

        parser.cli_argument(
            "--size-gigabytes",
            dest="size_gigabytes",
            type=int,
            required=True,
            description="""The new size of the disk in GB. If increasing the size of the disk the server must have sufficient unallocated storage space.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ResizeDiskType,
        disk_id: str,
        size_gigabytes: int,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ResizeDisk(
                type=type,
                disk_id=disk_id,
                size_gigabytes=size_gigabytes,
            ),
        )
        return page_response.status_code, page_response.parsed
