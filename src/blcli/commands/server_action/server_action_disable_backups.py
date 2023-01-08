from typing import Any, Type, Union

from ...client.api.server_action.server_action_disable_backups import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.disable_backups import DisableBackups
from ...client.models.disable_backups_type import DisableBackupsType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "disable-backups"

    @property
    def description(self):
        return """Disable Backups for an Existing Server"""

    def configure(self, parser):
        """Add arguments for server-action_disable-backups"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=DisableBackupsType,
            required=True,
            description="""None""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: DisableBackupsType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=DisableBackups(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed
