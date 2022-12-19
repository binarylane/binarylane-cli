from typing import Union

from ... import cli
from ...client.api.image.image_update import sync
from ...client.client import Client
from ...client.models.image_request import ImageRequest
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


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
    ):
        return sync(
            image_id=image_id,
            client=client,
            json_body=ImageRequest(
                name=name,
                locked=locked,
            ),
        )
