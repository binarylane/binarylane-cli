from __future__ import annotations

from typing import Any, Dict, List, Optional, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ValidationProblemDetails")


@attr.s(auto_attribs=True)
class ValidationProblemDetails:
    title: Optional[str]
    errors: Optional[Dict[str, List[str]]]
    type: Union[Unset, None, str] = UNSET
    status: Union[Unset, None, int] = UNSET
    detail: Union[Unset, None, str] = UNSET
    instance: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        title = self.title
        status = self.status
        detail = self.detail
        instance = self.instance
        errors = self.errors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "errors": errors,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

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
