from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.algorithm_type import AlgorithmType
from ..models.forwarding_rule import ForwardingRule
from ..models.health_check import HealthCheck
from ..models.sticky_sessions import StickySessions
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLoadBalancerRequest")


@attr.s(auto_attribs=True)
class CreateLoadBalancerRequest:
    """
    Attributes:
        name (str): The hostname of the load balancer.
        algorithm (Union[Unset, None, AlgorithmType]):
            | Value | Description |
            | ----- | ----------- |
            | round_robin | Each request will be sent to one of the nominated servers in turn. |
            | least_connections | Each request will be sent to the server with the least existing connections. This option
            is not currently supported. |

        forwarding_rules (Union[Unset, None, List[ForwardingRule]]): The rules that control which traffic the load
            balancer will forward to servers in the pool. Leave null to accept a default "HTTP" only forwarding rule.
        health_check (Union[Unset, None, HealthCheck]):
        sticky_sessions (Union[Unset, None, StickySessions]):
        redirect_http_to_https (Union[Unset, None, bool]): Redirect HTTP traffic received by the load balancer to HTTPS.
            This is not currently supported.
        enable_proxy_protocol (Union[Unset, None, bool]): Enable the PROXY protocol on the load balancer. This is not
            currently supported.
        enable_backend_keepalive (Union[Unset, None, bool]): Use HTTP keepalive connections to servers in the load
            balancer pool. This is not currently supported.
        server_ids (Union[Unset, None, List[int]]): A list of server IDs to assign to this load balancer. This is
            mutually exclusive with 'tag'.
        tag (Union[Unset, None, str]): Tags are not currently supported and attempting to add servers by tag will add no
            servers. This is mutually exclusive with 'server_ids'.
        region (Union[Unset, None, str]): Leave null to create an anycast load balancer.
        vpc_id (Union[Unset, None, int]): Adding or assigning a load balancer to a VPC is not currently supported.
    """

    name: str
    algorithm: Union[Unset, None, AlgorithmType] = UNSET
    forwarding_rules: Union[Unset, None, List[ForwardingRule]] = UNSET
    health_check: Union[Unset, None, HealthCheck] = UNSET
    sticky_sessions: Union[Unset, None, StickySessions] = UNSET
    redirect_http_to_https: Union[Unset, None, bool] = UNSET
    enable_proxy_protocol: Union[Unset, None, bool] = UNSET
    enable_backend_keepalive: Union[Unset, None, bool] = UNSET
    server_ids: Union[Unset, None, List[int]] = UNSET
    tag: Union[Unset, None, str] = UNSET
    region: Union[Unset, None, str] = UNSET
    vpc_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        algorithm: Union[Unset, None, str] = UNSET
        if not isinstance(self.algorithm, Unset):
            algorithm = self.algorithm.value if self.algorithm else None

        forwarding_rules: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.forwarding_rules, Unset):
            if self.forwarding_rules is None:
                forwarding_rules = None
            else:
                forwarding_rules = []
                for forwarding_rules_item_data in self.forwarding_rules:
                    forwarding_rules_item = forwarding_rules_item_data.to_dict()

                    forwarding_rules.append(forwarding_rules_item)

        health_check: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.health_check, Unset):
            health_check = self.health_check.to_dict() if self.health_check else None

        sticky_sessions: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.sticky_sessions, Unset):
            sticky_sessions = self.sticky_sessions.to_dict() if self.sticky_sessions else None

        redirect_http_to_https = self.redirect_http_to_https
        enable_proxy_protocol = self.enable_proxy_protocol
        enable_backend_keepalive = self.enable_backend_keepalive
        server_ids: Union[Unset, None, List[int]] = UNSET
        if not isinstance(self.server_ids, Unset):
            if self.server_ids is None:
                server_ids = None
            else:
                server_ids = self.server_ids

        tag = self.tag
        region = self.region
        vpc_id = self.vpc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if algorithm is not UNSET:
            field_dict["algorithm"] = algorithm
        if forwarding_rules is not UNSET:
            field_dict["forwarding_rules"] = forwarding_rules
        if health_check is not UNSET:
            field_dict["health_check"] = health_check
        if sticky_sessions is not UNSET:
            field_dict["sticky_sessions"] = sticky_sessions
        if redirect_http_to_https is not UNSET:
            field_dict["redirect_http_to_https"] = redirect_http_to_https
        if enable_proxy_protocol is not UNSET:
            field_dict["enable_proxy_protocol"] = enable_proxy_protocol
        if enable_backend_keepalive is not UNSET:
            field_dict["enable_backend_keepalive"] = enable_backend_keepalive
        if server_ids is not UNSET:
            field_dict["server_ids"] = server_ids
        if tag is not UNSET:
            field_dict["tag"] = tag
        if region is not UNSET:
            field_dict["region"] = region
        if vpc_id is not UNSET:
            field_dict["vpc_id"] = vpc_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        _algorithm = d.pop("algorithm", UNSET)
        algorithm: Union[Unset, None, AlgorithmType]
        if _algorithm is None:
            algorithm = None
        elif isinstance(_algorithm, Unset):
            algorithm = UNSET
        else:
            algorithm = AlgorithmType(_algorithm)

        forwarding_rules = []
        _forwarding_rules = d.pop("forwarding_rules", UNSET)
        for forwarding_rules_item_data in _forwarding_rules or []:
            forwarding_rules_item = ForwardingRule.from_dict(forwarding_rules_item_data)

            forwarding_rules.append(forwarding_rules_item)

        _health_check = d.pop("health_check", UNSET)
        health_check: Union[Unset, None, HealthCheck]
        if _health_check is None:
            health_check = None
        elif isinstance(_health_check, Unset):
            health_check = UNSET
        else:
            health_check = HealthCheck.from_dict(_health_check)

        _sticky_sessions = d.pop("sticky_sessions", UNSET)
        sticky_sessions: Union[Unset, None, StickySessions]
        if _sticky_sessions is None:
            sticky_sessions = None
        elif isinstance(_sticky_sessions, Unset):
            sticky_sessions = UNSET
        else:
            sticky_sessions = StickySessions.from_dict(_sticky_sessions)

        redirect_http_to_https = d.pop("redirect_http_to_https", UNSET)

        enable_proxy_protocol = d.pop("enable_proxy_protocol", UNSET)

        enable_backend_keepalive = d.pop("enable_backend_keepalive", UNSET)

        server_ids = cast(List[int], d.pop("server_ids", UNSET))

        tag = d.pop("tag", UNSET)

        region = d.pop("region", UNSET)

        vpc_id = d.pop("vpc_id", UNSET)

        create_load_balancer_request = cls(
            name=name,
            algorithm=algorithm,
            forwarding_rules=forwarding_rules,
            health_check=health_check,
            sticky_sessions=sticky_sessions,
            redirect_http_to_https=redirect_http_to_https,
            enable_proxy_protocol=enable_proxy_protocol,
            enable_backend_keepalive=enable_backend_keepalive,
            server_ids=server_ids,
            tag=tag,
            region=region,
            vpc_id=vpc_id,
        )

        create_load_balancer_request.additional_properties = d
        return create_load_balancer_request

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
