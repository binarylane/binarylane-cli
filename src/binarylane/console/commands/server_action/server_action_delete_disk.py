from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_delete_disk import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.delete_disk import DeleteDisk
from binarylane.models.delete_disk_type import DeleteDiskType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
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
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            DeleteDiskType,
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

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: DeleteDiskType,
        disk_id: str,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=DeleteDisk(
                type=type,
                disk_id=disk_id,
            ),
        )
        return page_response.status_code, page_response.parsed
