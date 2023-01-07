from typing import Any, Union

from ...client.api.server.server_feature_list import sync_detailed
from ...client.client import Client
from ...client.models.available_advanced_server_features_response import AvailableAdvancedServerFeaturesResponse
from ...client.models.problem_details import ProblemDetails
from ...runners import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "list"

    @property
    def description(self):
        return """Fetch the Currently Available Advanced Features for a Server"""

    def configure(self, parser):
        """Add arguments for server_feature_list"""
        parser.cli_argument(
            "server_id",
            type=int,
            description="""The ID of the server for which advanced features should be listed.""",
        )

    def request(
        self,
        server_id: int,
        client: Client,
    ) -> Union[Any, AvailableAdvancedServerFeaturesResponse, ProblemDetails]:

        page_response = sync_detailed(
            server_id=server_id,
            client=client,
        )
        return page_response.status_code, page_response.parsed
