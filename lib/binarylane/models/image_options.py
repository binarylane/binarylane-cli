from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ImageOptions")


@attr.s(auto_attribs=True)
class ImageOptions:
    """
    Attributes:
        name (Union[Unset, None, str]): The hostname for the server. Leave null to accept the auto-generated permalink.
        ssh_keys (Union[Unset, None, List[Union[int, str]]]): This may be either the existing SSH Keys IDs or
            fingerprints.
            If this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating
            system supports SSH Keys).
            Submit an empty array to disable deployment of default keys.
        user_data (Union[Unset, None, str]): If provided this will be used to initialise the new server. This must be
            left null if the Image does not support UserData, see DistributionInfo.Features for more information.
        password (Union[Unset, None, str]): If this is provided the default remote user account's password will be set
            to this value. If this is null a random password will be generated and emailed to the account email address.
    """

    name: Union[Unset, None, str] = UNSET
    ssh_keys: Union[Unset, None, List[Union[int, str]]] = UNSET
    user_data: Union[Unset, None, str] = UNSET
    password: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        ssh_keys: Union[Unset, None, List[Union[int, str]]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            if self.ssh_keys is None:
                ssh_keys = None
            else:
                ssh_keys = []
                for ssh_keys_item_data in self.ssh_keys:
                    ssh_keys_item: Union[int, str]

                    ssh_keys_item = ssh_keys_item_data

                    ssh_keys.append(ssh_keys_item)

        user_data = self.user_data
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if user_data is not UNSET:
            field_dict["user_data"] = user_data
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        ssh_keys = []
        _ssh_keys = d.pop("ssh_keys", UNSET)
        for ssh_keys_item_data in _ssh_keys or []:

            def _parse_ssh_keys_item(data: object) -> Union[int, str]:
                return cast(Union[int, str], data)

            ssh_keys_item = _parse_ssh_keys_item(ssh_keys_item_data)

            ssh_keys.append(ssh_keys_item)

        user_data = d.pop("user_data", UNSET)

        password = d.pop("password", UNSET)

        image_options = cls(
            name=name,
            ssh_keys=ssh_keys,
            user_data=user_data,
            password=password,
        )

        image_options.additional_properties = d
        return image_options

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
