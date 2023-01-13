from __future__ import annotations

from http import HTTPStatus
from typing import Tuple, Union

from binarylane.api.image.image_download import sync_detailed
from binarylane.client import Client
from binarylane.models.image_download_response import ImageDownloadResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.parsers import CommandParser
from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self) -> str:
        return "download"

    @property
    def description(self) -> str:
        return """Download an Existing Image"""

    def configure(self, parser: CommandParser) -> None:
        """Add arguments for image_download"""
        parser.cli_argument(
            "image_id",
            int,
            description="""The ID of the image to download.""",
        )

    @property
    def ok_response_type(self) -> type:
        return ImageDownloadResponse

    def request(
        self,
        image_id: int,
        client: Client,
    ) -> Tuple[HTTPStatus, Union[None, ImageDownloadResponse, ProblemDetails]]:

        # HTTPStatus.OK: ImageDownloadResponse
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            image_id=image_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
