from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.reverse_names.post_v2_reverse_names_ipv6 import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.reverse_nameservers_request import ReverseNameserversRequest
from binarylane.models.validation_problem_details import ValidationProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    json_body: ReverseNameserversRequest

    def __init__(self, json_body: ReverseNameserversRequest) -> None:
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "update"

    @property
    def description(self) -> str:
        return """Create New or Update Existing IPv6 Name Server Records"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ReverseNames/paths/~1v2~1reverse_names~1ipv6/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        json_body = mapping.add_json_body(ReverseNameserversRequest)

        json_body.add_primitive(
            "reverse_nameservers",
            List[str],
            option_name="reverse-nameservers",
            required=True,
            description="""A list of all IPv6 reverse name servers for this server. Any existing reverse name servers that are omitted from the list will be removed from the server.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
