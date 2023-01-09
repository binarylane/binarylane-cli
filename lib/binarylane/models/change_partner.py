from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.change_partner_type import ChangePartnerType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ChangePartner")


@attr.s(auto_attribs=True)
class ChangePartner:
    """Add, Update or Remove a Partner Server for a Server

    Attributes:
        type (ChangePartnerType):
        partner_server_id (Union[Unset, None, int]): Leave this null to remove the server partnership. The partner
            server must be in the same region as the target server.
    """

    type: ChangePartnerType
    partner_server_id: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        partner_server_id = self.partner_server_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if partner_server_id is not UNSET:
            field_dict["partner_server_id"] = partner_server_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangePartnerType(d.pop("type"))

        partner_server_id = d.pop("partner_server_id", UNSET)

        change_partner = cls(
            type=type,
            partner_server_id=partner_server_id,
        )

        change_partner.additional_properties = d
        return change_partner

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
