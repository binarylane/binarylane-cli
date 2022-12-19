from enum import Enum


class LoadBalancerRuleProtocol(str, Enum):
    HTTP = "http"
    HTTPS = "https"
    HTTP2 = "http2"
    TCP = "tcp"

    def __str__(self) -> str:
        return str(self.value)
