from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.image_options import ImageOptions
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ChangeImage")


@attr.s(auto_attribs=True)
class ChangeImage:
    """
    Attributes:
        image (Union[None, Unset, int, str]): The slug or ID of the selected image. What type of image is permitted here
            varies based on the server action. Example: 5.
        options (Union[Unset, None, ImageOptions]): Additional options for the server configuration after the image has
            been changed.
    """

    image: Union[None, Unset, int, str] = UNSET
    options: Union[Unset, None, ImageOptions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image: Union[None, Unset, int, str]
        if isinstance(self.image, Unset):
            image = UNSET
        elif self.image is None:
            image = None

        else:
            image = self.image

        options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict() if self.options else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image is not UNSET:
            field_dict["image"] = image
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_image(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        image = _parse_image(d.pop("image", UNSET))

        _options = d.pop("options", UNSET)
        options: Union[Unset, None, ImageOptions]
        if _options is None:
            options = None
        elif isinstance(_options, Unset):
            options = UNSET
        else:
            options = ImageOptions.from_dict(_options)

        change_image = cls(
            image=image,
            options=options,
        )

        change_image.additional_properties = d
        return change_image

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
