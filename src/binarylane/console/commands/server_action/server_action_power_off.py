from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_power_off import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.power_off import PowerOff
from binarylane.models.power_off_type import PowerOffType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "power-off"

    @property
    def description(self):
        return """Power a Server Off"""

    def configure(self, parser):
        """Add arguments for server-action_power-off"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            PowerOffType,
            dest="type",
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
        type: PowerOffType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=PowerOff(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed
