from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.server_actions.post_v_2_servers_server_id_actions_change_advanced_features import sync_detailed
from binarylane.models.action_response import ActionResponse
from binarylane.models.advanced_feature import AdvancedFeature
from binarylane.models.change_advanced_features import ChangeAdvancedFeatures
from binarylane.models.change_advanced_features_type import ChangeAdvancedFeaturesType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails
from binarylane.models.video_device import VideoDevice
from binarylane.models.vm_machine_type import VmMachineType
from binarylane.types import Unset

if TYPE_CHECKING:
    from binarylane.client import Client

from binarylane.console.parser import Mapping, PrimitiveAttribute
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeAdvancedFeatures

    def __init__(self, server_id: int, json_body: ChangeAdvancedFeatures) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def reference_url(self) -> str:
        return "https://api.binarylane.com.au/reference/#tag/ServerActions/paths/~1v2~1servers~1%7Bserver_id%7D~1actions#ChangeAdvancedFeatures/post"

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add(
            PrimitiveAttribute(
                "server_id",
                int,
                required=True,
                option_name=None,
                description="""The ID of the server on which the action should be performed.""",
            )
        )

        json_body = mapping.add_json_body(ChangeAdvancedFeatures)

        json_body.add(
            PrimitiveAttribute(
                "type",
                ChangeAdvancedFeaturesType,
                required=True,
                option_name="type",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "enabled_advanced_features",
                Union[Unset, None, List[AdvancedFeature]],
                required=False,
                option_name="enabled-advanced-features",
                description="""Do not provide or set to null to keep existing advanced features. Provide an empty array to disable all advanced features, otherwise provide an array with selected advanced features. If provided, any currently enabled advanced features that aren't included will be disabled.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "processor_model",
                Union[Unset, None, int],
                required=False,
                option_name="processor-model",
                description="""Do not provide or set to null to keep existing processor model.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "automatic_processor_model",
                Union[Unset, None, bool],
                required=False,
                option_name="automatic-processor-model",
                description="""Set to true to use best available processor model. If this is provided the processor_model property must not be provided.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "machine_type",
                Union[Unset, None, VmMachineType],
                required=False,
                option_name="machine-type",
                description="""Do not provide or set to null to keep existing machine type.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "automatic_machine_type",
                Union[Unset, None, bool],
                required=False,
                option_name="automatic-machine-type",
                description="""Set to true to use best available machine type. If this is provided the machine_type property must not be provided.""",
            )
        )

        json_body.add(
            PrimitiveAttribute(
                "video_device",
                Union[Unset, None, VideoDevice],
                required=False,
                option_name="video-device",
                description="""Do not provide or set to null to keep existing video device.""",
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
