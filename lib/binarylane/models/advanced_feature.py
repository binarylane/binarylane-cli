from __future__ import annotations

from enum import Enum


class AdvancedFeature(str, Enum):
    EMULATED_HYPERV = "emulated-hyperv"
    EMULATED_DEVICES = "emulated-devices"
    NESTED_VIRT = "nested-virt"
    DRIVER_DISK = "driver-disk"
    UNSET_UUID = "unset-uuid"
    LOCAL_RTC = "local-rtc"
    EMULATED_TPM = "emulated-tpm"
    CLOUD_INIT = "cloud-init"
    QEMU_GUEST_AGENT = "qemu-guest-agent"
    UEFI_BOOT = "uefi-boot"

    def __str__(self) -> str:
        return str(self.value)
