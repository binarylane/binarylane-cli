from __future__ import annotations

from http import HTTPStatus
from typing import Any, Tuple, Union

from binarylane.api.account.account_get import sync_detailed
from binarylane.client import Client
from binarylane.models.account_response import AccountResponse

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch Information About the Current Account"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for account_get"""

    @property
    def ok_response_type(self) -> type:
        return AccountResponse

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, AccountResponse, Any]]:

        # HTTPStatus.OK: AccountResponse
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
