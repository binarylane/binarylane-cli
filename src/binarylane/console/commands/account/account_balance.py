from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.account.account_balance import sync_detailed
from binarylane.client import Client
from binarylane.models.balance import Balance

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "balance"

    @property
    def description(self):
        return """Fetch Current Balance Information"""

    def configure(self, parser):
        """Add arguments for account_balance"""

    @property
    def ok_response_type(self) -> Type:
        return Balance

    def request(
        self,
        client: Client,
    ) -> Union[Any, Balance]:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
