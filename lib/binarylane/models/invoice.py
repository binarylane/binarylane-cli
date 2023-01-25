from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from binarylane.models.invoice_line_item import InvoiceLineItem
from binarylane.models.tax_code import TaxCode
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Invoice")


@attr.s(auto_attribs=True)
class Invoice:
    """
    Attributes:
        invoice_id (int): The ID of the invoice.
        invoice_number (str): The invoice number for this invoice.
        amount (float): The amount of the invoice in AU$.
        tax_code (TaxCode): The tax code that was applied to transactions on this invoice.
        tax (float): The amount of tax (if any) that was charged on the transactions on this invoice.
        created (datetime.datetime): The date in ISO8601 format this invoice was created.
        date_due (datetime.datetime): The date in ISO8601 format this invoice is due for payment.
        date_overdue (datetime.datetime): The date in ISO8601 format this invoice is considered overdue.
        paid (bool): If this is true the invoice has been paid.
        refunded (bool): If this is true the payment for this invoice has been refunded.
        invoice_items (List[InvoiceLineItem]): The individual items that make up invoice.
        reference (Union[Unset, None, str]): The reference for this invoice. If this invoice is for a single service
            this may identify the service, otherwise it will be the account reference.
        payment_failure_count (Union[Unset, None, int]): If this is included it indicates the number of failed attempts
            at processing payment for this invoice that have occurred.
        invoice_download_url (Union[Unset, None, str]): The download URL for the rendered version of the invoice.
    """

    invoice_id: int
    invoice_number: str
    amount: float
    tax_code: TaxCode
    tax: float
    created: datetime.datetime
    date_due: datetime.datetime
    date_overdue: datetime.datetime
    paid: bool
    refunded: bool
    invoice_items: List[InvoiceLineItem]
    reference: Union[Unset, None, str] = UNSET
    payment_failure_count: Union[Unset, None, int] = UNSET
    invoice_download_url: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id
        invoice_number = self.invoice_number
        amount = self.amount
        tax_code = self.tax_code.to_dict()

        tax = self.tax
        created = self.created.isoformat()

        date_due = self.date_due.isoformat()

        date_overdue = self.date_overdue.isoformat()

        paid = self.paid
        refunded = self.refunded
        invoice_items = []
        for invoice_items_item_data in self.invoice_items:
            invoice_items_item = invoice_items_item_data.to_dict()

            invoice_items.append(invoice_items_item)

        reference = self.reference
        payment_failure_count = self.payment_failure_count
        invoice_download_url = self.invoice_download_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice_id": invoice_id,
                "invoice_number": invoice_number,
                "amount": amount,
                "tax_code": tax_code,
                "tax": tax,
                "created": created,
                "date_due": date_due,
                "date_overdue": date_overdue,
                "paid": paid,
                "refunded": refunded,
                "invoice_items": invoice_items,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference
        if payment_failure_count is not UNSET:
            field_dict["payment_failure_count"] = payment_failure_count
        if invoice_download_url is not UNSET:
            field_dict["invoice_download_url"] = invoice_download_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_id = d.pop("invoice_id")

        invoice_number = d.pop("invoice_number")

        amount = d.pop("amount")

        tax_code = TaxCode.from_dict(d.pop("tax_code"))

        tax = d.pop("tax")

        created = isoparse(d.pop("created"))

        date_due = isoparse(d.pop("date_due"))

        date_overdue = isoparse(d.pop("date_overdue"))

        paid = d.pop("paid")

        refunded = d.pop("refunded")

        invoice_items = []
        _invoice_items = d.pop("invoice_items")
        for invoice_items_item_data in _invoice_items:
            invoice_items_item = InvoiceLineItem.from_dict(invoice_items_item_data)

            invoice_items.append(invoice_items_item)

        reference = d.pop("reference", UNSET)

        payment_failure_count = d.pop("payment_failure_count", UNSET)

        invoice_download_url = d.pop("invoice_download_url", UNSET)

        invoice = cls(
            invoice_id=invoice_id,
            invoice_number=invoice_number,
            amount=amount,
            tax_code=tax_code,
            tax=tax,
            created=created,
            date_due=date_due,
            date_overdue=date_overdue,
            paid=paid,
            refunded=refunded,
            invoice_items=invoice_items,
            reference=reference,
            payment_failure_count=payment_failure_count,
            invoice_download_url=invoice_download_url,
        )

        invoice.additional_properties = d
        return invoice

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
