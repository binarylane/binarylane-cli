from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server.server_user_data import sync_detailed
from binarylane.client import Client
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.user_data import UserData

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "user-data"

    @property
    def description(self):
        return """Fetch the Currently Set UserData for a Server"""

    def configure(self, parser):
        """Add arguments for server_user-data"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server for which userdata should be fetched.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return UserData

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, ProblemDetails, UserData]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
