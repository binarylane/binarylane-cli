from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.image.image_get import sync_detailed
from binarylane.client import Client
from binarylane.models.image_response import ImageResponse
from binarylane.models.problem_details import ProblemDetails

from binarylane.console.runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "get"

    @property
    def description(self):
        return """Fetch an Existing Image"""

    def configure(self, parser):
        """Add arguments for image_get"""
        parser.cli_argument(
            "image_id_or_slug",
            str,
            description="""The ID or Slug (if an operating system) of the image to retrieve.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ImageResponse

    def request(
        self,
        image_id_or_slug: str,
        client: Client,
    ) -> Union[Any, ImageResponse, ProblemDetails]:

        page_response = sync_detailed(
            image_id_or_slug=image_id_or_slug,
            client=client,
        )
        return page_response.status_code, page_response.parsed
