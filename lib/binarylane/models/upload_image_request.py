from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.backup_replacement_strategy import BackupReplacementStrategy
from binarylane.models.backup_slot import BackupSlot
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="UploadImageRequest")


@attr.s(auto_attribs=True)
class UploadImageRequest:
    """
    Attributes:
        replacement_strategy (BackupReplacementStrategy): The strategy for selecting which backup to replace (if any).
        url (str): The source URL for the image to upload. Only HTTP and HTTPS sources are currently supported.
        backup_type (Union[Unset, None, BackupSlot]): If replacement_strategy is anything other than 'specified', this
            must be provided.
        backup_id_to_replace (Union[Unset, None, int]): If replacement_strategy is 'specified' this property must be set
            to an existing backup.
        label (Union[Unset, None, str]): An optional label to identify the backup.
    """

    replacement_strategy: BackupReplacementStrategy
    url: str
    backup_type: Union[Unset, None, BackupSlot] = UNSET
    backup_id_to_replace: Union[Unset, None, int] = UNSET
    label: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        replacement_strategy = self.replacement_strategy.value

        url = self.url
        backup_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value if self.backup_type else None

        backup_id_to_replace = self.backup_id_to_replace
        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "replacement_strategy": replacement_strategy,
                "url": url,
            }
        )
        if backup_type is not UNSET:
            field_dict["backup_type"] = backup_type
        if backup_id_to_replace is not UNSET:
            field_dict["backup_id_to_replace"] = backup_id_to_replace
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        replacement_strategy = BackupReplacementStrategy(d.pop("replacement_strategy"))

        url = d.pop("url")

        _backup_type = d.pop("backup_type", UNSET)
        backup_type: Union[Unset, None, BackupSlot]
        if _backup_type is None:
            backup_type = None
        elif isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = BackupSlot(_backup_type)

        backup_id_to_replace = d.pop("backup_id_to_replace", UNSET)

        label = d.pop("label", UNSET)

        upload_image_request = cls(
            replacement_strategy=replacement_strategy,
            url=url,
            backup_type=backup_type,
            backup_id_to_replace=backup_id_to_replace,
            label=label,
        )

        upload_image_request.additional_properties = d
        return upload_image_request

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
