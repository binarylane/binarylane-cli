from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_rebuild import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.image_options import ImageOptions
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.rebuild import Rebuild
from binarylane.models.rebuild_type import RebuildType
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
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
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            RebuildType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--image",
            Union[None, Unset, int, str],
            dest="image",
            required=False,
            description="""The Operating System ID or slug or Backup image ID to use as a base for the rebuild.""",
        )

        parser.cli_argument(
            "--options",
            Union[Unset, None, ImageOptions],
            dest="options",
            required=False,
            description="""""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: RebuildType,
        image: Union[None, Unset, int, str] = UNSET,
        options: Union[Unset, None, ImageOptions] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Rebuild(
                type=type,
                image=image,
                options=options,
            ),
        )
        return page_response.status_code, page_response.parsed
