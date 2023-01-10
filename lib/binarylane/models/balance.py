from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from binarylane.models.charge_information import ChargeInformation
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Balance")


@attr.s(auto_attribs=True)
class Balance:
    """
    Attributes:
        unbilled_total (float): The total of any un-billed charges in AU$.
        available_credit (float): Available credit in AU$.
        charges (List[ChargeInformation]): A list of all of the individual charges that contribute to the un-billed
            total.
        generated_at (Union[Unset, None, datetime.datetime]): The timestamp of the most recent charge.
    """

    unbilled_total: float
    available_credit: float
    charges: List[ChargeInformation]
    generated_at: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unbilled_total = self.unbilled_total
        available_credit = self.available_credit
        charges = []
        for charges_item_data in self.charges:
            charges_item = charges_item_data.to_dict()

            charges.append(charges_item)

        generated_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.generated_at, Unset):
            generated_at = self.generated_at.isoformat() if self.generated_at else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unbilled_total": unbilled_total,
                "available_credit": available_credit,
                "charges": charges,
            }
        )
        if generated_at is not UNSET:
            field_dict["generated_at"] = generated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unbilled_total = d.pop("unbilled_total")

        available_credit = d.pop("available_credit")

        charges = []
        _charges = d.pop("charges")
        for charges_item_data in _charges:
            charges_item = ChargeInformation.from_dict(charges_item_data)

            charges.append(charges_item)

        _generated_at = d.pop("generated_at", UNSET)
        generated_at: Union[Unset, None, datetime.datetime]
        if _generated_at is None:
            generated_at = None
        elif isinstance(_generated_at, Unset):
            generated_at = UNSET
        else:
            generated_at = isoparse(_generated_at)

        balance = cls(
            unbilled_total=unbilled_total,
            available_credit=available_credit,
            charges=charges,
            generated_at=generated_at,
        )

        balance.additional_properties = d
        return balance

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
