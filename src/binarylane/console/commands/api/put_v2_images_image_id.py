from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.images.put_v2_images_image_id import sync_detailed
from binarylane.models.image_request import ImageRequest
from binarylane.models.image_response import ImageResponse
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    image_id: int
    json_body: ImageRequest

    def __init__(self, image_id: int, json_body: ImageRequest) -> None:
        self.image_id = image_id
        self.json_body = json_body


class Command(CommandRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Images/paths/~1v2~1images~1%7Bimage_id%7D/put"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add(
            PrimitiveAttribute(
                "image_id",
                int,
                required=True,
                option_name=None,
                description="""The ID of the image to update.""",
            )
        )

        json_body = mapping.add_json_body(ImageRequest)

        json_body.add(
            PrimitiveAttribute(
                "name",
                Union[Unset, None, str],
                required=False,
                option_name="name",
                description="""Optional: a new display name for this image. Do not provide to leave the display name unchanged, submit an empty string to clear the display name.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "locked",
                Union[Unset, None, bool],
                required=False,
                option_name="locked",
                description="""Optional: you may choose to lock an individual backup in which case we will not update that backup until you unlock it. Do not provide to leave the locked status unchanged. You may not lock or unlock a temporary backup or a backup that is attached to a server.""",
            )
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ImageResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ImageResponse, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ImageResponse
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            image_id=request.image_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
