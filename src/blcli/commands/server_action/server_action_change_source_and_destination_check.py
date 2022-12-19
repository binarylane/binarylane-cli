from ... import cli
from ...client.api.server_action.server_action_change_source_and_destination_check import sync
from ...client.client import Client
from ...client.models.change_source_and_destination_check import ChangeSourceAndDestinationCheck
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-source-and-destination-check"

    @property
    def description(self):
        return """Enable or Disable Network Source and Destination Checks for a Server in a VPC"""

    def configure(self, parser):
        """Add arguments for server-action_change-source-and-destination-check"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeSourceAndDestinationCheckType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled",
            dest="enabled",
            type=bool,
            required=True,
            description="""None""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeSourceAndDestinationCheckType,
        enabled: bool,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=ChangeSourceAndDestinationCheck(
                type=type,
                enabled=enabled,
            ),
        )
