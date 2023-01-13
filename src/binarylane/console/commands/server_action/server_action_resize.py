from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.server_action.server_action_resize import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_image import ChangeImage
from binarylane.models.change_licenses import ChangeLicenses
from binarylane.models.change_size_options_request import ChangeSizeOptionsRequest
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.resize import Resize
from binarylane.models.resize_type import ResizeType
from binarylane.models.take_backup import TakeBackup
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "resize"

    @property
    def description(self) -> str:
        return """Update the Size and Related Options for a Server"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for server-action_resize"""
        parser.cli_argument(
            "server_id",
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ResizeType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--size",
            Union[Unset, None, str],
            dest="size",
            required=False,
            description="""The slug of the selected size. Do not provide to keep the current size.""",
        )

        parser.cli_argument(
            "--options",
            Union[Unset, None, ChangeSizeOptionsRequest],
            dest="options",
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--change-image",
            Union[Unset, None, ChangeImage],
            dest="change_image",
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--change-licenses",
            Union[Unset, None, ChangeLicenses],
            dest="change_licenses",
            required=False,
            description="""""",
        )

        parser.cli_argument(
            "--pre-action-backup",
            Union[Unset, None, TakeBackup],
            dest="pre_action_backup",
            required=False,
            description="""Take a Backup of a Server""",
        )

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

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
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
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
        )
        return page_response.status_code, page_response.parsed
