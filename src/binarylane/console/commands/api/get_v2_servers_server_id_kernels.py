from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple, Union

from binarylane.api.servers.get_v2_servers_server_id_kernels import sync_detailed
from binarylane.models.kernels_response import KernelsResponse
from binarylane.models.links import Links
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.list import ListRunner


class CommandRequest:
    server_id: int

    def __init__(self, server_id: int) -> None:
        self.server_id = server_id


class Command(ListRunner):
    def response(self, status_code: int, received: Any) -> None:
        if not isinstance(received, KernelsResponse):
            return super().response(status_code, received)

        return self._printer.print(received, self._format)

    @property
    def default_format(self) -> List[str]:
        return [
            "id",
            "name",
            "version",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this kernel.""",
            "name": """This name of this kernel.""",
            "version": """The version (if any) of this kernel.""",
        }

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Servers/paths/~1v2~1servers~1%7Bserver_id%7D~1kernels/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def lookup_server_id(ref: str) -> Union[None, int]:
            return api_get_v2_servers.Command(self._context).lookup(ref)

        mapping.add(
            PrimitiveAttribute(
                "server_id",
                int,
                required=True,
                option_name=None,
                metavar="server",
                description="""The ID or name of the server for which kernels should be listed.""",
                lookup=lookup_server_id,
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return KernelsResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, KernelsResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: KernelsResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page = 0
        per_page = 25
        has_next = True
        response: Optional[KernelsResponse] = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=request.server_id,
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                return status_code, page_response.parsed

            assert isinstance(page_response.parsed, KernelsResponse)
            has_next = isinstance(page_response.parsed.links, Links) and isinstance(
                page_response.parsed.links.pages.next_, str
            )
            if not response:
                response = page_response.parsed
            else:
                response.kernels += page_response.parsed.kernels

        return status_code, response
