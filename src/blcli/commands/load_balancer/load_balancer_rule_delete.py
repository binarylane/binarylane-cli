from typing import List

from ...client.api.load_balancer.load_balancer_rule_delete import sync
from ...client.client import Client
from ...client.models.forwarding_rules_request import ForwardingRulesRequest
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "load-balancer_rule_delete"

    @property
    def description(self):
        return """Remove Forwarding Rules from an Existing Load Balancer"""

    def configure(self, parser):
        """Add arguments for load-balancer_rule_delete"""
        parser.cli_argument(
            "load_balancer_id",
        )

        parser.cli_argument(
            "--forwarding-rules",
            dest="forwarding_rules",
            type=List[ForwardingRule],
            required=True,
            description="""The rules that control which traffic the load balancer will forward to servers in the pool.""",
        )

    def request(
        self,
        load_balancer_id: int,
        client: Client,
        forwarding_rules: List[ForwardingRule],
    ):
        return sync(
            load_balancer_id=load_balancer_id,
            client=client,
            json_body=ForwardingRulesRequest(
                forwarding_rules=forwarding_rules,
            ),
        )
