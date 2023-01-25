from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.distribution_feature import DistributionFeature
from binarylane.models.password_recovery_type import PasswordRecoveryType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="DistributionInfo")


@attr.s(auto_attribs=True)
class DistributionInfo:
    """
    Attributes:
        password_recovery (PasswordRecoveryType): Supported methods of password recovery.

            | Value | Description |
            | ----- | ----------- |
            | manual | Password must be reset manually using the recovery console and rescue disk. |
            | offline-clear | Password can be cleared for the admin/root user only. New password needs to be provided on
            login via the console (Requires restart). |
            | offline-change | Password can be reset and new credentials sent (Requires restart). |
            | online-change | Password may be reset without requiring a reboot via installed QEMU Guest Agent. |

        features (List[DistributionFeature]): Features supported by this distribution.
        remote_access_user (Union[Unset, None, str]): User name to use when connecting via remote access (RDP or SSH).
    """

    password_recovery: PasswordRecoveryType
    features: List[DistributionFeature]
    remote_access_user: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password_recovery = self.password_recovery.value

        features = []
        for features_item_data in self.features:
            features_item = features_item_data.value

            features.append(features_item)

        remote_access_user = self.remote_access_user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password_recovery": password_recovery,
                "features": features,
            }
        )
        if remote_access_user is not UNSET:
            field_dict["remote_access_user"] = remote_access_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password_recovery = PasswordRecoveryType(d.pop("password_recovery"))

        features = []
        _features = d.pop("features")
        for features_item_data in _features:
            features_item = DistributionFeature(features_item_data)

            features.append(features_item)

        remote_access_user = d.pop("remote_access_user", UNSET)

        distribution_info = cls(
            password_recovery=password_recovery,
            features=features,
            remote_access_user=remote_access_user,
        )

        distribution_info.additional_properties = d
        return distribution_info

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
