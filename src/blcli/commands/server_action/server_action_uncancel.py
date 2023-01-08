from typing import Any, Type, Union

from ...client.api.server_action.server_action_uncancel import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.uncancel import Uncancel
from ...client.models.uncancel_type import UncancelType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "uncancel"

    @property
    def description(self):
        return """Revert the Cancellation of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_uncancel"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=UncancelType,
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
        type: UncancelType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Uncancel(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed
