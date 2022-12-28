from typing import Any, Union

from ...client.api.image.image_get import sync_detailed
from ...client.client import Client
from ...client.models.image_response import ImageResponse
from ...client.models.problem_details import ProblemDetails
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "image_get"

    @property
    def description(self):
        return """Fetch an Existing Image"""

    def configure(self, parser):
        """Add arguments for image_get"""
        parser.cli_argument(
            "image_id_or_slug",
        )

    def request(
        self,
        image_id_or_slug: str,
        client: Client,
    ) -> Union[Any, ImageResponse, ProblemDetails]:

        return sync_detailed(
            image_id_or_slug=image_id_or_slug,
            client=client,
        ).parsed
