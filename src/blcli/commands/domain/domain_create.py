from typing import Union

from ...client.api.domain.domain_create import sync
from ...client.client import Client
from ...client.models.domain_request import DomainRequest
from ...client.types import UNSET, Unset
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "domain_create"

    @property
    def description(self):
        return """Create a New Domain"""

    def configure(self, parser):
        """Add arguments for domain_create"""

        parser.cli_argument(
            "--name",
            dest="name",
            type=str,
            required=True,
            description="""The domain name to add to the DNS management system.""",
        )

        parser.cli_argument(
            "--ip-address",
            dest="ip_address",
            type=Union[Unset, None, str],
            required=False,
            description="""An optional IPv4 address that will be used to create an A record for the root domain.""",
        )

    def request(
        self,
        client: Client,
        name: str,
        ip_address: Union[Unset, None, str] = UNSET,
    ):
        return sync(
            client=client,
            json_body=DomainRequest(
                name=name,
                ip_address=ip_address,
            ),
        )
