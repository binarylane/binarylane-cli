from typing import Any, Union

from ...client.api.account.account_balance import sync_detailed
from ...client.client import Client
from ...client.models.balance import Balance
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "account_balance"

    @property
    def description(self):
        return """Fetch Current Balance Information"""

    def configure(self, parser):
        """Add arguments for account_balance"""

    def request(
        self,
        client: Client,
    ) -> Union[Any, Balance]:

        return sync_detailed(
            client=client,
        ).parsed
