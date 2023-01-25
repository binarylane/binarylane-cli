from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.tax_code_type import TaxCodeType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="TaxCode")


@attr.s(auto_attribs=True)
class TaxCode:
    """
    Attributes:
        name (str): The name of this tax code.
        type (TaxCodeType): The type of tax code.

            | Value | Description |
            | ----- | ----------- |
            | none | No tax is applied to any transaction. |
            | scalar | A fixed fraction of the value of all transactions is added as tax. |

        fixed_percent (Union[Unset, None, float]): If this is set then this tax is added to all applicable transactions.
            This is a percentage value where 100 = 100%. For example: if the type is 'scalar' and the value of this is '10'
            then 10% of the value of all transactions will be added as tax.
    """

    name: str
    type: TaxCodeType
    fixed_percent: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        fixed_percent = self.fixed_percent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if fixed_percent is not UNSET:
            field_dict["fixed_percent"] = fixed_percent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = TaxCodeType(d.pop("type"))

        fixed_percent = d.pop("fixed_percent", UNSET)

        tax_code = cls(
            name=name,
            type=type,
            fixed_percent=fixed_percent,
        )

        tax_code.additional_properties = d
        return tax_code

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
