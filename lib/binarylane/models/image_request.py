from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ImageRequest")


@attr.s(auto_attribs=True)
class ImageRequest:
    """
    Attributes:
        name (Union[Unset, None, str]): Optional: a new display name for this image. Do not provide to leave the display
            name unchanged, submit an empty string to clear the display name.
        locked (Union[Unset, None, bool]): Optional: you may choose to lock an individual backup in which case we will
            not update that backup until you unlock it. Do not provide to leave the locked status unchanged.
    """

    name: Union[Unset, None, str] = UNSET
    locked: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        locked = self.locked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if locked is not UNSET:
            field_dict["locked"] = locked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        locked = d.pop("locked", UNSET)

        image_request = cls(
            name=name,
            locked=locked,
        )

        image_request.additional_properties = d
        return image_request

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
