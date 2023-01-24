from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.domains.post_v2_domains import sync_detailed
from binarylane.models.domain_request import DomainRequest
from binarylane.models.domain_response import DomainResponse
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    json_body: DomainRequest

    def __init__(self, json_body: DomainRequest) -> None:
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return """Create a New Domain"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Domains/paths/~1v2~1domains/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        json_body = mapping.add_json_body(DomainRequest)

        json_body.add_primitive(
            "name",
            str,
            option_name="name",
            required=True,
            description="""The domain name to add to the DNS management system.""",
        )

        json_body.add_primitive(
            "ip_address",
            Union[Unset, None, str],
            option_name="ip-address",
            required=False,
            description="""An optional IPv4 address that will be used to create an A record for the root domain.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return DomainResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, DomainResponse, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: DomainResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
