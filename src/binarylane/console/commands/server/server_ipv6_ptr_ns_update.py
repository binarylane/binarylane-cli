from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple, Union

from binarylane.api.server.server_ipv6_ptr_ns_update import sync_detailed
from binarylane.client import Client
from binarylane.models.action import Action
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.reverse_nameservers_request import ReverseNameserversRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return """Create New or Update Existing IPv6 Name Server Records"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_ipv6-ptr-ns_update"""

        parser.cli_argument(
            "--reverse-nameservers",
            Union[Unset, None, List[str]],
            dest="reverse_nameservers",
            required=False,
            description="""A list of all IPv6 reverse name servers for this server. Any existing reverse name servers that are omitted from the list will be removed from the server.""",
        )

    @property
    def ok_response_type(self) -> type:
        return Action

    def request(
        self,
        client: Client,
        reverse_nameservers: Union[Unset, None, List[str]] = UNSET,
    ) -> Tuple[HTTPStatus, Union[Action, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: Action
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=ReverseNameserversRequest(
                reverse_nameservers=reverse_nameservers,
            ),
        )
        return page_response.status_code, page_response.parsed
