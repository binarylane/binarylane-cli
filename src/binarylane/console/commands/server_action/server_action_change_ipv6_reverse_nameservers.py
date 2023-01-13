from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.server_action.server_action_change_ipv6_reverse_nameservers import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_ipv_6_reverse_nameservers import ChangeIpv6ReverseNameservers
from binarylane.models.change_ipv_6_reverse_nameservers_type import ChangeIpv6ReverseNameserversType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-ipv6-reverse-nameservers"

    @property
    def description(self) -> str:
        return """Update the IPv6 Reverse Name Servers for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_change-ipv6-reverse-nameservers"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeIpv6ReverseNameserversType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--ipv6-reverse-nameservers",
            List[str],
            dest="ipv6_reverse_nameservers",
            required=True,
            description="""A list of all IPv6 reverse name servers for this server. Any existing reverse name servers that are omitted from the list will be removed from the server.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeIpv6ReverseNameserversType,
        ipv6_reverse_nameservers: List[str],
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeIpv6ReverseNameservers(
                type=type,
                ipv6_reverse_nameservers=ipv6_reverse_nameservers,
            ),
        )
        return page_response.status_code, page_response.parsed
