from ...client.api.domain.domain_record_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_record_get"

    @property
    def description(self):
        return """Fetch an Existing Domain Record"""

    def configure(self, parser):
        """Add arguments for domain_record_get"""
        parser.cli_argument(
            "domain_name",
        )
        parser.cli_argument(
            "record_id",
        )

    def request(
        self,
        domain_name: str,
        record_id: int,
        client: Client,
    ):
        return sync(
            domain_name=domain_name,
            record_id=record_id,
            client=client,
        )
