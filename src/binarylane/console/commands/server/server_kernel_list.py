from __future__ import annotations

from typing import Any, Dict, List, Type, Union

from binarylane.api.server.server_kernel_list import sync_detailed
from binarylane.client import Client
from binarylane.models.kernels_response import KernelsResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "id",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "id": """The ID of this kernel.""",
            "name": """This name of this kernel.""",
            "version": """The version (if any) of this kernel.""",
        }

    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """List all Available Kernels for a Server"""

    def configure(self, parser):
        """Add arguments for server_kernel_list"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server for which kernels should be listed.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return KernelsResponse

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, KernelsResponse, ProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: KernelsResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                server_id=server_id,
                client=client,
                page=page,
                per_page=per_page,
            )

            status_code = page_response.status_code
            if status_code != 200:
                response = page_response.parsed
                break

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.kernels += page_response.parsed.kernels

        return status_code, response
