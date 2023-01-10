from __future__ import annotations

from typing import Any, Type, Union

from binarylane.api.server_action.server_action_change_kernel import sync_detailed
from binarylane.client import Client
from binarylane.models.action_response import ActionResponse
from binarylane.models.change_kernel import ChangeKernel
from binarylane.models.change_kernel_type import ChangeKernelType
from binarylane.models.problem_details import ProblemDetails
from binarylane.models.validation_problem_details import ValidationProblemDetails

from binarylane.console.runners import ActionRunner


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
            int,
            description="""The ID of the server on which the action should be performed.""",
        )

        parser.cli_argument(
            "--type",
            ChangeKernelType,
            dest="type",
            required=True,
            description="""None""",
        )

        parser.cli_argument(
            "--kernel",
            int,
            dest="kernel",
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
