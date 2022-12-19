from ...client.api.domain.domain_record_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_record_list"

    @property
    def description(self):
        return """List All Domain Records for a Domain"""

    def configure(self, parser):
        """Add arguments for domain_record_list"""
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
