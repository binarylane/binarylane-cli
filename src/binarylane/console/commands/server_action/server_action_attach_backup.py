from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_attach_backup import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.attach_backup import AttachBackup
from binarylane.models.attach_backup_type import AttachBackupType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "attach-backup"

    @property
    def description(self):
        return """Attach a Backup to a Server"""

    def configure(self, parser):
        """Add arguments for server-action_attach-backup"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            AttachBackupType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--image",
            int,
            dest="image",
            required=True,
            description="""Only attaching backup images is currently supported.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: AttachBackupType,
        image: int,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=AttachBackup(
                type=type,
                image=image,
            ),
        )
        return page_response.status_code, page_response.parsed
