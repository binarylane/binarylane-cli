from typing import Any, Union

from ...client.api.server_action.server_action_disable_selinux import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.disable_selinux import DisableSelinux
from ...client.models.disable_selinux_type import DisableSelinuxType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_disable-selinux"

    @property
    def description(self):
        return """Disable SE Linux for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_disable-selinux"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=DisableSelinuxType,
            required=True,
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: DisableSelinuxType,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=DisableSelinux(
                type=type,
            ),
        ).parsed
