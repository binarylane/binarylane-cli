from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.domain_record_type import DomainRecordType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="UpdateDomainRecordRequest")


@attr.s(auto_attribs=True)
class UpdateDomainRecordRequest:
    """Any values not provided will be retained. Provide empty strings to clear existing string values, nulls to retain the
    existing values.

        Attributes:
            type (Union[Unset, None, DomainRecordType]): The type of the DNS record.

                | Value | Description |
                | ----- | ----------- |
                | A | Map an IPv4 address to a hostname. |
                | AAAA | Map an IPv6 address to a hostname. |
                | CAA | Restrict which certificate authorities are permitted to issue certificates for a domain. |
                | CNAME | Define an alias for your canonical hostname. |
                | MX | Define the mail exchanges that handle mail for the domain. |
                | NS | Define the nameservers that manage the domain. |
                | SOA | The Start of Authority record for the zone. |
                | SRV | Specify a server by hostname and port to handle a service or services. |
                | TXT | Define a string of text that is associated with a hostname. |

            name (Union[Unset, None, str]): The subdomain for this record. Use @ for records on the domain itself, and * to
                create a wildcard record.
            data (Union[Unset, None, str]): A general data field that has different functions depending on the record type.
            priority (Union[Unset, None, int]): A priority value that is only relevant for SRV and MX records.
            port (Union[Unset, None, int]): A port value that is only relevant for SRV records.
            ttl (Union[Unset, None, int]): This value is the time to live for the record, in seconds.
            weight (Union[Unset, None, int]): The weight value that is only relevant for SRV records.
            flags (Union[Unset, None, int]): An unsigned integer between 0-255 that is only relevant for CAA records.
            tag (Union[Unset, None, str]): A parameter tag that is only relevant for CAA records.
    """

    type: Union[Unset, None, DomainRecordType] = UNSET
    name: Union[Unset, None, str] = UNSET
    data: Union[Unset, None, str] = UNSET
    priority: Union[Unset, None, int] = UNSET
    port: Union[Unset, None, int] = UNSET
    ttl: Union[Unset, None, int] = UNSET
    weight: Union[Unset, None, int] = UNSET
    flags: Union[Unset, None, int] = UNSET
    tag: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, None, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        name = self.name
        data = self.data
        priority = self.priority
        port = self.port
        ttl = self.ttl
        weight = self.weight
        flags = self.flags
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if data is not UNSET:
            field_dict["data"] = data
        if priority is not UNSET:
            field_dict["priority"] = priority
        if port is not UNSET:
            field_dict["port"] = port
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if weight is not UNSET:
            field_dict["weight"] = weight
        if flags is not UNSET:
            field_dict["flags"] = flags
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, None, DomainRecordType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = DomainRecordType(_type)

        name = d.pop("name", UNSET)

        data = d.pop("data", UNSET)

        priority = d.pop("priority", UNSET)

        port = d.pop("port", UNSET)

        ttl = d.pop("ttl", UNSET)

        weight = d.pop("weight", UNSET)

        flags = d.pop("flags", UNSET)

        tag = d.pop("tag", UNSET)

        update_domain_record_request = cls(
            type=type,
            name=name,
            data=data,
            priority=priority,
            port=port,
            ttl=ttl,
            weight=weight,
            flags=flags,
            tag=tag,
        )

        update_domain_record_request.additional_properties = d
        return update_domain_record_request

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
