from enum import Enum


class AdvancedFeature(str, Enum):
    HYPER_V_SUPPORT = "hyper-v-support"
    EMULATED_DEVICES = "emulated-devices"
    NESTED_VIRTUALIZATION = "nested-virtualization"
    DRIVER_DISK_ATTACHED = "driver-disk-attached"
    DISABLE_BIOS_UUID = "disable-bios-uuid"
    LOCAL_TIME_REAL_TIME_CLOCK = "local-time-real-time-clock"
    TRUSTED_PLATFORM_MODULE = "trusted-platform-module"
    CLOUD_INIT_DATA_SOURCE = "cloud-init-data-source"
    GUEST_AGENT = "guest-agent"
    UEFI = "uefi"

    def __str__(self) -> str:
        return str(self.value)
