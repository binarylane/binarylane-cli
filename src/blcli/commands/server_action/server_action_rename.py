from typing import Any, Type, Union

from ...client.api.server_action.server_action_rename import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.rename import Rename
from ...client.models.rename_type import RenameType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "rename"

    @property
    def description(self):
        return """Rename a Server"""

    def configure(self, parser):
        """Add arguments for server-action_rename"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
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
            description="""The new hostname of your server, such as vps01.yourcompany.com.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: RenameType,
        name: str,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Rename(
                type=type,
                name=name,
            ),
        )
        return page_response.status_code, page_response.parsed
