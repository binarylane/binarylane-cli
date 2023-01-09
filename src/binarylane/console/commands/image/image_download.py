from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.image.image_download import sync_detailed
from binarylane.client import Client
from binarylane.models.image_download_response import ImageDownloadResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "download"

    @property
    def description(self):
        return """Download an Existing Image"""

    def configure(self, parser):
        """Add arguments for image_download"""
        parser.cli_argument(
            "image_id",
            type=int,
            description="""The ID of the image to download.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ImageDownloadResponse

    def request(
        self,
        image_id: int,
        client: Client,
    ) -> Union[Any, ImageDownloadResponse, ProblemDetails]:

        page_response = sync_detailed(
            image_id=image_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
