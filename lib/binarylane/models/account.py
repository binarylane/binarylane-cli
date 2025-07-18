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
        email_verified (bool): Whether this account has been verified. Un-verified accounts are subject to some
            restrictions.
        two_factor_authentication_enabled (bool): Whether this account has enabled two factor authentication.
        status (AccountStatus): The status of this account.

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
        additional_ipv4_limit (int): The maximum additional IPv4 addresses this account may assign across all servers.
            You may contact support to request this limit be increased.
    """

    email: str
    email_verified: bool
    two_factor_authentication_enabled: bool
    status: AccountStatus
    tax_code: TaxCode
    configured_payment_methods: List[PaymentMethod]
    additional_ipv4_limit: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        email_verified = self.email_verified
        two_factor_authentication_enabled = self.two_factor_authentication_enabled
        status = self.status.value

        tax_code = self.tax_code.to_dict()

        configured_payment_methods = []
        for configured_payment_methods_item_data in self.configured_payment_methods:
            configured_payment_methods_item = configured_payment_methods_item_data.value

            configured_payment_methods.append(configured_payment_methods_item)

        additional_ipv4_limit = self.additional_ipv4_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "email_verified": email_verified,
                "two_factor_authentication_enabled": two_factor_authentication_enabled,
                "status": status,
                "tax_code": tax_code,
                "configured_payment_methods": configured_payment_methods,
                "additional_ipv4_limit": additional_ipv4_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        email_verified = d.pop("email_verified")

        two_factor_authentication_enabled = d.pop("two_factor_authentication_enabled")

        status = AccountStatus(d.pop("status"))

        tax_code = TaxCode.from_dict(d.pop("tax_code"))

        configured_payment_methods = []
        _configured_payment_methods = d.pop("configured_payment_methods")
        for configured_payment_methods_item_data in _configured_payment_methods:
            configured_payment_methods_item = PaymentMethod(configured_payment_methods_item_data)

            configured_payment_methods.append(configured_payment_methods_item)

        additional_ipv4_limit = d.pop("additional_ipv4_limit")

        account = cls(
            email=email,
            email_verified=email_verified,
            two_factor_authentication_enabled=two_factor_authentication_enabled,
            status=status,
            tax_code=tax_code,
            configured_payment_methods=configured_payment_methods,
            additional_ipv4_limit=additional_ipv4_limit,
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
