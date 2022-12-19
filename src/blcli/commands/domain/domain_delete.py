from ...client.api.domain.domain_delete import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_delete"

    @property
    def description(self):
        return """Delete an Existing Domain"""

    def configure(self, parser):
        """Add arguments for domain_delete"""
        parser.cli_argument(
            "domain_name",
        )

    def request(
        self,
        domain_name: str,
        client: Client,
    ):
        return sync(
            domain_name=domain_name,
            client=client,
        )
