from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING, List, Tuple, Union

from binarylane.api.server_action.server_action_change_advanced_features import sync_detailed
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

from binarylane.console.parser import Mapping
from binarylane.console.runners.action import ActionRunner


class CommandRequest:
    server_id: int
    json_body: ChangeAdvancedFeatures

    def __init__(self, server_id: int, json_body: ChangeAdvancedFeatures) -> None:
        self.server_id = server_id
        self.json_body = json_body


class Command(ActionRunner):
    @property
    def name(self) -> str:
        return "change-advanced-features"

    @property
    def description(self) -> str:
        return """Change the Advanced Features of a Server"""

    def create_mapping(self) -> Mapping:
        mapping = Mapping(CommandRequest)

        mapping.add_primitive(
            "server_id",
            int,
            required=True,
            option_name=None,
            description="""The ID of the server on which the action should be performed.""",
        )

        json_body = mapping.add_json_body(ChangeAdvancedFeatures)

        json_body.add_primitive(
            "type",
            ChangeAdvancedFeaturesType,
            option_name="type",
            required=True,
        )

        json_body.add_primitive(
            "enabled_advanced_features",
            Union[Unset, None, List[AdvancedFeature]],
            option_name="enabled-advanced-features",
            required=False,
            description="""Do not provide or set to null to keep existing advanced features. Provide an empty array to disable all advanced features, otherwise provide an array with selected advanced features. If provided, any currently enabled advanced features that aren't included will be disabled.""",
        )

        json_body.add_primitive(
            "processor_model",
            Union[Unset, None, str],
            option_name="processor-model",
            required=False,
            description="""Do not provide or set to null to keep existing processor model.""",
        )

        json_body.add_primitive(
            "automatic_processor_model",
            Union[Unset, None, bool],
            option_name="automatic-processor-model",
            required=False,
            description="""Set to true to use best available processor model. If this is provided the processor_model property must not be provided.""",
        )

        json_body.add_primitive(
            "machine_type",
            Union[Unset, None, VmMachineType],
            option_name="machine-type",
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| pc_i440_fx_1_point_5 | PC I440 FX 1.5 |
| pc_i440_fx_2_point_11 | PC I440 FX 2.11 |
| pc_i440_fx_4point_1 | PC I440 FX 4.1 |
| pc_i440_fx_4point_2 | PC I440 FX 4.2 |
| pc_i440_fx_5point_0 | PC I440 FX 5.0 |
| pc_i440_fx_5point_1 | PC I440 FX 5.1 |

""",
        )

        json_body.add_primitive(
            "automatic_machine_type",
            Union[Unset, None, bool],
            option_name="automatic-machine-type",
            required=False,
            description="""Set to true to use best available machine type. If this is provided the machine_type property must not be provided.""",
        )

        json_body.add_primitive(
            "video_device",
            Union[Unset, None, VideoDevice],
            option_name="video-device",
            required=False,
            description="""
| Value | Description |
| ----- | ----------- |
| cirrus-logic | Cirrus Logic GD5446 |
| standard | Standard VGA with VESA 2.0 extensions |
| virtio | Virtio VGA (800x600) |
| virtio-wide | Virtio VGA (1600x900) |

""",
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
