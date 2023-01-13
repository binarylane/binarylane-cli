from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_user_data import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.user_data import UserData

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "user-data"

    @property
    def description(self) -> str:
        return """Fetch the Currently Set UserData for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_user-data"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server for which userdata should be fetched.""",
        )

    @property
    def ok_response_type(self) -> type:
        return UserData

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ProblemDetails, UserData]]:

        # HTTPStatus.OK: UserData
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
