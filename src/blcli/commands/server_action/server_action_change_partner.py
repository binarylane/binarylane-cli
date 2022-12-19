from typing import Union

from ...client.api.server_action.server_action_change_partner import sync
from ...client.client import Client
from ...client.models.change_partner import ChangePartner
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-partner"

    @property
    def description(self):
        return """Add, Update or Remove a Partner Server for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-partner"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangePartnerType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--partner-server-id",
            dest="partner_server_id",
            type=Union[Unset, None, int],
            required=False,
            description="""Leave this null to remove the server partnership. The partner server must be in the same region as the target server.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangePartnerType,
        partner_server_id: Union[Unset, None, int] = UNSET,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=ChangePartner(
                type=type,
                partner_server_id=partner_server_id,
            ),
        )
