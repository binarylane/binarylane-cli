from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.user_interaction_type import UserInteractionType

T = TypeVar("T", bound="UserInteractionRequired")


@attr.s(auto_attribs=True)
class UserInteractionRequired:
    """
    Attributes:
        interaction_type (UserInteractionType):
            | Value | Description |
            | ----- | ----------- |
            | continue-after-ping-failure | Whether we should assume the server creation was successful despite failing to
            ping the server. |
            | allow-unclean-power-off | Whether we are permitted to perform an un-clean power off after the server failed to
            perform a clean shutdown. |

    """

    interaction_type: UserInteractionType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interaction_type = self.interaction_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interaction_type": interaction_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        interaction_type = UserInteractionType(d.pop("interaction_type"))

        user_interaction_required = cls(
            interaction_type=interaction_type,
        )

        user_interaction_required.additional_properties = d
        return user_interaction_required

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
