from typing import Any, Union

from ...client.api.server_action.server_action_rebuild import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.image_options import ImageOptions
from ...client.models.problem_details import ProblemDetails
from ...client.models.rebuild import Rebuild
from ...client.models.rebuild_type import RebuildType
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "rebuild"

    @property
    def description(self):
        return """Rebuild an Existing Server"""

    def configure(self, parser):
        """Add arguments for server-action_rebuild"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The target server id.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=RebuildType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--image",
            dest="image",
            type=Union[None, Unset, int, str],
            required=False,
            description="""The Operating System ID or slug or Backup image ID to use as a base for the rebuild.""",
        )

        parser.cli_argument(
            "--options",
            dest="options",
            type=Union[Unset, None, ImageOptions],
            required=False,
            description="""""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: RebuildType,
        image: Union[None, Unset, int, str] = UNSET,
        options: Union[Unset, None, ImageOptions] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Rebuild(
                type=type,
                image=image,
                options=options,
            ),
        ).parsed
