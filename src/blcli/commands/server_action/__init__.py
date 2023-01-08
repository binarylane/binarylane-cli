""" Contains methods for accessing server_action endpoints """
from __future__ import annotations

from typing import List, Type

from ...runners import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: ModuleRunner) -> ModuleRunner:
    commands.append(cls)
    return cls


@register_command
class ServerActionChangeThresholdAlerts(ModuleRunner):
    """Runner for server-action_change-threshold-alerts API operation"""

    @property
    def name(self) -> str:
        return "change-threshold-alerts"

    @property
    def description(self) -> str:
        return "Set or Update the Threshold Alerts for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_threshold_alerts"


@register_command
class ServerActionIsRunning(ModuleRunner):
    """Runner for server-action_is-running API operation"""

    @property
    def name(self) -> str:
        return "is-running"

    @property
    def description(self) -> str:
        return "Check if a Server is Running"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_is_running"


@register_command
class ServerActionPing(ModuleRunner):
    """Runner for server-action_ping API operation"""

    @property
    def name(self) -> str:
        return "ping"

    @property
    def description(self) -> str:
        return "Attempt to Ping a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_ping"


@register_command
class ServerActionUncancel(ModuleRunner):
    """Runner for server-action_uncancel API operation"""

    @property
    def name(self) -> str:
        return "uncancel"

    @property
    def description(self) -> str:
        return "Revert the Cancellation of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_uncancel"


@register_command
class ServerActionUptime(ModuleRunner):
    """Runner for server-action_uptime API operation"""

    @property
    def name(self) -> str:
        return "uptime"

    @property
    def description(self) -> str:
        return "Check the Uptime of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_uptime"


@register_command
class ServerActionAttachBackup(ModuleRunner):
    """Runner for server-action_attach-backup API operation"""

    @property
    def name(self) -> str:
        return "attach-backup"

    @property
    def description(self) -> str:
        return "Attach a Backup to a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_attach_backup"


@register_command
class ServerActionChangeBackupSchedule(ModuleRunner):
    """Runner for server-action_change-backup-schedule API operation"""

    @property
    def name(self) -> str:
        return "change-backup-schedule"

    @property
    def description(self) -> str:
        return "Change the Backup Schedule of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_backup_schedule"


@register_command
class ServerActionChangeManageOffsiteBackupCopies(ModuleRunner):
    """Runner for server-action_change-manage-offsite-backup-copies API operation"""

    @property
    def name(self) -> str:
        return "change-manage-offsite-backup-copies"

    @property
    def description(self) -> str:
        return "Change the Management of Offsite Backup Copies"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_manage_offsite_backup_copies"


@register_command
class ServerActionChangeOffsiteBackupLocation(ModuleRunner):
    """Runner for server-action_change-offsite-backup-location API operation"""

    @property
    def name(self) -> str:
        return "change-offsite-backup-location"

    @property
    def description(self) -> str:
        return "Change the Offsite Backup Location of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_offsite_backup_location"


@register_command
class ServerActionCloneUsingBackup(ModuleRunner):
    """Runner for server-action_clone-using-backup API operation"""

    @property
    def name(self) -> str:
        return "clone-using-backup"

    @property
    def description(self) -> str:
        return "Restore a Backup of a Server to a Different Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_clone_using_backup"


@register_command
class ServerActionDetachBackup(ModuleRunner):
    """Runner for server-action_detach-backup API operation"""

    @property
    def name(self) -> str:
        return "detach-backup"

    @property
    def description(self) -> str:
        return "Detach Any Attached Backup from a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_detach_backup"


@register_command
class ServerActionDisableBackups(ModuleRunner):
    """Runner for server-action_disable-backups API operation"""

    @property
    def name(self) -> str:
        return "disable-backups"

    @property
    def description(self) -> str:
        return "Disable Backups for an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_disable_backups"


@register_command
class ServerActionEnableBackups(ModuleRunner):
    """Runner for server-action_enable-backups API operation"""

    @property
    def name(self) -> str:
        return "enable-backups"

    @property
    def description(self) -> str:
        return "Enable Two Daily Backups for an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_enable_backups"


@register_command
class ServerActionRestore(ModuleRunner):
    """Runner for server-action_restore API operation"""

    @property
    def name(self) -> str:
        return "restore"

    @property
    def description(self) -> str:
        return "Restore a Backup to a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_restore"


@register_command
class ServerActionTakeBackup(ModuleRunner):
    """Runner for server-action_take-backup API operation"""

    @property
    def name(self) -> str:
        return "take-backup"

    @property
    def description(self) -> str:
        return "Take a Backup of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_take_backup"


@register_command
class ServerActionPasswordReset(ModuleRunner):
    """Runner for server-action_password-reset API operation"""

    @property
    def name(self) -> str:
        return "password-reset"

    @property
    def description(self) -> str:
        return "Reset the Password of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_password_reset"


@register_command
class ServerActionPowerCycle(ModuleRunner):
    """Runner for server-action_power-cycle API operation"""

    @property
    def name(self) -> str:
        return "power-cycle"

    @property
    def description(self) -> str:
        return "Power a Server Off and then On"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_power_cycle"


@register_command
class ServerActionPowerOff(ModuleRunner):
    """Runner for server-action_power-off API operation"""

    @property
    def name(self) -> str:
        return "power-off"

    @property
    def description(self) -> str:
        return "Power a Server Off"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_power_off"


@register_command
class ServerActionPowerOn(ModuleRunner):
    """Runner for server-action_power-on API operation"""

    @property
    def name(self) -> str:
        return "power-on"

    @property
    def description(self) -> str:
        return "Power a Server On"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_power_on"


@register_command
class ServerActionReboot(ModuleRunner):
    """Runner for server-action_reboot API operation"""

    @property
    def name(self) -> str:
        return "reboot"

    @property
    def description(self) -> str:
        return "Request a Server Perform a Reboot"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_reboot"


@register_command
class ServerActionShutdown(ModuleRunner):
    """Runner for server-action_shutdown API operation"""

    @property
    def name(self) -> str:
        return "shutdown"

    @property
    def description(self) -> str:
        return "Request a Server Perform a Shutdown"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_shutdown"


@register_command
class ServerActionChangeAdvancedFeatures(ModuleRunner):
    """Runner for server-action_change-advanced-features API operation"""

    @property
    def name(self) -> str:
        return "change-advanced-features"

    @property
    def description(self) -> str:
        return "Change the Advanced Features of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_advanced_features"


@register_command
class ServerActionChangeAdvancedFirewallRules(ModuleRunner):
    """Runner for server-action_change-advanced-firewall-rules API operation"""

    @property
    def name(self) -> str:
        return "change-advanced-firewall-rules"

    @property
    def description(self) -> str:
        return "Change the Advanced Firewall Rules for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_advanced_firewall_rules"


@register_command
class ServerActionChangeKernel(ModuleRunner):
    """Runner for server-action_change-kernel API operation"""

    @property
    def name(self) -> str:
        return "change-kernel"

    @property
    def description(self) -> str:
        return "Change the Kernel of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_kernel"


@register_command
class ServerActionChangePartner(ModuleRunner):
    """Runner for server-action_change-partner API operation"""

    @property
    def name(self) -> str:
        return "change-partner"

    @property
    def description(self) -> str:
        return "Add, Update or Remove a Partner Server for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_partner"


@register_command
class ServerActionDisableSelinux(ModuleRunner):
    """Runner for server-action_disable-selinux API operation"""

    @property
    def name(self) -> str:
        return "disable-selinux"

    @property
    def description(self) -> str:
        return "Disable SE Linux for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_disable_selinux"


@register_command
class ServerActionRebuild(ModuleRunner):
    """Runner for server-action_rebuild API operation"""

    @property
    def name(self) -> str:
        return "rebuild"

    @property
    def description(self) -> str:
        return "Rebuild an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_rebuild"


@register_command
class ServerActionResize(ModuleRunner):
    """Runner for server-action_resize API operation"""

    @property
    def name(self) -> str:
        return "resize"

    @property
    def description(self) -> str:
        return "Update the Size and Related Options for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_resize"


@register_command
class ServerActionAddDisk(ModuleRunner):
    """Runner for server-action_add-disk API operation"""

    @property
    def name(self) -> str:
        return "add-disk"

    @property
    def description(self) -> str:
        return "Create an Additional Disk for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_add_disk"


@register_command
class ServerActionResizeDisk(ModuleRunner):
    """Runner for server-action_resize-disk API operation"""

    @property
    def name(self) -> str:
        return "resize-disk"

    @property
    def description(self) -> str:
        return "Alter the Size of an Existing Disk for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_resize_disk"


@register_command
class ServerActionDeleteDisk(ModuleRunner):
    """Runner for server-action_delete-disk API operation"""

    @property
    def name(self) -> str:
        return "delete-disk"

    @property
    def description(self) -> str:
        return "Delete an Additional Disk for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_delete_disk"


@register_command
class ServerActionChangeIpv6ReverseNameservers(ModuleRunner):
    """Runner for server-action_change-ipv6-reverse-nameservers API operation"""

    @property
    def name(self) -> str:
        return "change-ipv6-reverse-nameservers"

    @property
    def description(self) -> str:
        return "Update the IPv6 Reverse Name Servers for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_ipv6_reverse_nameservers"


@register_command
class ServerActionChangeReverseName(ModuleRunner):
    """Runner for server-action_change-reverse-name API operation"""

    @property
    def name(self) -> str:
        return "change-reverse-name"

    @property
    def description(self) -> str:
        return "Change the Reverse Name for an IPv4 Address on a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_reverse_name"


@register_command
class ServerActionRename(ModuleRunner):
    """Runner for server-action_rename API operation"""

    @property
    def name(self) -> str:
        return "rename"

    @property
    def description(self) -> str:
        return "Rename a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_rename"


@register_command
class ServerActionChangeIpv6(ModuleRunner):
    """Runner for server-action_change-ipv6 API operation"""

    @property
    def name(self) -> str:
        return "change-ipv6"

    @property
    def description(self) -> str:
        return "Enable or Disable IPv6 for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_ipv6"


@register_command
class ServerActionChangePortBlocking(ModuleRunner):
    """Runner for server-action_change-port-blocking API operation"""

    @property
    def name(self) -> str:
        return "change-port-blocking"

    @property
    def description(self) -> str:
        return "Change the Port Blocking for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_port_blocking"


@register_command
class ServerActionEnableIpv6(ModuleRunner):
    """Runner for server-action_enable-ipv6 API operation"""

    @property
    def name(self) -> str:
        return "enable-ipv6"

    @property
    def description(self) -> str:
        return "Enable IPv6 for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_enable_ipv6"


@register_command
class ServerActionChangeNetwork(ModuleRunner):
    """Runner for server-action_change-network API operation"""

    @property
    def name(self) -> str:
        return "change-network"

    @property
    def description(self) -> str:
        return "Move a Server to an Existing Network"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_network"


@register_command
class ServerActionChangeSeparatePrivateNetworkInterface(ModuleRunner):
    """Runner for server-action_change-separate-private-network-interface API operation"""

    @property
    def name(self) -> str:
        return "change-separate-private-network-interface"

    @property
    def description(self) -> str:
        return "Enable or Disable a Separate Private Network Interface for a Server in a VPC"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_separate_private_network_interface"


@register_command
class ServerActionChangeSourceAndDestinationCheck(ModuleRunner):
    """Runner for server-action_change-source-and-destination-check API operation"""

    @property
    def name(self) -> str:
        return "change-source-and-destination-check"

    @property
    def description(self) -> str:
        return "Enable or Disable Network Source and Destination Checks for a Server in a VPC"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_source_and_destination_check"


@register_command
class ServerActionChangeVpcIpv4(ModuleRunner):
    """Runner for server-action_change-vpc-ipv4 API operation"""

    @property
    def name(self) -> str:
        return "change-vpc-ipv4"

    @property
    def description(self) -> str:
        return "Change the IPv4 Address for a Server in a VPC"

    @property
    def module_path(self) -> str:
        return ".commands.server_action.server_action_change_vpc_ipv4"
