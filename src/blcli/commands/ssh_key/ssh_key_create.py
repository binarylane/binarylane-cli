from typing import Union

from ... import cli
from ...client.api.ssh_key.ssh_key_create import sync
from ...client.client import Client
from ...client.models.ssh_key_request import SshKeyRequest
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "ssh-key_create"

    @property
    def description(self):
        return """Add a New SSH Key"""

    def configure(self, parser):
        """Add arguments for ssh-key_create"""

        parser.cli_argument(
            "--public-key",
            dest="public_key",
            type=str,
            required=True,
            description="""The public key in OpenSSH "authorized_keys" format.""",
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
            description="""Optional: If true this will be added to all new server installations (if we support SSH Key injection for the server's operating system).""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        client: Client,
        public_key: str,
        name: str,
        default: Union[Unset, None, bool] = UNSET,
    ):
        return sync(
            client=client,
            json_body=SshKeyRequest(
                public_key=public_key,
                name=name,
                default=default,
            ),
        )
