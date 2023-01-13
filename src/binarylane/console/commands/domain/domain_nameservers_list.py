from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.domain.domain_nameservers_list import sync_detailed
from binarylane.client import Client
from binarylane.models.local_nameservers_response import LocalNameserversResponse

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return """List All Public Nameservers"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for domain_nameservers_list"""

    @property
    def ok_response_type(self) -> type:
        return LocalNameserversResponse

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, LocalNameserversResponse]]:

        # HTTPStatus.OK: LocalNameserversResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
