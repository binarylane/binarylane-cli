from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_resize_disk import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.resize_disk import ResizeDisk
from binarylane.models.resize_disk_type import ResizeDiskType
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
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
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ResizeDiskType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--disk-id",
            str,
            dest="disk_id",
            required=True,
            description="""The ID of the existing disk. See server.disks for a list of IDs.""",
        )

        parser.cli_argument(
            "--size-gigabytes",
            int,
            dest="size_gigabytes",
            required=True,
            description="""The new size of the disk in GB. If increasing the size of the disk the server must have sufficient unallocated storage space.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

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
