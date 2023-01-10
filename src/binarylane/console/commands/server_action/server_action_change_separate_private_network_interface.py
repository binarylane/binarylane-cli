from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_separate_private_network_interface import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_separate_private_network_interface import ChangeSeparatePrivateNetworkInterface
from binarylane.models.change_separate_private_network_interface_type import ChangeSeparatePrivateNetworkInterfaceType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.runners import ActionRunner


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
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeSeparatePrivateNetworkInterfaceType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled",
            bool,
            dest="enabled",
            required=True,
            description="""The desired enabled status of the separate second network interface.""",
            action=BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

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
