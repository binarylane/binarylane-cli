from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="Region")


@attr.s(auto_attribs=True)
class Region:
    """
    Attributes:
        slug (str): The unique slug for this region.
        name (str): The name of this region.
        sizes (List[str]): The slugs of the sizes available in this region.
        available (bool): Whether this region is available for the allocation of new resources.
        features (List[str]): A list of features available for resources in this region.
        name_servers (List[str]): A list of nameservers available for resources in this region.
    """

    slug: str
    name: str
    sizes: List[str]
    available: bool
    features: List[str]
    name_servers: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug
        name = self.name
        sizes = self.sizes

        available = self.available
        features = self.features

        name_servers = self.name_servers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
                "name": name,
                "sizes": sizes,
                "available": available,
                "features": features,
                "name_servers": name_servers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slug = d.pop("slug")

        name = d.pop("name")

        sizes = cast(List[str], d.pop("sizes"))

        available = d.pop("available")

        features = cast(List[str], d.pop("features"))

        name_servers = cast(List[str], d.pop("name_servers"))

        region = cls(
            slug=slug,
            name=name,
            sizes=sizes,
            available=available,
            features=features,
            name_servers=name_servers,
        )

        region.additional_properties = d
        return region

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
