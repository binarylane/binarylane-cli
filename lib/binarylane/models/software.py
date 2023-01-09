from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Software")


@attr.s(auto_attribs=True)
class Software:
    """
    Attributes:
        id (str): The ID of this software.
        enabled (bool): Software that is not enabled is not available to be added to servers but may be retained by
            servers that currently use it.
        name (str): The name of this software.
        description (str): The description of this software.
        cost_per_licence_per_month (float): The cost for each licence of this software per month in AU$.
        minimum_licence_count (int): The minimum licences permitted for this software.
        maximum_licence_count (int): The maximum licences permitted for this software.
        licence_step_count (int): Licences must be purchased in multiples of this value.
        supported_operating_systems (List[str]): A list of slugs of operating system images that support this software.
        group (Union[Unset, None, str]): Software in the same group may not be licensed together.
    """

    id: str
    enabled: bool
    name: str
    description: str
    cost_per_licence_per_month: float
    minimum_licence_count: int
    maximum_licence_count: int
    licence_step_count: int
    supported_operating_systems: List[str]
    group: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        enabled = self.enabled
        name = self.name
        description = self.description
        cost_per_licence_per_month = self.cost_per_licence_per_month
        minimum_licence_count = self.minimum_licence_count
        maximum_licence_count = self.maximum_licence_count
        licence_step_count = self.licence_step_count
        supported_operating_systems = self.supported_operating_systems

        group = self.group

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "enabled": enabled,
                "name": name,
                "description": description,
                "cost_per_licence_per_month": cost_per_licence_per_month,
                "minimum_licence_count": minimum_licence_count,
                "maximum_licence_count": maximum_licence_count,
                "licence_step_count": licence_step_count,
                "supported_operating_systems": supported_operating_systems,
            }
        )
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        enabled = d.pop("enabled")

        name = d.pop("name")

        description = d.pop("description")

        cost_per_licence_per_month = d.pop("cost_per_licence_per_month")

        minimum_licence_count = d.pop("minimum_licence_count")

        maximum_licence_count = d.pop("maximum_licence_count")

        licence_step_count = d.pop("licence_step_count")

        supported_operating_systems = cast(List[str], d.pop("supported_operating_systems"))

        group = d.pop("group", UNSET)

        software = cls(
            id=id,
            enabled=enabled,
            name=name,
            description=description,
            cost_per_licence_per_month=cost_per_licence_per_month,
            minimum_licence_count=minimum_licence_count,
            maximum_licence_count=maximum_licence_count,
            licence_step_count=licence_step_count,
            supported_operating_systems=supported_operating_systems,
            group=group,
        )

        software.additional_properties = d
        return software

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
