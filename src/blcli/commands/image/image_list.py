from typing import Union

from ...client.api.image.image_list import sync
from ...client.client import Client
from ...client.models.image_query_type import ImageQueryType
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
        parser.cli_argument(
            "--page",
            dest="page",
            type=Union[Unset, None, int],
            required=False,
            description="""The selected page. Page numbering starts at 1""",
        )
        parser.cli_argument(
            "--per-page",
            dest="per_page",
            type=Union[Unset, None, int],
            required=False,
            description="""The number of results to show per page.""",
        )

    def request(
        self,
        client: Client,
        type: Union[Unset, None, ImageQueryType] = UNSET,
        private: Union[Unset, None, bool] = UNSET,
        tag_name: Union[Unset, None, str] = UNSET,
        page: Union[Unset, None, int] = 1,
        per_page: Union[Unset, None, int] = 20,
    ):
        return sync(
            client=client,
            type=type,
            private=private,
            tag_name=tag_name,
            page=page,
            per_page=per_page,
        )
