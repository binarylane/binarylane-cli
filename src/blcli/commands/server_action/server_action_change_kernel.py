from ...client.api.server_action.server_action_change_kernel import sync
from ...client.client import Client
from ...client.models.change_kernel import ChangeKernel
from ...client.models.change_kernel_type import ChangeKernelType
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server-action_change-kernel"

    @property
    def description(self):
        return """Change the Kernel of a Server"""

    def configure(self, parser):
        """Add arguments for server-action_change-kernel"""
        parser.cli_argument(
            "server_id",
            description="""The target server id.""",
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
            description="""None""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
        type: ChangeKernelType,
        kernel: int,
    ):
        return sync(
            server_id=server_id,
            client=client,
            json_body=ChangeKernel(
                type=type,
                kernel=kernel,
            ),
        )
