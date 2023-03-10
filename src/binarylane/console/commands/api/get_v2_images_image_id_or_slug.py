from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.images.get_v2_images_image_id_or_slug import sync_detailed
from binarylane.models.image_response import ImageResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    image_id_or_slug: str

    def __init__(self, image_id_or_slug: str) -> None:
        self.image_id_or_slug = image_id_or_slug


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return """Fetch an Existing Image"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Images/paths/~1v2~1images~1%7Bimage_id_or_slug%7D/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "image_id_or_slug",
            str,
            required=True,
            option_name=None,
            description="""The ID or Slug (if an operating system) of the image to retrieve.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ImageResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ImageResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ImageResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            image_id_or_slug=request.image_id_or_slug,
            client=client,
        )
        return page_response.status_code, page_response.parsed
