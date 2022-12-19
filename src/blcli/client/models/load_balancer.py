import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.algorithm_type import AlgorithmType
from ..models.forwarding_rule import ForwardingRule
from ..models.health_check import HealthCheck
from ..models.load_balancer_status import LoadBalancerStatus
from ..models.region import Region
from ..models.sticky_sessions import StickySessions
from ..types import UNSET, Unset

T = TypeVar("T", bound="LoadBalancer")


@attr.s(auto_attribs=True)
class LoadBalancer:
    """
    Attributes:
        id (int): The ID of the load balancer.
        name (str): The hostname of the load balancer.
        ip (str): The IPv4 address of the load balancer.
        status (LoadBalancerStatus):
            | Value | Description |
            | ----- | ----------- |
            | new | The load balancer is currently being built and is not ready to accept connections. |
            | active | The load balancer is available. |
            | errored | The load balancer is in an errored state. |

        created_at (datetime.datetime): The date and time in ISO8601 format of the creation of the load balancer.
        forwarding_rules (List[ForwardingRule]): The rules that control which traffic the load balancer will forward to
            servers in the pool.
        health_check (HealthCheck):
        sticky_sessions (StickySessions):
        server_ids (List[int]): The server IDs of the servers that are currently in the load balancer pool (regardless
            of their current 'health').
        algorithm (AlgorithmType):
            | Value | Description |
            | ----- | ----------- |
            | round_robin | Each request will be sent to one of the nominated servers in turn. |
            | least_connections | Each request will be sent to the server with the least existing connections. This option
            is not currently supported. |

        redirect_http_to_https (bool): Whether to redirect HTTP traffic received by the load balancer to HTTPS. This is
            not currently supported.
        enable_proxy_protocol (bool): Whether the PROXY protocol is enabled on the load balancer. This is not currently
            supported.
        enable_backend_keepalive (bool): Whether to use HTTP keepalive connections to servers in the load balancer pool.
            This is not currently supported.
        region (Union[Unset, None, Region]):
        tag (Union[Unset, None, str]): Adding servers by tag is currently not supported and this value will always be
            null.
        vpc_id (Union[Unset, None, int]): The VPC ID of the VPC the load balancer is assigned to. This is not currently
            supported: all load balancers are either in the default (public) network for the region or are 'AnyCast' load
            balancers.
    """

    id: int
    name: str
    ip: str
    status: LoadBalancerStatus
    created_at: datetime.datetime
    forwarding_rules: List[ForwardingRule]
    health_check: HealthCheck
    sticky_sessions: StickySessions
    server_ids: List[int]
    algorithm: AlgorithmType
    redirect_http_to_https: bool
    enable_proxy_protocol: bool
    enable_backend_keepalive: bool
    region: Union[Unset, None, Region] = UNSET
    tag: Union[Unset, None, str] = UNSET
    vpc_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        ip = self.ip
        status = self.status.value

        created_at = self.created_at.isoformat()

        forwarding_rules = []
        for forwarding_rules_item_data in self.forwarding_rules:
            forwarding_rules_item = forwarding_rules_item_data.to_dict()

            forwarding_rules.append(forwarding_rules_item)

        health_check = self.health_check.to_dict()

        sticky_sessions = self.sticky_sessions.to_dict()

        server_ids = self.server_ids

        algorithm = self.algorithm.value

        redirect_http_to_https = self.redirect_http_to_https
        enable_proxy_protocol = self.enable_proxy_protocol
        enable_backend_keepalive = self.enable_backend_keepalive
        region: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict() if self.region else None

        tag = self.tag
        vpc_id = self.vpc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "ip": ip,
                "status": status,
                "created_at": created_at,
                "forwarding_rules": forwarding_rules,
                "health_check": health_check,
                "sticky_sessions": sticky_sessions,
                "server_ids": server_ids,
                "algorithm": algorithm,
                "redirect_http_to_https": redirect_http_to_https,
                "enable_proxy_protocol": enable_proxy_protocol,
                "enable_backend_keepalive": enable_backend_keepalive,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if tag is not UNSET:
            field_dict["tag"] = tag
        if vpc_id is not UNSET:
            field_dict["vpc_id"] = vpc_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        ip = d.pop("ip")

        status = LoadBalancerStatus(d.pop("status"))

        created_at = isoparse(d.pop("created_at"))

        forwarding_rules = []
        _forwarding_rules = d.pop("forwarding_rules")
        for forwarding_rules_item_data in _forwarding_rules:
            forwarding_rules_item = ForwardingRule.from_dict(forwarding_rules_item_data)

            forwarding_rules.append(forwarding_rules_item)

        health_check = HealthCheck.from_dict(d.pop("health_check"))

        sticky_sessions = StickySessions.from_dict(d.pop("sticky_sessions"))

        server_ids = cast(List[int], d.pop("server_ids"))

        algorithm = AlgorithmType(d.pop("algorithm"))

        redirect_http_to_https = d.pop("redirect_http_to_https")

        enable_proxy_protocol = d.pop("enable_proxy_protocol")

        enable_backend_keepalive = d.pop("enable_backend_keepalive")

        _region = d.pop("region", UNSET)
        region: Union[Unset, None, Region]
        if _region is None:
            region = None
        elif isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        tag = d.pop("tag", UNSET)

        vpc_id = d.pop("vpc_id", UNSET)

        load_balancer = cls(
            id=id,
            name=name,
            ip=ip,
            status=status,
            created_at=created_at,
            forwarding_rules=forwarding_rules,
            health_check=health_check,
            sticky_sessions=sticky_sessions,
            server_ids=server_ids,
            algorithm=algorithm,
            redirect_http_to_https=redirect_http_to_https,
            enable_proxy_protocol=enable_proxy_protocol,
            enable_backend_keepalive=enable_backend_keepalive,
            region=region,
            tag=tag,
            vpc_id=vpc_id,
        )

        load_balancer.additional_properties = d
        return load_balancer

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
