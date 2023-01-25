from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.backup_replacement_strategy import BackupReplacementStrategy
from binarylane.models.backup_slot import BackupSlot
from binarylane.models.take_backup_type import TakeBackupType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="TakeBackup")


@attr.s(auto_attribs=True)
class TakeBackup:
    """Take a Backup of a Server

    Attributes:
        type (TakeBackupType):
        replacement_strategy (BackupReplacementStrategy): The strategy for selecting which backup to replace (if any).
        backup_type (Union[Unset, None, BackupSlot]): If replacement_strategy is anything other than 'specified', this
            must be provided.
        backup_id_to_replace (Union[Unset, None, int]): If replacement_strategy is 'specified' this property must be set
            to an existing backup.
        label (Union[Unset, None, str]): An optional label to identify the backup.
    """

    type: TakeBackupType
    replacement_strategy: BackupReplacementStrategy
    backup_type: Union[Unset, None, BackupSlot] = UNSET
    backup_id_to_replace: Union[Unset, None, int] = UNSET
    label: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        replacement_strategy = self.replacement_strategy.value

        backup_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value if self.backup_type else None

        backup_id_to_replace = self.backup_id_to_replace
        label = self.label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "replacement_strategy": replacement_strategy,
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
        type = TakeBackupType(d.pop("type"))

        replacement_strategy = BackupReplacementStrategy(d.pop("replacement_strategy"))

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

        take_backup = cls(
            type=type,
            replacement_strategy=replacement_strategy,
            backup_type=backup_type,
            backup_id_to_replace=backup_id_to_replace,
            label=label,
        )

        take_backup.additional_properties = d
        return take_backup

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
