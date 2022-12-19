from ...client.api.vpc.vpc_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "vpc_get"

    @property
    def description(self):
        return """Fetch an Existing VPC"""

    def configure(self, parser):
        """Add arguments for vpc_get"""
        parser.cli_argument(
            "vpc_id",
            description="""The target vpc id.""",
        )

    def request(
        self,
        vpc_id: int,
        client: Client,
    ):
        return sync(
            vpc_id=vpc_id,
            client=client,
        )
