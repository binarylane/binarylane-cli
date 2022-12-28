from typing import Any, Union

from ... import cli
from ...client.api.image.image_update import sync_detailed
from ...client.client import Client
from ...client.models.image_request import ImageRequest
from ...client.models.image_response import ImageResponse
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "image_update"

    @property
    def description(self):
        return """Update an Existing Image"""

    def configure(self, parser):
        """Add arguments for image_update"""
        parser.cli_argument(
            "image_id",
        )

        parser.cli_argument(
            "--name",
            dest="name",
            type=Union[Unset, None, str],
            required=False,
            description="""Optional: a new display name for this image. Do not provide to leave the display name unchanged, submit an empty string to clear the display name.""",
        )

        parser.cli_argument(
            "--locked",
            dest="locked",
            type=Union[Unset, None, bool],
            required=False,
            description="""Optional: you may choose to lock an individual backup in which case we will not update that backup until you unlock it. Do not provide to leave the locked status unchanged.""",
            action=cli.BooleanOptionalAction,
        )

    def request(
        self,
        image_id: int,
        client: Client,
        name: Union[Unset, None, str] = UNSET,
        locked: Union[Unset, None, bool] = UNSET,
    ) -> Union[Any, ImageResponse, ProblemDetails, ValidationProblemDetails]:

        return sync_detailed(
            image_id=image_id,
            client=client,
            json_body=ImageRequest(
                name=name,
                locked=locked,
            ),
        ).parsed
