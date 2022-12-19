from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sticky_sessions_type import StickySessionsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StickySessions")


@attr.s(auto_attribs=True)
class StickySessions:
    """
    Attributes:
        type (Union[Unset, None, StickySessionsType]):
            | Value | Description |
            | ----- | ----------- |
            | none | Do not use sticky sessions. |
            | cookies | Use cookie based sticky sessions. This option is not currently supported. |

        cookie_name (Union[Unset, None, str]):
        cookie_ttl_seconds (Union[Unset, None, int]):
    """

    type: Union[Unset, None, StickySessionsType] = UNSET
    cookie_name: Union[Unset, None, str] = UNSET
    cookie_ttl_seconds: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, None, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value if self.type else None

        cookie_name = self.cookie_name
        cookie_ttl_seconds = self.cookie_ttl_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if cookie_name is not UNSET:
            field_dict["cookie_name"] = cookie_name
        if cookie_ttl_seconds is not UNSET:
            field_dict["cookie_ttl_seconds"] = cookie_ttl_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, None, StickySessionsType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = StickySessionsType(_type)

        cookie_name = d.pop("cookie_name", UNSET)

        cookie_ttl_seconds = d.pop("cookie_ttl_seconds", UNSET)

        sticky_sessions = cls(
            type=type,
            cookie_name=cookie_name,
            cookie_ttl_seconds=cookie_ttl_seconds,
        )

        sticky_sessions.additional_properties = d
        return sticky_sessions

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
