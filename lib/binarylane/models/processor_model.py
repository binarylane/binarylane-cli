from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ProcessorModel")


@attr.s(auto_attribs=True)
class ProcessorModel:
    """
    Attributes:
        id (int): The ID of this processor model.
        name (str): The name of this processor model.
        description (Union[Unset, None, str]): A description of this processor model.
    """

    id: int
    name: str
    description: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        processor_model = cls(
            id=id,
            name=name,
            description=description,
        )

        processor_model.additional_properties = d
        return processor_model

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
