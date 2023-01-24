from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Optional, Tuple, Union

from binarylane.api.reverse_names.get_v2_reverse_names_ipv6 import sync_detailed
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.reverse_name_servers_response import ReverseNameServersResponse

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    pass


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """Fetch all Existing IPv6 Name Server Records"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ReverseNames/paths/~1v2~1reverse_names~1ipv6/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)
        return mapping

    @property
    def ok_response_type(self) -> type:
        return ReverseNameServersResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, ReverseNameServersResponse]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ReverseNameServersResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[ReverseNameServersResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, ReverseNameServersResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.reverse_nameservers += page_response.parsed.reverse_nameservers

        return status_code, response
