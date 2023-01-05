from typing import Any, Union

from ...client.api.server_action.server_action_resize import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_image import ChangeImage
from ...client.models.change_licenses import ChangeLicenses
from ...client.models.change_size_options_request import ChangeSizeOptionsRequest
from ...client.models.problem_details import ProblemDetails
from ...client.models.resize import Resize
from ...client.models.resize_type import ResizeType
from ...client.models.take_backup import TakeBackup
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "resize"

    @property
    def description(self):
        return """Update the Size and Related Options for a Server"""

    def configure(self, parser):
        """Add arguments for server-action_resize"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ResizeType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--size",
            dest="size",
            type=Union[Unset, None, str],
            required=False,
            description="""The slug of the selected size. Do not provide to keep the current size.""",
        )

        parser.cli_argument(
            "--options",
            dest="options",
            type=Union[Unset, None, ChangeSizeOptionsRequest],
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--change-image",
            dest="change_image",
            type=Union[Unset, None, ChangeImage],
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--change-licenses",
            dest="change_licenses",
            type=Union[Unset, None, ChangeLicenses],
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--pre-action-backup",
            dest="pre_action_backup",
            type=Union[Unset, None, TakeBackup],
            required=False,
            description="""Take a Backup of a Server""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ResizeType,
        size: Union[Unset, None, str] = UNSET,
        options: Union[Unset, None, ChangeSizeOptionsRequest] = UNSET,
        change_image: Union[Unset, None, ChangeImage] = UNSET,
        change_licenses: Union[Unset, None, ChangeLicenses] = UNSET,
        pre_action_backup: Union[Unset, None, TakeBackup] = UNSET,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            server_id=server_id,
            client=client,
            json_body=Resize(
                type=type,
                size=size,
                options=options,
                change_image=change_image,
                change_licenses=change_licenses,
                pre_action_backup=pre_action_backup,
            ),
        ).parsed
