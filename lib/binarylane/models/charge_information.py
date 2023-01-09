from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="ChargeInformation")


@attr.s(auto_attribs=True)
class ChargeInformation:
    """
    Attributes:
        created (datetime.datetime): The time when the charge was created.
        description (str): A summary of the charge.
        total (float): The cost in AU$.
        ongoing (bool): If this is true the charge is for an ongoing service. If this is false the charge is complete
            and awaiting invoicing.
    """

    created: datetime.datetime
    description: str
    total: float
    ongoing: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created.isoformat()

        description = self.description
        total = self.total
        ongoing = self.ongoing

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "description": description,
                "total": total,
                "ongoing": ongoing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = isoparse(d.pop("created"))

        description = d.pop("description")

        total = d.pop("total")

        ongoing = d.pop("ongoing")

        charge_information = cls(
            created=created,
            description=description,
            total=total,
            ongoing=ongoing,
        )

        charge_information.additional_properties = d
        return charge_information

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
