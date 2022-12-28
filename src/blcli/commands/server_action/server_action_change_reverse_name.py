from typing import Any, Union

from ...client.api.server_action.server_action_change_reverse_name import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_reverse_name import ChangeReverseName
from ...client.models.change_reverse_name_type import ChangeReverseNameType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-reverse-name"

    @property
    def description(self):
        return """Change the Reverse Name for an IPv4 Address on a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-reverse-name"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeReverseNameType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--ipv4-address",
            dest="ipv4_address",
            type=str,
            required=True,
            description="""The IPv4 address to set or clear the reverse name for.""",
        )

        parser.cli_argument(
            "--reverse-name",
            dest="reverse_name",
            type=Union[Unset, None, str],
            required=False,
            description="""Leave this null to clear the custom reverse name.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeReverseNameType,
        ipv4_address: str,
        reverse_name: Union[Unset, None, str] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeReverseName(
                type=type,
                ipv4_address=ipv4_address,
                reverse_name=reverse_name,
            ),
        ).parsed
