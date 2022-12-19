from typing import Union

from ... import cli
from ...client.api.ssh_key.ssh_key_update import sync
from ...client.client import Client
from ...client.models.update_ssh_key_request import UpdateSshKeyRequest
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "ssh-key_update"

    @property
    def description(self):
        return """Update an Existing SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_update"""
        parser.cli_argument(
            "key_id",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=str,
            required=True,
            description="""A name to help you identify the key.""",
        )

        parser.cli_argument(
            "--default",
            dest="default",
            type=Union[Unset, None, bool],
            required=False,
            description="""Do not provide or leave null to leave the default status of the key unchanged.
Optional: If true this will be added to all new server installations (if we support SSH Key injection for the server's operating system).""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        key_id: str,
        client: Client,
        name: str,
        default: Union[Unset, None, bool] = UNSET,
    ):
        return sync(
            key_id=key_id,
            client=client,
            json_body=UpdateSshKeyRequest(
                name=name,
                default=default,
            ),
        )
