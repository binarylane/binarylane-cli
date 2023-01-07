from typing import Any, Union

from ...client.api.server_action.server_action_enable_backups import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.enable_backups import EnableBackups
from ...client.models.enable_backups_type import EnableBackupsType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "enable-backups"

    @property
    def description(self):
        return """Enable Two Daily Backups for an Existing Server"""

    def configure(self, parser):
        """Add arguments for server-action_enable-backups"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=EnableBackupsType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: EnableBackupsType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=EnableBackups(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed
