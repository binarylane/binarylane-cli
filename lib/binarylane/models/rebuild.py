from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.image_options import ImageOptions
from binarylane.models.rebuild_type import RebuildType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Rebuild")


@attr.s(auto_attribs=True)
class Rebuild:
    """Rebuild an Existing Server

    Attributes:
        type (RebuildType):
        image (Union[None, Unset, int, str]): The Operating System ID or slug or Backup image ID to use as a base for
            the rebuild. Example: 5.
        options (Union[Unset, None, ImageOptions]): Additional options. Leaving this entirely null or any of the
            properties included null will use the defaults from the existing server.
    """

    type: RebuildType
    image: Union[None, Unset, int, str] = UNSET
    options: Union[Unset, None, ImageOptions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

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
        field_dict.update(
            {
                "type": type,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = RebuildType(d.pop("type"))

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

        rebuild = cls(
            type=type,
            image=image,
            options=options,
        )

        rebuild.additional_properties = d
        return rebuild

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
