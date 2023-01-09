from __future__ import annotations

from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr

from binarylane.models.validation_problem_details_errors import ValidationProblemDetailsErrors
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ValidationProblemDetails")


@attr.s(auto_attribs=True)
class ValidationProblemDetails:
    """
    Attributes:
        type (Union[Unset, None, str]):
        title (Optional[str]):
        status (Union[Unset, None, int]):
        detail (Union[Unset, None, str]):
        instance (Union[Unset, None, str]):
        errors (Optional[ValidationProblemDetailsErrors]):
    """

    title: Optional[str]
    errors: Optional[ValidationProblemDetailsErrors]
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
        errors = self.errors.to_dict() if self.errors else None

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

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type", UNSET)

        title = d.pop("title")

        status = d.pop("status", UNSET)

        detail = d.pop("detail", UNSET)

        instance = d.pop("instance", UNSET)

        _errors = d.pop("errors")
        errors: Optional[ValidationProblemDetailsErrors]
        if _errors is None:
            errors = None
        else:
            errors = ValidationProblemDetailsErrors.from_dict(_errors)

        validation_problem_details = cls(
            type=type,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            errors=errors,
        )

        validation_problem_details.additional_properties = d
        return validation_problem_details

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
