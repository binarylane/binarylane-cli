from typing import Any, Union

from ...client.api.account.account_get import sync_detailed
from ...client.client import Client
from ...client.models.account_response import AccountResponse
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch Information About the Current Account"""

    def configure(self, parser):
        """Add arguments for account_get"""

    def request(
        self,
        client: Client,
    ) -> Union[AccountResponse, Any]:

        page_response = sync_detailed(
            client=client,
        )
        return page_response.status_code, page_response.parsed
