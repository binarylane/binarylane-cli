from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="OffsiteBackupSettings")


@attr.s(auto_attribs=True)
class OffsiteBackupSettings:
    """
    Attributes:
        use_custom_backup_location (bool): If this is true a custom backup location will be used. If false our
            internally managed offsite backup location be used.
        offsite_backup_location (Union[Unset, None, str]): If a custom backup location is used, this is the provided
            location.
        manage_offsite_copies (Union[Unset, None, bool]): This only has effect if a custom offsite location is being
            used: the internal offsite backup location always manages copies.
            If this is true old offsite backups will be removed once the replacement upload is complete.
            If this is false backups must be removed from the Amazon S3 bucket manually. Amazon will charge your S3 account
            at their standard rate for every backup stored.
    """

    use_custom_backup_location: bool
    offsite_backup_location: Union[Unset, None, str] = UNSET
    manage_offsite_copies: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_custom_backup_location = self.use_custom_backup_location
        offsite_backup_location = self.offsite_backup_location
        manage_offsite_copies = self.manage_offsite_copies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "use_custom_backup_location": use_custom_backup_location,
            }
        )
        if offsite_backup_location is not UNSET:
            field_dict["offsite_backup_location"] = offsite_backup_location
        if manage_offsite_copies is not UNSET:
            field_dict["manage_offsite_copies"] = manage_offsite_copies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        use_custom_backup_location = d.pop("use_custom_backup_location")

        offsite_backup_location = d.pop("offsite_backup_location", UNSET)

        manage_offsite_copies = d.pop("manage_offsite_copies", UNSET)

        offsite_backup_settings = cls(
            use_custom_backup_location=use_custom_backup_location,
            offsite_backup_location=offsite_backup_location,
            manage_offsite_copies=manage_offsite_copies,
        )

        offsite_backup_settings.additional_properties = d
        return offsite_backup_settings

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
