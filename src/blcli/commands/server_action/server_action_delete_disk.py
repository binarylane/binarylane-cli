from typing import Any, Union

from ...client.api.server_action.server_action_delete_disk import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.delete_disk import DeleteDisk
from ...client.models.delete_disk_type import DeleteDiskType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete-disk"

    @property
    def description(self):
        return """Delete an Additional Disk for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_delete-disk"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=DeleteDiskType,
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

    def request(
        self,
        server_id: int,
        client: Client,
        type: DeleteDiskType,
        disk_id: str,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=DeleteDisk(
                type=type,
                disk_id=disk_id,
            ),
        ).parsed
