from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.change_image import ChangeImage
from binarylane.models.change_licenses import ChangeLicenses
from binarylane.models.change_size_options_request import ChangeSizeOptionsRequest
from binarylane.models.resize_type import ResizeType
from binarylane.models.take_backup import TakeBackup
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Resize")


@attr.s(auto_attribs=True)
class Resize:
    """Update the Size and Related Options for a Server

    Attributes:
        type (ResizeType):
        size (Union[Unset, None, str]): The slug of the selected size. Do not provide to keep the current size.
        options (Union[Unset, None, ChangeSizeOptionsRequest]): If this is null and the server has no selected size
            options the defaults for the size will be used. If this is null and the server has currently selected size
            options those will be preserved. If this is provided any option fields that are not included will be removed
            from the existing server.
        change_image (Union[Unset, None, ChangeImage]): This may be left null to keep the current base image for the
            server. If this is provided the server disks will be destroyed and the server will be rebuilt from the selected
            image.
        change_licenses (Union[Unset, None, ChangeLicenses]): This may be left null to keep the current licenses for the
            server. If this is provided any licenses that are not included will be removed.
        pre_action_backup (Union[Unset, None, TakeBackup]): Specify this to create a backup before any actions are
            taken, or leave null to skip.
    """

    type: ResizeType
    size: Union[Unset, None, str] = UNSET
    options: Union[Unset, None, ChangeSizeOptionsRequest] = UNSET
    change_image: Union[Unset, None, ChangeImage] = UNSET
    change_licenses: Union[Unset, None, ChangeLicenses] = UNSET
    pre_action_backup: Union[Unset, None, TakeBackup] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        size = self.size
        options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict() if self.options else None

        change_image: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.change_image, Unset):
            change_image = self.change_image.to_dict() if self.change_image else None

        change_licenses: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.change_licenses, Unset):
            change_licenses = self.change_licenses.to_dict() if self.change_licenses else None

        pre_action_backup: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.pre_action_backup, Unset):
            pre_action_backup = self.pre_action_backup.to_dict() if self.pre_action_backup else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size
        if options is not UNSET:
            field_dict["options"] = options
        if change_image is not UNSET:
            field_dict["change_image"] = change_image
        if change_licenses is not UNSET:
            field_dict["change_licenses"] = change_licenses
        if pre_action_backup is not UNSET:
            field_dict["pre_action_backup"] = pre_action_backup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ResizeType(d.pop("type"))

        size = d.pop("size", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, None, ChangeSizeOptionsRequest]
        if _options is None:
            options = None
        elif isinstance(_options, Unset):
            options = UNSET
        else:
            options = ChangeSizeOptionsRequest.from_dict(_options)

        _change_image = d.pop("change_image", UNSET)
        change_image: Union[Unset, None, ChangeImage]
        if _change_image is None:
            change_image = None
        elif isinstance(_change_image, Unset):
            change_image = UNSET
        else:
            change_image = ChangeImage.from_dict(_change_image)

        _change_licenses = d.pop("change_licenses", UNSET)
        change_licenses: Union[Unset, None, ChangeLicenses]
        if _change_licenses is None:
            change_licenses = None
        elif isinstance(_change_licenses, Unset):
            change_licenses = UNSET
        else:
            change_licenses = ChangeLicenses.from_dict(_change_licenses)

        _pre_action_backup = d.pop("pre_action_backup", UNSET)
        pre_action_backup: Union[Unset, None, TakeBackup]
        if _pre_action_backup is None:
            pre_action_backup = None
        elif isinstance(_pre_action_backup, Unset):
            pre_action_backup = UNSET
        else:
            pre_action_backup = TakeBackup.from_dict(_pre_action_backup)

        resize = cls(
            type=type,
            size=size,
            options=options,
            change_image=change_image,
            change_licenses=change_licenses,
            pre_action_backup=pre_action_backup,
        )

        resize.additional_properties = d
        return resize

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
