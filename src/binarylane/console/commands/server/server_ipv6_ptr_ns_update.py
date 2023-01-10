from __future__ import annotations

from typing import Any, List, Type, Union

from binarylane.api.server.server_ipv6_ptr_ns_update import sync_detailed
from binarylane.client import Client
from binarylane.models.action import Action
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.reverse_nameservers_request import ReverseNameserversRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "update"

    @property
    def description(self):
        return """Create New or Update Existing IPv6 Name Server Records"""

    def configure(self, parser):
        """Add arguments for server_ipv6-ptr-ns_update"""

        parser.cli_argument(
            "--reverse-nameservers",
            Union[Unset, None, List[str]],
            dest="reverse_nameservers",
            required=False,
            description="""A list of all IPv6 reverse name servers for this server. Any existing reverse name servers that are omitted from the list will be removed from the server.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return Action

    def request(
        self,
        client: Client,
        reverse_nameservers: Union[Unset, None, List[str]] = UNSET,
    ) -> Union[Action, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            client=client,
            json_body=ReverseNameserversRequest(
                reverse_nameservers=reverse_nameservers,
            ),
        )
        return page_response.status_code, page_response.parsed
