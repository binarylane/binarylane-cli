from ...client.api.ssh_key.ssh_key_get import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "ssh-key_get"

    @property
    def description(self):
        return """Fetch an Existing SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_get"""
        parser.cli_argument(
            "key_id",
        )

    def request(
        self,
        key_id: str,
        client: Client,
    ):
        return sync(
            key_id=key_id,
            client=client,
        )
