from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar

import attr

from binarylane.models.change_threshold_alerts_type import ChangeThresholdAlertsType
from binarylane.models.threshold_alert_request import ThresholdAlertRequest

T = TypeVar("T", bound="ChangeThresholdAlerts")


@attr.s(auto_attribs=True)
class ChangeThresholdAlerts:
    """Set or Update the Threshold Alerts for a Server

    Attributes:
        type (ChangeThresholdAlertsType):
        threshold_alerts (List[ThresholdAlertRequest]): Any alert type not listed will not be updated.
    """

    type: ChangeThresholdAlertsType
    threshold_alerts: List[ThresholdAlertRequest]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        threshold_alerts = []
        for threshold_alerts_item_data in self.threshold_alerts:
            threshold_alerts_item = threshold_alerts_item_data.to_dict()

            threshold_alerts.append(threshold_alerts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "threshold_alerts": threshold_alerts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeThresholdAlertsType(d.pop("type"))

        threshold_alerts = []
        _threshold_alerts = d.pop("threshold_alerts")
        for threshold_alerts_item_data in _threshold_alerts:
            threshold_alerts_item = ThresholdAlertRequest.from_dict(threshold_alerts_item_data)

            threshold_alerts.append(threshold_alerts_item)

        change_threshold_alerts = cls(
            type=type,
            threshold_alerts=threshold_alerts,
        )

        change_threshold_alerts.additional_properties = d
        return change_threshold_alerts

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
