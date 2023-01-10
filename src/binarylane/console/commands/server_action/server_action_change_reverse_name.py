from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_reverse_name import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_reverse_name import ChangeReverseName
from binarylane.models.change_reverse_name_type import ChangeReverseNameType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-reverse-name"

    @property
    def description(self):
        return """Change the Reverse Name for an IPv4 Address on a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-reverse-name"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeReverseNameType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--ipv4-address",
            str,
            dest="ipv4_address",
            required=True,
            description="""The IPv4 address to set or clear the reverse name for.""",
        )

        parser.cli_argument(
            "--reverse-name",
            Union[Unset, None, str],
            dest="reverse_name",
            required=False,
            description="""Leave this null to clear the custom reverse name.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeReverseNameType,
        ipv4_address: str,
        reverse_name: Union[Unset, None, str] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeReverseName(
                type=type,
                ipv4_address=ipv4_address,
                reverse_name=reverse_name,
            ),
        )
        return page_response.status_code, page_response.parsed
