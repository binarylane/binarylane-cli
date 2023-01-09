from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="UpdateSshKeyRequest")


@attr.s(auto_attribs=True)
class UpdateSshKeyRequest:
    """
    Attributes:
        name (str): A name to help you identify the key.
        default (Union[Unset, None, bool]): Do not provide or leave null to leave the default status of the key
            unchanged.
            Optional: If true this will be added to all new server installations (if we support SSH Key injection for the
            server's operating system).
    """

    name: str
    default: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        default = d.pop("default", UNSET)

        update_ssh_key_request = cls(
            name=name,
            default=default,
        )

        update_ssh_key_request.additional_properties = d
        return update_ssh_key_request

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
