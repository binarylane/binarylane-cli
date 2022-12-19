from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.load_balancer_rule_protocol import LoadBalancerRuleProtocol
from ..types import UNSET, Unset

T = TypeVar("T", bound="ForwardingRule")


@attr.s(auto_attribs=True)
class ForwardingRule:
    """
    Attributes:
        entry_protocol (LoadBalancerRuleProtocol):
            | Value | Description |
            | ----- | ----------- |
            | http | The load balancer will forward HTTP traffic that matches this rule. |
            | https | The load balancer will forward HTTPS traffic that matches this rule. |
            | http2 | This option is not currently supported. |
            | tcp | This option is not currently supported. |

        entry_port (Union[Unset, None, int]): The port that traffic must match for this load balancer to forward traffic
            according to this rule.
            For rules with HTTP entry_protocol the only currently supported value is 80.
            For rules with HTTPS entry_protocol the only currently supported value is 443.
        target_protocol (Union[Unset, None, LoadBalancerRuleProtocol]):
            | Value | Description |
            | ----- | ----------- |
            | http | The load balancer will forward HTTP traffic that matches this rule. |
            | https | The load balancer will forward HTTPS traffic that matches this rule. |
            | http2 | This option is not currently supported. |
            | tcp | This option is not currently supported. |

        target_port (Union[Unset, None, int]): The port that traffic will be forwarded to according to this rule.
            Currently this must match the value of entry_port.
        certificate_id (Union[Unset, None, str]): Certificate are not currently supported.
        tls_passthrough (Union[Unset, None, bool]): TLS passthrough is not currently supported.
    """

    entry_protocol: LoadBalancerRuleProtocol
    entry_port: Union[Unset, None, int] = UNSET
    target_protocol: Union[Unset, None, LoadBalancerRuleProtocol] = UNSET
    target_port: Union[Unset, None, int] = UNSET
    certificate_id: Union[Unset, None, str] = UNSET
    tls_passthrough: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entry_protocol = self.entry_protocol.value

        entry_port = self.entry_port
        target_protocol: Union[Unset, None, str] = UNSET
        if not isinstance(self.target_protocol, Unset):
            target_protocol = self.target_protocol.value if self.target_protocol else None

        target_port = self.target_port
        certificate_id = self.certificate_id
        tls_passthrough = self.tls_passthrough

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry_protocol": entry_protocol,
            }
        )
        if entry_port is not UNSET:
            field_dict["entry_port"] = entry_port
        if target_protocol is not UNSET:
            field_dict["target_protocol"] = target_protocol
        if target_port is not UNSET:
            field_dict["target_port"] = target_port
        if certificate_id is not UNSET:
            field_dict["certificate_id"] = certificate_id
        if tls_passthrough is not UNSET:
            field_dict["tls_passthrough"] = tls_passthrough

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entry_protocol = LoadBalancerRuleProtocol(d.pop("entry_protocol"))

        entry_port = d.pop("entry_port", UNSET)

        _target_protocol = d.pop("target_protocol", UNSET)
        target_protocol: Union[Unset, None, LoadBalancerRuleProtocol]
        if _target_protocol is None:
            target_protocol = None
        elif isinstance(_target_protocol, Unset):
            target_protocol = UNSET
        else:
            target_protocol = LoadBalancerRuleProtocol(_target_protocol)

        target_port = d.pop("target_port", UNSET)

        certificate_id = d.pop("certificate_id", UNSET)

        tls_passthrough = d.pop("tls_passthrough", UNSET)

        forwarding_rule = cls(
            entry_protocol=entry_protocol,
            entry_port=entry_port,
            target_protocol=target_protocol,
            target_port=target_port,
            certificate_id=certificate_id,
            tls_passthrough=tls_passthrough,
        )

        forwarding_rule.additional_properties = d
        return forwarding_rule

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
