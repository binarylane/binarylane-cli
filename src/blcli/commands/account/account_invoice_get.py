from ...client.api.account.account_invoice_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "account_invoice_get"

    @property
    def description(self):
        return """Fetch an Invoice"""

    def configure(self, parser):
        """Add arguments for account_invoice_get"""
        parser.cli_argument(
            "invoice_id",
        )

    def request(
        self,
        invoice_id: int,
        client: Client,
    ):
        return sync(
            invoice_id=invoice_id,
            client=client,
        )
