from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.models.restore_type import RestoreType

T = TypeVar("T", bound="Restore")


@attr.s(auto_attribs=True)
class Restore:
    """Restore a Backup to a Server

    Attributes:
        type (RestoreType):
        image (Union[int, str]): The ID of the specific backup to use. Snapshots are not currently supported. Example:
            5.
    """

    type: RestoreType
    image: Union[int, str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        image: Union[int, str]

        image = self.image

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "image": image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = RestoreType(d.pop("type"))

        def _parse_image(data: object) -> Union[int, str]:
            return cast(Union[int, str], data)

        image = _parse_image(d.pop("image"))

        restore = cls(
            type=type,
            image=image,
        )

        restore.additional_properties = d
        return restore

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
