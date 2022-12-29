from typing import Any, Dict, List, Union

from ...client.api.account.account_balance import sync_detailed
from ...client.client import Client
from ...client.models.balance import Balance
from ...runners import ListRunner


class Command(ListRunner):
    @property
    def default_format(self) -> List[str]:
        return [
            "created",
            "description",
            "total",
            "ongoing",
        ]

    @property
    def fields(self) -> Dict[str, str]:
        return {
            "created": """The time when the charge was created.""",
            "description": """A summary of the charge.""",
            "total": """The cost in AU$.""",
            "ongoing": """If this is true the charge is for an ongoing service. If this is false the charge is complete and awaiting invoicing.""",
        }

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
