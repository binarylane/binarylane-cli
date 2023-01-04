from typing import Any, Union

from ...client.api.server.server_tagged_delete import sync_detailed
from ...client.client import Client
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "delete"

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
    ) -> Any:

        return sync_detailed(
            client=client,
            tag_name=tag_name,
        ).parsed
