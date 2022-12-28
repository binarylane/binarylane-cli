from typing import Union

from ...client.api.server.server_tagged_delete import sync
from ...client.client import Client
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_tagged_delete"

    @property
    def description(self):
        return """Cancel Existing Servers by Tag"""

    def configure(self, parser):
        """Add arguments for server_tagged_delete"""

        parser.cli_argument(
            "--tag-name",
            dest="tag_name",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

    def request(
        self,
        client: Client,
        tag_name: Union[Unset, None, str] = UNSET,
    ):
        return sync(
            client=client,
            tag_name=tag_name,
        )
