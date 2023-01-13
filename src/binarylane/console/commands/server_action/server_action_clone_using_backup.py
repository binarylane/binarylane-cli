from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_clone_using_backup import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.clone_using_backup import CloneUsingBackup
from binarylane.models.clone_using_backup_type import CloneUsingBackupType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "clone-using-backup"

    @property
    def description(self) -> str:
        return """Restore a Backup of a Server to a Different Existing Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_clone-using-backup"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            CloneUsingBackupType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--image-id",
            int,
            dest="image_id",
            required=True,
            description="""The ID of the image to clone. Only backup type images are currently supported. This must be a backup of the server ID in the action endpoint URL.""",
        )

        parser.cli_argument(
            "--target-server-id",
            int,
            dest="target_server_id",
            required=True,
            description="""The target server ID. This server's current disks will be wiped and replaced with the selected backup image.""",
        )

        parser.cli_argument(
            "--name",
            Union[Unset, None, str],
            dest="name",
            required=False,
            description="""The new hostname for the target server. If this is not supplied the target server's existing hostname will be used.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: CloneUsingBackupType,
        image_id: int,
        target_server_id: int,
        name: Union[Unset, None, str] = UNSET,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=CloneUsingBackup(
                type=type,
                image_id=image_id,
                target_server_id=target_server_id,
                name=name,
            ),
        )
        return page_response.status_code, page_response.parsed
