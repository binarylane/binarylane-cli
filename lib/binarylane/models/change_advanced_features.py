from __future__ import annotations

from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from binarylane.models.advanced_feature import AdvancedFeature
from binarylane.models.change_advanced_features_type import ChangeAdvancedFeaturesType
from binarylane.models.video_device import VideoDevice
from binarylane.models.vm_machine_type import VmMachineType
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="ChangeAdvancedFeatures")


@attr.s(auto_attribs=True)
class ChangeAdvancedFeatures:
    """Change the Advanced Features of a Server

    Attributes:
        type (ChangeAdvancedFeaturesType):
        enabled_advanced_features (Union[Unset, None, List[AdvancedFeature]]): Do not provide or set to null to keep
            existing advanced features. Provide an empty array to disable all advanced features, otherwise provide an array
            with selected advanced features. If provided, any currently enabled advanced features that aren't included will
            be disabled.
        processor_model (Union[Unset, None, str]): Do not provide or set to null to keep existing processor model.
        automatic_processor_model (Union[Unset, None, bool]): Set to true to use best available processor model. If this
            is provided the processor_model property must not be provided.
        machine_type (Union[Unset, None, VmMachineType]): Do not provide or set to null to keep existing machine type.
        automatic_machine_type (Union[Unset, None, bool]): Set to true to use best available machine type. If this is
            provided the machine_type property must not be provided.
        video_device (Union[Unset, None, VideoDevice]): Do not provide or set to null to keep existing video device.
    """

    type: ChangeAdvancedFeaturesType
    enabled_advanced_features: Union[Unset, None, List[AdvancedFeature]] = UNSET
    processor_model: Union[Unset, None, str] = UNSET
    automatic_processor_model: Union[Unset, None, bool] = UNSET
    machine_type: Union[Unset, None, VmMachineType] = UNSET
    automatic_machine_type: Union[Unset, None, bool] = UNSET
    video_device: Union[Unset, None, VideoDevice] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        enabled_advanced_features: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.enabled_advanced_features, Unset):
            if self.enabled_advanced_features is None:
                enabled_advanced_features = None
            else:
                enabled_advanced_features = []
                for enabled_advanced_features_item_data in self.enabled_advanced_features:
                    enabled_advanced_features_item = enabled_advanced_features_item_data.value

                    enabled_advanced_features.append(enabled_advanced_features_item)

        processor_model = self.processor_model
        automatic_processor_model = self.automatic_processor_model
        machine_type: Union[Unset, None, str] = UNSET
        if not isinstance(self.machine_type, Unset):
            machine_type = self.machine_type.value if self.machine_type else None

        automatic_machine_type = self.automatic_machine_type
        video_device: Union[Unset, None, str] = UNSET
        if not isinstance(self.video_device, Unset):
            video_device = self.video_device.value if self.video_device else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if enabled_advanced_features is not UNSET:
            field_dict["enabled_advanced_features"] = enabled_advanced_features
        if processor_model is not UNSET:
            field_dict["processor_model"] = processor_model
        if automatic_processor_model is not UNSET:
            field_dict["automatic_processor_model"] = automatic_processor_model
        if machine_type is not UNSET:
            field_dict["machine_type"] = machine_type
        if automatic_machine_type is not UNSET:
            field_dict["automatic_machine_type"] = automatic_machine_type
        if video_device is not UNSET:
            field_dict["video_device"] = video_device

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ChangeAdvancedFeaturesType(d.pop("type"))

        enabled_advanced_features = []
        _enabled_advanced_features = d.pop("enabled_advanced_features", UNSET)
        for enabled_advanced_features_item_data in _enabled_advanced_features or []:
            enabled_advanced_features_item = AdvancedFeature(enabled_advanced_features_item_data)

            enabled_advanced_features.append(enabled_advanced_features_item)

        processor_model = d.pop("processor_model", UNSET)

        automatic_processor_model = d.pop("automatic_processor_model", UNSET)

        _machine_type = d.pop("machine_type", UNSET)
        machine_type: Union[Unset, None, VmMachineType]
        if _machine_type is None:
            machine_type = None
        elif isinstance(_machine_type, Unset):
            machine_type = UNSET
        else:
            machine_type = VmMachineType(_machine_type)

        automatic_machine_type = d.pop("automatic_machine_type", UNSET)

        _video_device = d.pop("video_device", UNSET)
        video_device: Union[Unset, None, VideoDevice]
        if _video_device is None:
            video_device = None
        elif isinstance(_video_device, Unset):
            video_device = UNSET
        else:
            video_device = VideoDevice(_video_device)

        change_advanced_features = cls(
            type=type,
            enabled_advanced_features=enabled_advanced_features,
            processor_model=processor_model,
            automatic_processor_model=automatic_processor_model,
            machine_type=machine_type,
            automatic_machine_type=automatic_machine_type,
            video_device=video_device,
        )

        change_advanced_features.additional_properties = d
        return change_advanced_features

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
