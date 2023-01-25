from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.password_reset_type import PasswordResetType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="PasswordReset")


@attr.s(auto_attribs=True)
class PasswordReset:
    """Reset the Password of a Server

    Attributes:
        type (PasswordResetType):
        username (Union[Unset, None, str]): The username of the user to change the password.
            Only valid if the server supports password change actions (check server.password_change_supported via the
            servers endpoint).
            If omitted and the server supports password change actions this will default to the username of the remote user
            that was configured when the server was created (normally 'root').
        password (Union[Unset, None, str]): If this is provided the specified or default remote user's account password
            will be set to this value.
            Only valid if the server supports password change actions (check server.password_change_supported via the
            servers endpoint).
            If omitted and the server supports password change actions a random password will be generated and emailed to
            the account email address.
    """

    type: PasswordResetType
    username: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        username = self.username
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = PasswordResetType(d.pop("type"))

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        password_reset = cls(
            type=type,
            username=username,
            password=password,
        )

        password_reset.additional_properties = d
        return password_reset

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
