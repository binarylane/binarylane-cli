from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.change_network_type import ChangeNetworkType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ChangeNetwork")


@attr.s(auto_attribs=True)
class ChangeNetwork:
    """Move a Server to an Existing Network

    Attributes:
        type (ChangeNetworkType):
        vpc_id (Union[Unset, None, int]): If this is null the server will be moved into the default public network for
            the server's region.
    """

    type: ChangeNetworkType
    vpc_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        vpc_id = self.vpc_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if vpc_id is not UNSET:
            field_dict["vpc_id"] = vpc_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeNetworkType(d.pop("type"))

        vpc_id = d.pop("vpc_id", UNSET)

        change_network = cls(
            type=type,
            vpc_id=vpc_id,
        )

        change_network.additional_properties = d
        return change_network

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
