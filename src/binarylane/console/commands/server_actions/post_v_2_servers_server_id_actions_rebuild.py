from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_rebuild import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.image_options import ImageOptions
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.rebuild import Rebuild
from binarylane.models.rebuild_type import RebuildType
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping, ObjectAttribute
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: Rebuild

    def __init__(self, server_id: int, json_body: Rebuild) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "rebuild"

    @property
    def description(self) -> str:
        return """Rebuild an Existing Server"""

    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#Rebuild/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(Rebuild)

        json_body.add_primitive(
            "type",
            RebuildType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "image",
            Union[None, Unset, int, str],
            option_name="image",
            required=False,
            description="""The Operating System ID or slug or Backup image ID to use as a base for the rebuild.""",
        )

        json_body_image_options = json_body.add(
            ObjectAttribute(
                "options",
                ImageOptions,
                option_name="options",
                required=False,
                description="""Additional options. Leaving this entirely null or any of the properties included null will use the defaults from the existing server.""",
            )
        )

        json_body_image_options.add_primitive(
            "name",
            Union[Unset, None, str],
            option_name="name",
            required=False,
            description="""The hostname for the server. Leave null to accept the auto-generated permalink.""",
        )

        json_body_image_options.add_primitive(
            "ssh_keys",
            Union[Unset, None, List[Union[int, str]]],
            option_name="ssh-keys",
            required=False,
            description="""This may be either the existing SSH Keys IDs or fingerprints.
If this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating system supports SSH Keys).
Submit an empty array to disable deployment of default keys.""",
        )

        json_body_image_options.add_primitive(
            "user_data",
            Union[Unset, None, str],
            option_name="user-data",
            required=False,
            description="""If provided this will be used to initialise the new server. This must be left null if the Image does not support UserData, see DistributionInfo.Features for more information.""",
        )

        json_body_image_options.add_primitive(
            "password",
            Union[Unset, None, str],
            option_name="password",
            required=False,
            description="""If this is provided the default remote user account's password will be set to this value. If this is null a random password will be generated and emailed to the account email address.""",
        )

        return mapping

    @property
    def ok_response_type(self) -> type:
        return ActionResponse

    def request(
        self,
        client: Client,
        request: object,
    ) -> Tuple[HTTPStatus, Union[ActionResponse, None, ProblemDetails, ValidationProblemDetails]]:
        assert isinstance(request, CommandRequest)

        # HTTPStatus.OK: ActionResponse
        # HTTPStatus.ACCEPTED: Any
        # HTTPStatus.BAD_REQUEST: ValidationProblemDetails
        # HTTPStatus.NOT_FOUND: ProblemDetails
        # HTTPStatus.UNPROCESSABLE_ENTITY: ProblemDetails
        # HTTPStatus.UNAUTHORIZED: Any
        page_response = sync_detailed(
            server_id=request.server_id,
            client=client,
            json_body=request.json_body,
        )
        return page_response.status_code, page_response.parsed
