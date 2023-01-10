from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server.server_get import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.server_response import ServerResponse

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Existing Server"""

    def configure(self, parser):
        """Add arguments for server_get"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server to fetch.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ServerResponse

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, ServerResponse]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
