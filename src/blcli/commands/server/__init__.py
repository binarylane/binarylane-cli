""" Contains methods for accessing server endpoints """
from __future__ import annotations

from typing import List, Type

from ...runner import ModuleRunner, Runner

__all__ = ["commands"]
commands: List[Type[Runner]] = []


def register_command(cls):
    commands.append(cls)
    return cls


@register_command
class ServerDataUsageGet(ModuleRunner):
    """Runner for server_data-usage_get API operation"""

    @property
    def name(self) -> str:
        return "data-usage_get"

    @property
    def description(self) -> str:
        return "Fetch the Current Data Usage (Transfer) for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_data_usage_get"


@register_command
class ServerDataUsageList(ModuleRunner):
    """Runner for server_data-usage_list API operation"""

    @property
    def name(self) -> str:
        return "data-usage_list"

    @property
    def description(self) -> str:
        return "Fetch all Current Data Usage (Transfer) for All Servers"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_data_usage_list"


@register_command
class ServerFailoverIpGet(ModuleRunner):
    """Runner for server_failover-ip_get API operation"""

    @property
    def name(self) -> str:
        return "failover-ip_get"

    @property
    def description(self) -> str:
        return "Fetch the Failover IPs for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_failover_ip_get"


@register_command
class ServerFailoverIpUpdate(ModuleRunner):
    """Runner for server_failover-ip_update API operation"""

    @property
    def name(self) -> str:
        return "failover-ip_update"

    @property
    def description(self) -> str:
        return "Sets the List of Failover IPs that are Assigned to a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_failover_ip_update"


@register_command
class ServerFailoverIpAvailable(ModuleRunner):
    """Runner for server_failover-ip_available API operation"""

    @property
    def name(self) -> str:
        return "failover-ip_available"

    @property
    def description(self) -> str:
        return "Fetch a List of all Failover IPs that are Available to be Assigned to a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_failover_ip_available"


@register_command
class ServerIpv6PtrNsList(ModuleRunner):
    """Runner for server_ipv6-ptr-ns_list API operation"""

    @property
    def name(self) -> str:
        return "ipv6-ptr-ns_list"

    @property
    def description(self) -> str:
        return "Fetch all Existing IPv6 Name Server Records"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_ipv6_ptr_ns_list"


@register_command
class ServerIpv6PtrNsUpdate(ModuleRunner):
    """Runner for server_ipv6-ptr-ns_update API operation"""

    @property
    def name(self) -> str:
        return "ipv6-ptr-ns_update"

    @property
    def description(self) -> str:
        return "Create New or Update Existing IPv6 Name Server Records"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_ipv6_ptr_ns_update"


@register_command
class ServerMetricsGet(ModuleRunner):
    """Runner for server_metrics_get API operation"""

    @property
    def name(self) -> str:
        return "metrics_get"

    @property
    def description(self) -> str:
        return "Fetch the Latest Performance and Usage Data Sample Set for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_metrics_get"


@register_command
class ServerMetricsList(ModuleRunner):
    """Runner for server_metrics_list API operation"""

    @property
    def name(self) -> str:
        return "metrics_list"

    @property
    def description(self) -> str:
        return "Fetch all of the Performance and Usage Data Sample Sets for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_metrics_list"


@register_command
class ServerActionList(ModuleRunner):
    """Runner for server_action_list API operation"""

    @property
    def name(self) -> str:
        return "action_list"

    @property
    def description(self) -> str:
        return "List All Actions for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_action_list"


@register_command
class ServerActionCreate(ModuleRunner):
    """Runner for server_action_create API operation"""

    @property
    def name(self) -> str:
        return "action_create"

    @property
    def description(self) -> str:
        return "Perform an Action on a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_action_create"


@register_command
class ServerTaggedAction(ModuleRunner):
    """Runner for server_tagged-action API operation"""

    @property
    def name(self) -> str:
        return "tagged-action"

    @property
    def description(self) -> str:
        return "Perform an Action on Servers by Tag"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_tagged_action"


@register_command
class ServerGet(ModuleRunner):
    """Runner for server_get API operation"""

    @property
    def name(self) -> str:
        return "get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_get"


@register_command
class ServerDelete(ModuleRunner):
    """Runner for server_delete API operation"""

    @property
    def name(self) -> str:
        return "delete"

    @property
    def description(self) -> str:
        return "Cancel an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_delete"


@register_command
class ServerList(ModuleRunner):
    """Runner for server_list API operation"""

    @property
    def name(self) -> str:
        return "list"

    @property
    def description(self) -> str:
        return "List All Servers"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_list"


@register_command
class ServerCreate(ModuleRunner):
    """Runner for server_create API operation"""

    @property
    def name(self) -> str:
        return "create"

    @property
    def description(self) -> str:
        return "Create a New Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_create"


@register_command
class ServerTaggedDelete(ModuleRunner):
    """Runner for server_tagged_delete API operation"""

    @property
    def name(self) -> str:
        return "tagged_delete"

    @property
    def description(self) -> str:
        return "Cancel Existing Servers by Tag"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_tagged_delete"


@register_command
class ServerActionGet(ModuleRunner):
    """Runner for server_action_get API operation"""

    @property
    def name(self) -> str:
        return "action_get"

    @property
    def description(self) -> str:
        return "Fetch an Action for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_action_get"


@register_command
class ServerFirewallList(ModuleRunner):
    """Runner for server_firewall_list API operation"""

    @property
    def name(self) -> str:
        return "firewall_list"

    @property
    def description(self) -> str:
        return "Fetch All Advanced Firewall Rules for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_firewall_list"


@register_command
class ServerFeatureList(ModuleRunner):
    """Runner for server_feature_list API operation"""

    @property
    def name(self) -> str:
        return "feature_list"

    @property
    def description(self) -> str:
        return "Fetch the Currently Available Advanced Features for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_feature_list"


@register_command
class ServerBackupList(ModuleRunner):
    """Runner for server_backup_list API operation"""

    @property
    def name(self) -> str:
        return "backup_list"

    @property
    def description(self) -> str:
        return "List All Backups for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_backup_list"


@register_command
class ServerBackupUpload(ModuleRunner):
    """Runner for server_backup_upload API operation"""

    @property
    def name(self) -> str:
        return "backup_upload"

    @property
    def description(self) -> str:
        return "Upload a Backup for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_backup_upload"


@register_command
class ServerKernelList(ModuleRunner):
    """Runner for server_kernel_list API operation"""

    @property
    def name(self) -> str:
        return "kernel_list"

    @property
    def description(self) -> str:
        return "List all Available Kernels for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_kernel_list"


@register_command
class ServerNeighborsGet(ModuleRunner):
    """Runner for server_neighbors_get API operation"""

    @property
    def name(self) -> str:
        return "neighbors_get"

    @property
    def description(self) -> str:
        return "List All Servers That Share a Host with a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_neighbors_get"


@register_command
class ServerNeighborsList(ModuleRunner):
    """Runner for server_neighbors_list API operation"""

    @property
    def name(self) -> str:
        return "neighbors_list"

    @property
    def description(self) -> str:
        return "List All Servers That Share a Host"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_neighbors_list"


@register_command
class ServerSnapshotList(ModuleRunner):
    """Runner for server_snapshot_list API operation"""

    @property
    def name(self) -> str:
        return "snapshot_list"

    @property
    def description(self) -> str:
        return "List all Snapshots for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_snapshot_list"


@register_command
class ServerAlertGet(ModuleRunner):
    """Runner for server_alert_get API operation"""

    @property
    def name(self) -> str:
        return "alert_get"

    @property
    def description(self) -> str:
        return "Fetch the Currently Set Threshold Alerts for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_alert_get"


@register_command
class ServerAlertList(ModuleRunner):
    """Runner for server_alert_list API operation"""

    @property
    def name(self) -> str:
        return "alert_list"

    @property
    def description(self) -> str:
        return "List any Servers that have a Current Exceeded Threshold Alert"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_alert_list"


@register_command
class ServerSoftware(ModuleRunner):
    """Runner for server_software API operation"""

    @property
    def name(self) -> str:
        return "software"

    @property
    def description(self) -> str:
        return "List all Enabled Software for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_software"


@register_command
class ServerUserData(ModuleRunner):
    """Runner for server_user-data API operation"""

    @property
    def name(self) -> str:
        return "user-data"

    @property
    def description(self) -> str:
        return "Fetch the Currently Set UserData for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server.server_user_data"
