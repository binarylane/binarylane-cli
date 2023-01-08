from typing import Any, Type, Union

from ...client.api.server_action.server_action_change_kernel import sync_detailed
from ...client.client import Client
from ...client.models.action_response import ActionResponse
from ...client.models.change_kernel import ChangeKernel
from ...client.models.change_kernel_type import ChangeKernelType
from ...client.models.problem_details import ProblemDetails
from ...client.models.validation_problem_details import ValidationProblemDetails
from ...runners import ActionRunner


class Command(ActionRunner):
    @property
    def name(self):
        return "change-kernel"

    @property
    def description(self):
        return """Change the Kernel of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-kernel"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            dest="type",
            type=ChangeKernelType,
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--kernel",
            dest="kernel",
            type=int,
            required=True,
            description="""The ID of the kernel to use.""",
        )

    @property
    def ok_response_type(self) -> Type:
        return ActionResponse

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeKernelType,
        kernel: int,
    ) -> Union[ActionResponse, Any, ProblemDetails, ValidationProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
            json_body=ChangeKernel(
                type=type,
                kernel=kernel,
            ),
        )
        return page_response.status_code, page_response.parsed
