from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.image.image_update import sync_detailed
from binarylane.client import Client
from binarylane.models.image_request import ImageRequest
from binarylane.models.image_response import ImageResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import UNSET, Unset

from binarylane.console.actions import BooleanOptionalAction
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "update"

    @property
    def description(self):
        return """Update an Existing Image"""

    def configure(self, parser):
        """Add arguments for image_update"""
        parser.cli_argument(
            "image_id",
            int,
            description="""The ID of the image to update.""",
        )

        parser.cli_argument(
            "--name",
            Union[Unset, None, str],
            dest="name",
            required=False,
            description="""Optional: a new display name for this image. Do not provide to leave the display name unchanged, submit an empty string to clear the display name.""",
        )

        parser.cli_argument(
            "--locked",
            Union[Unset, None, bool],
            dest="locked",
            required=False,
            description="""Optional: you may choose to lock an individual backup in which case we will not update that backup until you unlock it. Do not provide to leave the locked status unchanged.""",
            action=BooleanOptionalAction,
        )

    @property
    def ok_response_type(self) -> Type:
        return ImageResponse

    def request(
        self,
        image_id: int,
        client: Client,
        name: Union[Unset, None, str] = UNSET,
        locked: Union[Unset, None, bool] = UNSET,
    ) -> Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            image_id=image_id,
            client=client,
            json_body=ImageRequest(
                name=name,
                locked=locked,
            ),
        )
        return page_response.status_code, page_response.parsed
