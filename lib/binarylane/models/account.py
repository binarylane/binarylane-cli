from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.account_status import AccountStatus
from binarylane.models.payment_method import PaymentMethod
from binarylane.models.tax_code import TaxCode

T = TypeVar("T", bound="Account")


@attr.s(auto_attribs=True)
class Account:
    """
    Attributes:
        email (str): The email address registered for this account.
        uuid (str): The ID of this account.
        email_verified (bool): Whether this account has been verified. Un-verified accounts are subject to some
            restrictions.
        status (AccountStatus):
            | Value | Description |
            | ----- | ----------- |
            | incomplete | An account that exists but is not ready for use. The most common reason for this is a lack of
            payment information. |
            | active | An account in the normal state. |
            | warning | An account that is under review. If you are unsure why your account has this status please urgently
            contact support. |
            | locked | An account that is no longer permitted to access the service. |

        tax_code (TaxCode): The tax code that currently applies to transactions for this account.
        configured_payment_methods (List[PaymentMethod]): The payment methods that are configured (available) for this
            account.
    """

    email: str
    uuid: str
    email_verified: bool
    status: AccountStatus
    tax_code: TaxCode
    configured_payment_methods: List[PaymentMethod]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        uuid = self.uuid
        email_verified = self.email_verified
        status = self.status.value

        tax_code = self.tax_code.to_dict()

        configured_payment_methods = []
        for configured_payment_methods_item_data in self.configured_payment_methods:
            configured_payment_methods_item = configured_payment_methods_item_data.value

            configured_payment_methods.append(configured_payment_methods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "uuid": uuid,
                "email_verified": email_verified,
                "status": status,
                "tax_code": tax_code,
                "configured_payment_methods": configured_payment_methods,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        uuid = d.pop("uuid")

        email_verified = d.pop("email_verified")

        status = AccountStatus(d.pop("status"))

        tax_code = TaxCode.from_dict(d.pop("tax_code"))

        configured_payment_methods = []
        _configured_payment_methods = d.pop("configured_payment_methods")
        for configured_payment_methods_item_data in _configured_payment_methods:
            configured_payment_methods_item = PaymentMethod(configured_payment_methods_item_data)

            configured_payment_methods.append(configured_payment_methods_item)

        account = cls(
            email=email,
            uuid=uuid,
            email_verified=email_verified,
            status=status,
            tax_code=tax_code,
            configured_payment_methods=configured_payment_methods,
        )

        account.additional_properties = d
        return account

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
