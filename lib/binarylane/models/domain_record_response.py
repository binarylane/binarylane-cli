from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.domain_record import DomainRecord

T = TypeVar("T", bound="DomainRecordResponse")


@attr.s(auto_attribs=True)
class DomainRecordResponse:
    """
    Attributes:
        domain_record (DomainRecord):
    """

    domain_record: DomainRecord
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain_record = self.domain_record.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain_record": domain_record,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain_record = DomainRecord.from_dict(d.pop("domain_record"))

        domain_record_response = cls(
            domain_record=domain_record,
        )

        domain_record_response.additional_properties = d
        return domain_record_response

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
