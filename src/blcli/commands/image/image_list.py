from typing import Any, Union

from ...client.api.image.image_list import sync_detailed
from ...client.client import Client
from ...client.models.image_query_type import ImageQueryType
from ...client.models.images_response import ImagesResponse
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "image_list"

    @property
    def description(self):
        return """List All Images"""

    def configure(self, parser):
        """Add arguments for image_list"""

        parser.cli_argument(
            "--type",
            dest="type",
            type=Union[Unset, None, ImageQueryType],
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| distribution | Base operating system images. |
| application | Operating system images that include pre-installed applications. This option is not currently supported, operating system images with pre-installed applications are listed under 'distribution'. |
| backup | A backup image of a server. |

""",
        )
        parser.cli_argument(
            "--private",
            dest="private",
            type=Union[Unset, None, bool],
            required=False,
            description="""None""",
        )
        parser.cli_argument(
            "--tag-name",
            dest="tag_name",
            type=Union[Unset, None, str],
            required=False,
            description="""None""",
        )

    def request(
        self,
        client: Client,
        type: Union[Unset, None, ImageQueryType] = UNSET,
        private: Union[Unset, None, bool] = UNSET,
        tag_name: Union[Unset, None, str] = UNSET,
    ) -> Union[Any, ImagesResponse, ValidationProblemDetails]:

        page = 0
        per_page = 25
        has_next = True
        response: ImagesResponse = None

        while has_next:
            page += 1
            page_response = sync_detailed(
                client=client,
                type=type,
                private=private,
                tag_name=tag_name,
                page=page,
                per_page=per_page,
            )

            if page_response.status_code != 200:
                return page_response.parsed

            has_next = page_response.parsed.links and page_response.parsed.links.pages.next_
            if not response:
                response = page_response.parsed
            else:
                response.images += page_response.parsed.images

        return response
