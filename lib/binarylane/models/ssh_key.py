from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="SshKey")


@attr.s(auto_attribs=True)
class SshKey:
    """
    Attributes:
        id (int): The ID of this SSH key.
        fingerprint (str): The fingerprint of this SSH key.
        public_key (str): The public key of this SSH key.
        default (bool): If an SSH key is marked as default it will be deployed to all newly created servers that support
            SSH keys unless expressly overridden in the creation request.
        name (Union[Unset, None, str]): The name of this SSH key. This is used only to aid in identification.
    """

    id: int
    fingerprint: str
    public_key: str
    default: bool
    name: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        fingerprint = self.fingerprint
        public_key = self.public_key
        default = self.default
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fingerprint": fingerprint,
                "public_key": public_key,
                "default": default,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        fingerprint = d.pop("fingerprint")

        public_key = d.pop("public_key")

        default = d.pop("default")

        name = d.pop("name", UNSET)

        ssh_key = cls(
            id=id,
            fingerprint=fingerprint,
            public_key=public_key,
            default=default,
            name=name,
        )

        ssh_key.additional_properties = d
        return ssh_key

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
