from typing import Any, Union

from ...client.api.server_action.server_action_rename import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.rename import Rename
from ...client.models.rename_type import RenameType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_rename"

    @property
    def description(self):
        return """Rename a Server"""

    def configure(self, parser):
        """Add arguments for server-action_rename"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=RenameType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=str,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: RenameType,
        name: str,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Rename(
                type=type,
                name=name,
            ),
        ).parsed
