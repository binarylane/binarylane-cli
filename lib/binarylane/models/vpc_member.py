from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from binarylane.models.resource_type import ResourceType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="VpcMember")


@attr.s(auto_attribs=True)
class VpcMember:
    """
    Attributes:
        name (str): The name of this VPC member.
        resource_type (ResourceType):
            | Value | Description |
            | ----- | ----------- |
            | server | Server |
            | load-balancer | Load Balancer |
            | ssh-key | SSH Key |
            | vpc | Virtual Private Network |
            | image | Backup or Operating System Image |
            | registered-domain-name | Registered Domain Name |

        resource_id (str): The resource ID of this VPC member.
        created_at (Union[Unset, None, datetime.datetime]): The date and time in ISO8601 format of this resource's
            initial creation.
    """

    name: str
    resource_type: ResourceType
    resource_id: str
    created_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        resource_type = self.resource_type.value

        resource_id = self.resource_id
        created_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat() if self.created_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resource_type": resource_type,
                "resource_id": resource_id,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        resource_type = ResourceType(d.pop("resource_type"))

        resource_id = d.pop("resource_id")

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, None, datetime.datetime]
        if _created_at is None:
            created_at = None
        elif isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        vpc_member = cls(
            name=name,
            resource_type=resource_type,
            resource_id=resource_id,
            created_at=created_at,
        )

        vpc_member.additional_properties = d
        return vpc_member

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
