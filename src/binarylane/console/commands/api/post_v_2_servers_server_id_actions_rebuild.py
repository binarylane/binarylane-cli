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

import binarylane.console.commands.api.get_v2_servers as api_get_v2_servers
from binarylane.console.parser import Mapping, ObjectAttribute, PrimitiveAttribute
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: Rebuild

    def __init__(self, server_id: int, json_body: Rebuild) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#Rebuild/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        def lookup_server_id(ref: str) -> Union[None, int]:
            return api_get_v2_servers.Command(self._context).lookup(ref)

        mapping.add(
            PrimitiveAttribute(
                "server_id",
                int,
                required=True,
                option_name=None,
                metavar="server",
                description="""The ID or name of the server on which the action should be performed.""",
                lookup=lookup_server_id,
            )
        )

        json_body = mapping.add_json_body(Rebuild)

        json_body.add(
            PrimitiveAttribute(
                "type",
                RebuildType,
                required=True,
                option_name="type",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "image",
                Union[None, Unset, int, str],
                required=False,
                option_name="image",
                description="""The Operating System ID or slug or Backup image ID to use as a base for the rebuild.""",
            )
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

        json_body_image_options.add(
            PrimitiveAttribute(
                "name",
                Union[Unset, None, str],
                required=False,
                option_name="name",
                description="""The hostname for the server. Leave null to accept the auto-generated permalink.""",
            )
        )

        json_body_image_options.add(
            PrimitiveAttribute(
                "ssh_keys",
                Union[Unset, None, List[Union[int, str]]],
                required=False,
                option_name="ssh-keys",
                description="""This may be either the existing SSH Keys IDs or fingerprints.
If this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating system supports SSH Keys).
Submit an empty array to disable deployment of default keys.""",
            )
        )

        json_body_image_options.add(
            PrimitiveAttribute(
                "user_data",
                Union[Unset, None, str],
                required=False,
                option_name="user-data",
                description="""If provided this will be used to initialise the new server. This must be left null if the Image does not support UserData, see DistributionInfo.Features for more information.""",
            )
        )

        json_body_image_options.add(
            PrimitiveAttribute(
                "password",
                Union[Unset, None, str],
                required=False,
                option_name="password",
                description="""If this is provided the default remote user account's password will be set to this value. If this is null a random password will be generated and emailed to the account email address.""",
            )
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
