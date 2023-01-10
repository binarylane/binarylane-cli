from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_ipv6 import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_ipv_6 import ChangeIpv6
from binarylane.models.change_ipv_6_type import ChangeIpv6Type
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-ipv6"

    @property
    def description(self):
        return """Enable or Disable IPv6 for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-ipv6"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeIpv6Type,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--enabled",
            bool,
            dest="enabled",
            required=True,
            description="""The desired enabled status of IPv6.""",
            action=BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeIpv6Type,
        enabled: bool,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeIpv6(
                type=type,
                enabled=enabled,
            ),
        )
        return page_response.status_code, page_response.parsed
