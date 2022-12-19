from ...client.api.domain.domain_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_get"

    @property
    def description(self):
        return """Fetch an Existing Domain"""

    def configure(self, parser):
        """Add arguments for domain_get"""
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
