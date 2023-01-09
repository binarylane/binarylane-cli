from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="InvoiceLineItem")


@attr.s(auto_attribs=True)
class InvoiceLineItem:
    """
    Attributes:
        name (str): A description of the item.
        amount (float): The charge in AU$ for this item. A negative value indicates a discount or credit.
        amount_includes_tax (bool): If this is true the line item amount includes (if applicable) whatever tax was
            applied (see invoice.tax_code for details) and the total of the line items on this invoice will match the
            invoice.amount.
            If this is false the line item amount does not include any applicable tax and the total of the line items on
            this invoice will be the invoice.amount less invoice.tax.
    """

    name: str
    amount: float
    amount_includes_tax: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        amount = self.amount
        amount_includes_tax = self.amount_includes_tax

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "amount": amount,
                "amount_includes_tax": amount_includes_tax,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        amount = d.pop("amount")

        amount_includes_tax = d.pop("amount_includes_tax")

        invoice_line_item = cls(
            name=name,
            amount=amount,
            amount_includes_tax=amount_includes_tax,
        )

        invoice_line_item.additional_properties = d
        return invoice_line_item

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
