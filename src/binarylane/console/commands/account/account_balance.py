from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.account.account_balance import sync_detailed
from binarylane.client import Client
from binarylane.models.balance import Balance

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "balance"

    @property
    def description(self) -> str:
        return """Fetch Current Balance Information"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for account_balance"""

    @property
    def ok_response_type(self) -> type:
        return Balance

    def request(
        self,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, Balance]]:

        # HTTPStatus.OK: Balance
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
