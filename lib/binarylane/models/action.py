from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from binarylane.models.action_progress import ActionProgress
from binarylane.models.action_status import ActionStatus
from binarylane.models.region import Region
from binarylane.models.resource_type import ResourceType
from binarylane.models.user_interaction_required import UserInteractionRequired
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Action")


@attr.s(auto_attribs=True)
class Action:
    """
    Attributes:
        id (int): The ID of this action.
        status (ActionStatus):
            | Value | Description |
            | ----- | ----------- |
            | in-progress | This action is currently in progress. |
            | completed | This action has successfully completed. |
            | errored | An error was encountered while processing the action. |

        type (str): The type of this action.
        started_at (datetime.datetime): The timestamp in ISO8601 format of when processing of this action started.
        progress (ActionProgress): Information about the current progress of the action. Some actions are divided into
            'steps' and this may also contain information about the current and completed steps.
        completed_at (Union[Unset, None, datetime.datetime]): The timestamp in ISO8601 format of when processing of this
            action completed. If this value is null the action is currently in progress.
        resource_type (Union[Unset, None, ResourceType]): The resource type (if any) associated with this action. The
            resource type also determines which (if any) of the resource_id or resource_uuid fields are populated.
        resource_id (Union[Unset, None, int]): The resource id of the resource (if any) associated with this action.
            This is only populated when the resource type has an integer identifier.
        resource_uuid (Union[Unset, None, str]): The resource id of the resource (if any) associated with this action.
            This is only populated when the resource type has a UUID identifier.
        region (Union[Unset, None, Region]): The region (if any) of the resource associated with this action.
        region_slug (Union[Unset, None, str]): The region slug (if any) of the resource associated with this action.
        result_data (Union[Unset, None, str]): Returned information from a completed action. For example: a successful
            completed 'ping' action will have the ping value in ms in this field.
        blocking_invoice_id (Union[Unset, None, str]): If this Action is currently blocked by an invoice that requires
            payment this property will be set.
        user_interaction_required (Union[Unset, None, UserInteractionRequired]): If this is not null the action is
            waiting on a response from the user.
    """

    id: int
    status: ActionStatus
    type: str
    started_at: datetime.datetime
    progress: ActionProgress
    completed_at: Union[Unset, None, datetime.datetime] = UNSET
    resource_type: Union[Unset, None, ResourceType] = UNSET
    resource_id: Union[Unset, None, int] = UNSET
    resource_uuid: Union[Unset, None, str] = UNSET
    region: Union[Unset, None, Region] = UNSET
    region_slug: Union[Unset, None, str] = UNSET
    result_data: Union[Unset, None, str] = UNSET
    blocking_invoice_id: Union[Unset, None, str] = UNSET
    user_interaction_required: Union[Unset, None, UserInteractionRequired] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status = self.status.value

        type = self.type
        started_at = self.started_at.isoformat()

        progress = self.progress.to_dict()

        completed_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat() if self.completed_at else None

        resource_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.resource_type, Unset):
            resource_type = self.resource_type.value if self.resource_type else None

        resource_id = self.resource_id
        resource_uuid = self.resource_uuid
        region: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.to_dict() if self.region else None

        region_slug = self.region_slug
        result_data = self.result_data
        blocking_invoice_id = self.blocking_invoice_id
        user_interaction_required: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.user_interaction_required, Unset):
            user_interaction_required = (
                self.user_interaction_required.to_dict() if self.user_interaction_required else None
            )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "type": type,
                "started_at": started_at,
                "progress": progress,
            }
        )
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_uuid is not UNSET:
            field_dict["resource_uuid"] = resource_uuid
        if region is not UNSET:
            field_dict["region"] = region
        if region_slug is not UNSET:
            field_dict["region_slug"] = region_slug
        if result_data is not UNSET:
            field_dict["result_data"] = result_data
        if blocking_invoice_id is not UNSET:
            field_dict["blocking_invoice_id"] = blocking_invoice_id
        if user_interaction_required is not UNSET:
            field_dict["user_interaction_required"] = user_interaction_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        status = ActionStatus(d.pop("status"))

        type = d.pop("type")

        started_at = isoparse(d.pop("started_at"))

        progress = ActionProgress.from_dict(d.pop("progress"))

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, None, datetime.datetime]
        if _completed_at is None:
            completed_at = None
        elif isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        _resource_type = d.pop("resource_type", UNSET)
        resource_type: Union[Unset, None, ResourceType]
        if _resource_type is None:
            resource_type = None
        elif isinstance(_resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = ResourceType(_resource_type)

        resource_id = d.pop("resource_id", UNSET)

        resource_uuid = d.pop("resource_uuid", UNSET)

        _region = d.pop("region", UNSET)
        region: Union[Unset, None, Region]
        if _region is None:
            region = None
        elif isinstance(_region, Unset):
            region = UNSET
        else:
            region = Region.from_dict(_region)

        region_slug = d.pop("region_slug", UNSET)

        result_data = d.pop("result_data", UNSET)

        blocking_invoice_id = d.pop("blocking_invoice_id", UNSET)

        _user_interaction_required = d.pop("user_interaction_required", UNSET)
        user_interaction_required: Union[Unset, None, UserInteractionRequired]
        if _user_interaction_required is None:
            user_interaction_required = None
        elif isinstance(_user_interaction_required, Unset):
            user_interaction_required = UNSET
        else:
            user_interaction_required = UserInteractionRequired.from_dict(_user_interaction_required)

        action = cls(
            id=id,
            status=status,
            type=type,
            started_at=started_at,
            progress=progress,
            completed_at=completed_at,
            resource_type=resource_type,
            resource_id=resource_id,
            resource_uuid=resource_uuid,
            region=region,
            region_slug=region_slug,
            result_data=result_data,
            blocking_invoice_id=blocking_invoice_id,
            user_interaction_required=user_interaction_required,
        )

        action.additional_properties = d
        return action

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
