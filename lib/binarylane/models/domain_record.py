from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.domain_record_type import DomainRecordType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="DomainRecord")


@attr.s(auto_attribs=True)
class DomainRecord:
    """
    Attributes:
        id (int): The ID of this domain record.
        type (DomainRecordType): A general data field that has different functions depending on the record type.

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

        name (str): The subdomain, alias, or service defined by the record.
        ttl (int): This value is the time to live for the record in seconds.
        data (Union[Unset, None, str]): Variable data depending on record type.
        priority (Union[Unset, None, int]): A priority value that is only relevant for SRV and MX records.
        port (Union[Unset, None, int]): A port value that is only relevant for SRV records.
        weight (Union[Unset, None, int]): The weight value that is only relevant for SRV records.
        flags (Union[Unset, None, int]): An unsigned integer between 0-255 that is only relevant for CAA records.
        tag (Union[Unset, None, str]): A parameter tag that is only relevant for CAA records.
    """

    id: int
    type: DomainRecordType
    name: str
    ttl: int
    data: Union[Unset, None, str] = UNSET
    priority: Union[Unset, None, int] = UNSET
    port: Union[Unset, None, int] = UNSET
    weight: Union[Unset, None, int] = UNSET
    flags: Union[Unset, None, int] = UNSET
    tag: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        name = self.name
        ttl = self.ttl
        data = self.data
        priority = self.priority
        port = self.port
        weight = self.weight
        flags = self.flags
        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "name": name,
                "ttl": ttl,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if priority is not UNSET:
            field_dict["priority"] = priority
        if port is not UNSET:
            field_dict["port"] = port
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
        id = d.pop("id")

        type = DomainRecordType(d.pop("type"))

        name = d.pop("name")

        ttl = d.pop("ttl")

        data = d.pop("data", UNSET)

        priority = d.pop("priority", UNSET)

        port = d.pop("port", UNSET)

        weight = d.pop("weight", UNSET)

        flags = d.pop("flags", UNSET)

        tag = d.pop("tag", UNSET)

        domain_record = cls(
            id=id,
            type=type,
            name=name,
            ttl=ttl,
            data=data,
            priority=priority,
            port=port,
            weight=weight,
            flags=flags,
            tag=tag,
        )

        domain_record.additional_properties = d
        return domain_record

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
