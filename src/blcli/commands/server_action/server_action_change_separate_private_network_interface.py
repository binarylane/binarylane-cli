from typing import Any, Union

from ... import cli
from ...client.api.server_action.server_action_change_separate_private_network_interface import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_separate_private_network_interface import ChangeSeparatePrivateNetworkInterface
from ...client.models.change_separate_private_network_interface_type import ChangeSeparatePrivateNetworkInterfaceType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-separate-private-network-interface"

    @property
    def description(self):
        return """Enable or Disable a Separate Private Network Interface for a Server in a VPC"""

    def configure(self, parser):
        """Add arguments for server-action_change-separate-private-network-interface"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeSeparatePrivateNetworkInterfaceType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled",
            dest="enabled",
            type=bool,
            required=True,
            description="""The desired enabled status of the separate second network interface.""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeSeparatePrivateNetworkInterfaceType,
        enabled: bool,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeSeparatePrivateNetworkInterface(
                type=type,
                enabled=enabled,
            ),
        )
        return page_response.status_code, page_response.parsed
