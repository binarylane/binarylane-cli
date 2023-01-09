from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ActionProgress")


@attr.s(auto_attribs=True)
class ActionProgress:
    """
    Attributes:
        percent_complete (int): An estimation of the overall completion of the action.
        completed_steps (List[str]): A list of the completed action steps.
        current_step_detail (Union[Unset, None, str]): Detail about the progress of the current step of the action. For
            example, when creating an offsite backup this may be populated with the current upload speed and completion ETA
            of the upload step.
        current_step (Union[Unset, None, str]): An description of the current action step.
    """

    percent_complete: int
    completed_steps: List[str]
    current_step_detail: Union[Unset, None, str] = UNSET
    current_step: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        percent_complete = self.percent_complete
        completed_steps = self.completed_steps

        current_step_detail = self.current_step_detail
        current_step = self.current_step

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "percent_complete": percent_complete,
                "completed_steps": completed_steps,
            }
        )
        if current_step_detail is not UNSET:
            field_dict["current_step_detail"] = current_step_detail
        if current_step is not UNSET:
            field_dict["current_step"] = current_step

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        percent_complete = d.pop("percent_complete")

        completed_steps = cast(List[str], d.pop("completed_steps"))

        current_step_detail = d.pop("current_step_detail", UNSET)

        current_step = d.pop("current_step", UNSET)

        action_progress = cls(
            percent_complete=percent_complete,
            completed_steps=completed_steps,
            current_step_detail=current_step_detail,
            current_step=current_step,
        )

        action_progress.additional_properties = d
        return action_progress

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
