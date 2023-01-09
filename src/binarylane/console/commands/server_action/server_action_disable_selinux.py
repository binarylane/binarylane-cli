from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_disable_selinux import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.disable_selinux import DisableSelinux
from binarylane.models.disable_selinux_type import DisableSelinuxType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "disable-selinux"

    @property
    def description(self):
        return """Disable SE Linux for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_disable-selinux"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=DisableSelinuxType,
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
        type: DisableSelinuxType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=DisableSelinux(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed
