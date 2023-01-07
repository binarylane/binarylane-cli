from typing import Any, Union

from ...client.api.server_action.server_action_change_partner import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_partner import ChangePartner
from ...client.models.change_partner_type import ChangePartnerType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-partner"

    @property
    def description(self):
        return """Add, Update or Remove a Partner Server for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-partner"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
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
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangePartner(
                type=type,
                partner_server_id=partner_server_id,
            ),
        )
        return page_response.status_code, page_response.parsed
