from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.domains.get_v2_domains_domain_name import sync_detailed
from binarylane.models.domain_response import DomainResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    domain_name: str

    def __init__(self, domain_name: str) -> None:
        self.domain_name = domain_name


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing Domain"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Domains/paths/~1v2~1domains~1%7Bdomain_name%7D/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "domain_name",
            str,
            required=True,
            option_name=None,
            description="""The name of the domain to fetch.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return DomainResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, DomainResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: DomainResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            domain_name=request.domain_name,
            client=client,
        )
        return page_response.status_code, page_response.parsed
