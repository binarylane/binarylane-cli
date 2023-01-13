from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server.server_neighbors_list import sync_detailed
from binarylane.client import Client
from binarylane.models.neighbors_response import NeighborsResponse

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All Servers That Share a Host"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server_neighbors_list"""

    @property
    def ok_response_type(self) -> type:
        return NeighborsResponse

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, NeighborsResponse]]:

        # HTTPStatus.OK: NeighborsResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
