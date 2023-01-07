from typing import Any, Union

from ...client.api.server_action.server_action_enable_ipv6 import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.enable_ipv_6 import EnableIpv6
from ...client.models.enable_ipv_6_type import EnableIpv6Type
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "enable-ipv6"

    @property
    def description(self):
        return """Enable IPv6 for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_enable-ipv6"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=EnableIpv6Type,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: EnableIpv6Type,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=EnableIpv6(
                type=type,
            ),
        )
        return page_response.status_code, page_response.parsed
