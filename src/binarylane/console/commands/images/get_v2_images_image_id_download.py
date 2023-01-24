from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, Tuple, Union

from binarylane.api.images.get_v2_images_image_id_download import sync_detailed
from binarylane.models.image_download_response import ImageDownloadResponse
from binarylane.models.problem_details import ProblemDetails

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping
from binarylane.console.runners.command import CommandRunner


class CommandRequest:
    image_id: int

    def __init__(self, image_id: int) -> None:
        self.image_id = image_id


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "download"

    @property
    def description(self) -> str:
        return """Download an Existing Image"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/Images/paths/~1v2~1images~1%7Bimage_id%7D~1download/get"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "image_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the image to download.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ImageDownloadResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[None, ImageDownloadResponse, ProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ImageDownloadResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            image_id=request.image_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
