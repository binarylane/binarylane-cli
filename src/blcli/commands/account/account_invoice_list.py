from ...client.api.account.account_invoice_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "account_invoice_list"

    @property
    def description(self):
        return """Fetch Invoices"""

    def configure(self, parser):
        """Add arguments for account_invoice_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
