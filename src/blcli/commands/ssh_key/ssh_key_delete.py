from typing import Any, Union

from ...client.api.ssh_key.ssh_key_delete import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "ssh-key_delete"

    @property
    def description(self):
        return """Delete an Existing SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_delete"""
        parser.cli_argument(
            "key_id",
        )

    def request(
        self,
        key_id: str,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        return sync_detailed(
            key_id=key_id,
            client=client,
        ).parsed
