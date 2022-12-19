from ...client.api.account.account_invoice_overdue import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "account_invoice_overdue"

    @property
    def description(self):
        return """Fetch Unpaid Failed Invoices"""

    def configure(self, parser):
        """Add arguments for account_invoice_overdue"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
