from typing import Any, Union

from ...client.api.server_action.server_action_restore import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.restore import Restore
from ...client.models.restore_type import RestoreType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_restore"

    @property
    def description(self):
        return """Restore a Backup to a Server"""

    def configure(self, parser):
        """Add arguments for server-action_restore"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=RestoreType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--image",
            dest="image",
            type=Union[int, str],
            required=True,
            description="""The ID of the specific backup to use. Snapshots are not currently supported.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: RestoreType,
        image: Union[int, str],
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Restore(
                type=type,
                image=image,
            ),
        ).parsed
