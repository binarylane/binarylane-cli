from typing import Any, Union

from ...client.api.ssh_key.ssh_key_delete import sync_detailed
from ...client.client import Client
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

    @property
    def description(self):
        return """Delete an Existing SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_delete"""
        parser.cli_argument(
            "key_id",
            type=str,
            description="""The ID or fingerprint of the SSH Key to delete.""",
        )

    def request(
        self,
        key_id: str,
        client: Client,
    ) -> Union[Any, ProblemDetails]:

        page_response = sync_detailed(
            key_id=key_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
