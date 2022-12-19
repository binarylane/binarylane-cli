from ...client.api.ssh_key.ssh_key_list import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "ssh-key_list"

    @property
    def description(self):
        return """List All SSH Keys"""

    def configure(self, parser):
        """Add arguments for ssh-key_list"""

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
