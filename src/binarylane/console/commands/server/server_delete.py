from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_delete import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return """Cancel an Existing Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_delete"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server to be cancelled.""",
        )

        parser.cli_argument(
            "--reason",
            Union[Unset, None, str],
            dest="reason",
            required=False,
            description="""The reason for cancelling the server.""",
        )

    @property
    def ok_response_type(self) -> type:
        return type(None)

    def request(
        self,
        server_id: int,
        client: Client,
        reason: Union[Unset, None, str] = UNSET,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails]]:

        # HTTPStatus.NO_CONTENT: Any
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            reason=reason,
        )
        return page_response.status_code, page_response.parsed
