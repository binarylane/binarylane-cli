from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.account.account_get import sync_detailed
from binarylane.client import Client
from binarylane.models.account_response import AccountResponse

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch Information About the Current Account"""

    def configure(self, parser):
        """Add arguments for account_get"""

    @property
    def ok_response_type(self) -> Type:
        return AccountResponse

    def request(
        self,
        client: Client,
    ) -> Union[AccountResponse, Any]:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed