from typing import Any, Union

from ...client.api.server_action.server_action_add_disk import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.add_disk import AddDisk
from ...client.models.add_disk_type import AddDiskType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "add-disk"

    @property
    def description(self):
        return """Create an Additional Disk for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_add-disk"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=AddDiskType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--size-gigabytes",
            dest="size_gigabytes",
            type=int,
            required=True,
            description="""The size of the new disk in GB. The server must have at least this much unallocated storage space.""",
        )

        parser.cli_argument(
            "--description",
            dest="description",
            type=Union[Unset, None, str],
            required=False,
            description="""An optional description for the disk.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: AddDiskType,
        size_gigabytes: int,
        description: Union[Unset, None, str] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=AddDisk(
                type=type,
                size_gigabytes=size_gigabytes,
                description=description,
            ),
        )
        return page_response.status_code, page_response.parsed
