""" Contains methods for accessing the API """
from __future__ import annotations

import importlib
from typing import List, Type

from binarylane.console.runners.module import ModuleRunner

__all__ = ["commands"]
commands: List[Type[ModuleRunner]] = []


def register_command(cls: Type[ModuleRunner]) -> Type[ModuleRunner]:
    commands.append(cls)
    return cls


@register_command
class GetV2Account(ModuleRunner):
    @property
    def name(self) -> str:
        return "account get"

    @property
    def description(self) -> str:
        return "Fetch Information About the Current Account"

    @property
    def module_path(self) -> str:
        return ".commands.accounts.get_v2_account"


@register_command
class GetV2ActionsActionId(ModuleRunner):
    @property
    def name(self) -> str:
        return "action get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Action"

    @property
    def module_path(self) -> str:
        return ".commands.actions.get_v2_actions_action_id"


@register_command
class GetV2Actions(ModuleRunner):
    @property
    def name(self) -> str:
        return "action list"

    @property
    def description(self) -> str:
        return "List All Actions"

    @property
    def module_path(self) -> str:
        return ".commands.actions.get_v2_actions"


@register_command
class PostV2ActionsActionIdProceed(ModuleRunner):
    @property
    def name(self) -> str:
        return "action proceed"

    @property
    def description(self) -> str:
        return "Respond to a UserInteractionRequired Action"

    @property
    def module_path(self) -> str:
        return ".commands.actions.post_v2_actions_action_id_proceed"


@register_command
class GetV2CustomersMyBalance(ModuleRunner):
    @property
    def name(self) -> str:
        return "account balance"

    @property
    def description(self) -> str:
        return "Fetch Current Balance Information"

    @property
    def module_path(self) -> str:
        return ".commands.customers.get_v2_customers_my_balance"


@register_command
class GetV2CustomersMyInvoicesInvoiceId(ModuleRunner):
    @property
    def name(self) -> str:
        return "account invoice get"

    @property
    def description(self) -> str:
        return "Fetch an Invoice"

    @property
    def module_path(self) -> str:
        return ".commands.customers.get_v2_customers_my_invoices_invoice_id"


@register_command
class GetV2CustomersMyInvoices(ModuleRunner):
    @property
    def name(self) -> str:
        return "account invoice list"

    @property
    def description(self) -> str:
        return "Fetch Invoices"

    @property
    def module_path(self) -> str:
        return ".commands.customers.get_v2_customers_my_invoices"


@register_command
class GetV2CustomersMyUnpaidPaymentFailedInvoices(ModuleRunner):
    @property
    def name(self) -> str:
        return "account invoice overdue"

    @property
    def description(self) -> str:
        return "Fetch Unpaid Failed Invoices"

    @property
    def module_path(self) -> str:
        return ".commands.customers.get_v2_customers_my_unpaid_payment_failed_invoices"


@register_command
class GetV2DataUsagesServerIdCurrent(ModuleRunner):
    @property
    def name(self) -> str:
        return "server data-usage get"

    @property
    def description(self) -> str:
        return "Fetch the Current Data Usage (Transfer) for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.data_usages.get_v2_data_usages_server_id_current"


@register_command
class GetV2DataUsagesCurrent(ModuleRunner):
    @property
    def name(self) -> str:
        return "server data-usage list"

    @property
    def description(self) -> str:
        return "Fetch all Current Data Usage (Transfer) for All Servers"

    @property
    def module_path(self) -> str:
        return ".commands.data_usages.get_v2_data_usages_current"


@register_command
class GetV2DomainsNameservers(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain nameservers list"

    @property
    def description(self) -> str:
        return "List All Public Nameservers"

    @property
    def module_path(self) -> str:
        return ".commands.domains.get_v2_domains_nameservers"


@register_command
class PostV2DomainsRefreshNameserverCache(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain refresh-nameserver-cache"

    @property
    def description(self) -> str:
        return "Refresh Cached Nameserver Domain Records"

    @property
    def module_path(self) -> str:
        return ".commands.domains.post_v2_domains_refresh_nameserver_cache"


@register_command
class GetV2Domains(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain list"

    @property
    def description(self) -> str:
        return "List All Domains"

    @property
    def module_path(self) -> str:
        return ".commands.domains.get_v2_domains"


@register_command
class PostV2Domains(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain create"

    @property
    def description(self) -> str:
        return "Create a New Domain"

    @property
    def module_path(self) -> str:
        return ".commands.domains.post_v2_domains"


@register_command
class GetV2DomainsDomainName(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Domain"

    @property
    def module_path(self) -> str:
        return ".commands.domains.get_v2_domains_domain_name"


@register_command
class DeleteV2DomainsDomainName(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain delete"

    @property
    def description(self) -> str:
        return "Delete an Existing Domain"

    @property
    def module_path(self) -> str:
        return ".commands.domains.delete_v2_domains_domain_name"


@register_command
class GetV2DomainsDomainNameRecords(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain record list"

    @property
    def description(self) -> str:
        return "List All Domain Records for a Domain"

    @property
    def module_path(self) -> str:
        return ".commands.domains.get_v2_domains_domain_name_records"


@register_command
class PostV2DomainsDomainNameRecords(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain record create"

    @property
    def description(self) -> str:
        return "Create a New Domain Record"

    @property
    def module_path(self) -> str:
        return ".commands.domains.post_v2_domains_domain_name_records"


@register_command
class GetV2DomainsDomainNameRecordsRecordId(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain record get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Domain Record"

    @property
    def module_path(self) -> str:
        return ".commands.domains.get_v2_domains_domain_name_records_record_id"


@register_command
class PutV2DomainsDomainNameRecordsRecordId(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain record update"

    @property
    def description(self) -> str:
        return "Update an Existing Domain Record"

    @property
    def module_path(self) -> str:
        return ".commands.domains.put_v2_domains_domain_name_records_record_id"


@register_command
class DeleteV2DomainsDomainNameRecordsRecordId(ModuleRunner):
    @property
    def name(self) -> str:
        return "domain record delete"

    @property
    def description(self) -> str:
        return "Delete an Existing Domain Record"

    @property
    def module_path(self) -> str:
        return ".commands.domains.delete_v2_domains_domain_name_records_record_id"


@register_command
class GetV2FailoverIpsServerId(ModuleRunner):
    @property
    def name(self) -> str:
        return "server failover-ip get"

    @property
    def description(self) -> str:
        return "Fetch the Failover IPs for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.failover_ips.get_v2_failover_ips_server_id"


@register_command
class PostV2FailoverIpsServerId(ModuleRunner):
    @property
    def name(self) -> str:
        return "server failover-ip update"

    @property
    def description(self) -> str:
        return "Sets the List of Failover IPs that are Assigned to a Server"

    @property
    def module_path(self) -> str:
        return ".commands.failover_ips.post_v2_failover_ips_server_id"


@register_command
class GetV2FailoverIpsServerIdAvailable(ModuleRunner):
    @property
    def name(self) -> str:
        return "server failover-ip available"

    @property
    def description(self) -> str:
        return "Fetch a List of all Failover IPs that are Available to be Assigned to a Server"

    @property
    def module_path(self) -> str:
        return ".commands.failover_ips.get_v2_failover_ips_server_id_available"


@register_command
class GetV2Images(ModuleRunner):
    @property
    def name(self) -> str:
        return "image list"

    @property
    def description(self) -> str:
        return "List All Images"

    @property
    def module_path(self) -> str:
        return ".commands.images.get_v2_images"


@register_command
class GetV2ImagesImageIdOrSlug(ModuleRunner):
    @property
    def name(self) -> str:
        return "image get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Image"

    @property
    def module_path(self) -> str:
        return ".commands.images.get_v2_images_image_id_or_slug"


@register_command
class PutV2ImagesImageId(ModuleRunner):
    @property
    def name(self) -> str:
        return "image update"

    @property
    def description(self) -> str:
        return "Update an Existing Image"

    @property
    def module_path(self) -> str:
        return ".commands.images.put_v2_images_image_id"


@register_command
class GetV2ImagesImageIdDownload(ModuleRunner):
    @property
    def name(self) -> str:
        return "image download"

    @property
    def description(self) -> str:
        return "Download an Existing Image"

    @property
    def module_path(self) -> str:
        return ".commands.images.get_v2_images_image_id_download"


@register_command
class GetV2AccountKeysKeyId(ModuleRunner):
    @property
    def name(self) -> str:
        return "ssh-key get"

    @property
    def description(self) -> str:
        return "Fetch an Existing SSH Key"

    @property
    def module_path(self) -> str:
        return ".commands.keys.get_v2_account_keys_key_id"


@register_command
class PutV2AccountKeysKeyId(ModuleRunner):
    @property
    def name(self) -> str:
        return "ssh-key update"

    @property
    def description(self) -> str:
        return "Update an Existing SSH Key"

    @property
    def module_path(self) -> str:
        return ".commands.keys.put_v2_account_keys_key_id"


@register_command
class DeleteV2AccountKeysKeyId(ModuleRunner):
    @property
    def name(self) -> str:
        return "ssh-key delete"

    @property
    def description(self) -> str:
        return "Delete an Existing SSH Key"

    @property
    def module_path(self) -> str:
        return ".commands.keys.delete_v2_account_keys_key_id"


@register_command
class GetV2AccountKeys(ModuleRunner):
    @property
    def name(self) -> str:
        return "ssh-key list"

    @property
    def description(self) -> str:
        return "List All SSH Keys"

    @property
    def module_path(self) -> str:
        return ".commands.keys.get_v2_account_keys"


@register_command
class PostV2AccountKeys(ModuleRunner):
    @property
    def name(self) -> str:
        return "ssh-key create"

    @property
    def description(self) -> str:
        return "Add a New SSH Key"

    @property
    def module_path(self) -> str:
        return ".commands.keys.post_v2_account_keys"


@register_command
class GetV2LoadBalancersLoadBalancerId(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.get_v2_load_balancers_load_balancer_id"


@register_command
class PutV2LoadBalancersLoadBalancerId(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer update"

    @property
    def description(self) -> str:
        return "Update an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.put_v2_load_balancers_load_balancer_id"


@register_command
class DeleteV2LoadBalancersLoadBalancerId(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer delete"

    @property
    def description(self) -> str:
        return "Cancel an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.delete_v2_load_balancers_load_balancer_id"


@register_command
class GetV2LoadBalancers(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer list"

    @property
    def description(self) -> str:
        return "List all Load Balancers"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.get_v2_load_balancers"


@register_command
class PostV2LoadBalancers(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer create"

    @property
    def description(self) -> str:
        return "Create a New Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.post_v2_load_balancers"


@register_command
class GetV2LoadBalancersAvailability(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer availability"

    @property
    def description(self) -> str:
        return "Fetch Load Balancer Availability and Pricing"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.get_v2_load_balancers_availability"


@register_command
class PostV2LoadBalancersLoadBalancerIdServers(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer server create"

    @property
    def description(self) -> str:
        return "Add Servers to an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.post_v2_load_balancers_load_balancer_id_servers"


@register_command
class DeleteV2LoadBalancersLoadBalancerIdServers(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer server delete"

    @property
    def description(self) -> str:
        return "Remove Servers from an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.delete_v2_load_balancers_load_balancer_id_servers"


@register_command
class PostV2LoadBalancersLoadBalancerIdForwardingRules(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer rule create"

    @property
    def description(self) -> str:
        return "Add Forwarding Rules to an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.post_v2_load_balancers_load_balancer_id_forwarding_rules"


@register_command
class DeleteV2LoadBalancersLoadBalancerIdForwardingRules(ModuleRunner):
    @property
    def name(self) -> str:
        return "load-balancer rule delete"

    @property
    def description(self) -> str:
        return "Remove Forwarding Rules from an Existing Load Balancer"

    @property
    def module_path(self) -> str:
        return ".commands.load_balancers.delete_v2_load_balancers_load_balancer_id_forwarding_rules"


@register_command
class GetV2Regions(ModuleRunner):
    @property
    def name(self) -> str:
        return "region list"

    @property
    def description(self) -> str:
        return "List all Regions"

    @property
    def module_path(self) -> str:
        return ".commands.regions.get_v2_regions"


@register_command
class GetV2ReverseNamesIpv6(ModuleRunner):
    @property
    def name(self) -> str:
        return "server ipv6-ptr-ns list"

    @property
    def description(self) -> str:
        return "Fetch all Existing IPv6 Name Server Records"

    @property
    def module_path(self) -> str:
        return ".commands.reverse_names.get_v2_reverse_names_ipv6"


@register_command
class PostV2ReverseNamesIpv6(ModuleRunner):
    @property
    def name(self) -> str:
        return "server ipv6-ptr-ns update"

    @property
    def description(self) -> str:
        return "Create New or Update Existing IPv6 Name Server Records"

    @property
    def module_path(self) -> str:
        return ".commands.reverse_names.post_v2_reverse_names_ipv6"


@register_command
class GetV2SamplesetsServerIdLatest(ModuleRunner):
    @property
    def name(self) -> str:
        return "server metrics get"

    @property
    def description(self) -> str:
        return "Fetch the Latest Performance and Usage Data Sample Set for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.sample_sets.get_v2_samplesets_server_id_latest"


@register_command
class GetV2SamplesetsServerId(ModuleRunner):
    @property
    def name(self) -> str:
        return "server metrics list"

    @property
    def description(self) -> str:
        return "Fetch all of the Performance and Usage Data Sample Sets for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.sample_sets.get_v2_samplesets_server_id"


@register_command
class GetV2ServersServerIdActions(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action list"

    @property
    def description(self) -> str:
        return "List All Actions for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.get_v2_servers_server_id_actions"


@register_command
class PostV2ServersServerIdActionsChangeThresholdAlerts(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-threshold-alerts"

    @property
    def description(self) -> str:
        return "Set or Update the Threshold Alerts for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_threshold_alerts"


@register_command
class PostV2ServersServerIdActionsIsRunning(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action is-running"

    @property
    def description(self) -> str:
        return "Check if a Server is Running"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_is_running"


@register_command
class PostV2ServersServerIdActionsPing(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action ping"

    @property
    def description(self) -> str:
        return "Attempt to Ping a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_ping"


@register_command
class PostV2ServersServerIdActionsUncancel(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action uncancel"

    @property
    def description(self) -> str:
        return "Revert the Cancellation of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_uncancel"


@register_command
class PostV2ServersServerIdActionsUptime(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action uptime"

    @property
    def description(self) -> str:
        return "Check the Uptime of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_uptime"


@register_command
class PostV2ServersServerIdActionsAttachBackup(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action attach-backup"

    @property
    def description(self) -> str:
        return "Attach a Backup to a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_attach_backup"


@register_command
class PostV2ServersServerIdActionsChangeBackupSchedule(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-backup-schedule"

    @property
    def description(self) -> str:
        return "Change the Backup Schedule of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_backup_schedule"


@register_command
class PostV2ServersServerIdActionsChangeManageOffsiteBackupCopies(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-manage-offsite-backup-copies"

    @property
    def description(self) -> str:
        return "Change the Management of Offsite Backup Copies"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_manage_offsite_backup_copies"


@register_command
class PostV2ServersServerIdActionsChangeOffsiteBackupLocation(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-offsite-backup-location"

    @property
    def description(self) -> str:
        return "Change the Offsite Backup Location of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_offsite_backup_location"


@register_command
class PostV2ServersServerIdActionsCloneUsingBackup(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action clone-using-backup"

    @property
    def description(self) -> str:
        return "Restore a Backup of a Server to a Different Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_clone_using_backup"


@register_command
class PostV2ServersServerIdActionsDetachBackup(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action detach-backup"

    @property
    def description(self) -> str:
        return "Detach Any Attached Backup from a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_detach_backup"


@register_command
class PostV2ServersServerIdActionsDisableBackups(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action disable-backups"

    @property
    def description(self) -> str:
        return "Disable Backups for an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_disable_backups"


@register_command
class PostV2ServersServerIdActionsEnableBackups(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action enable-backups"

    @property
    def description(self) -> str:
        return "Enable Two Daily Backups for an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_enable_backups"


@register_command
class PostV2ServersServerIdActionsRestore(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action restore"

    @property
    def description(self) -> str:
        return "Restore a Backup to a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_restore"


@register_command
class PostV2ServersServerIdActionsTakeBackup(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action take-backup"

    @property
    def description(self) -> str:
        return "Take a Backup of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_take_backup"


@register_command
class PostV2ServersServerIdActionsPasswordReset(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action password-reset"

    @property
    def description(self) -> str:
        return "Reset the Password of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_password_reset"


@register_command
class PostV2ServersServerIdActionsPowerCycle(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action power-cycle"

    @property
    def description(self) -> str:
        return "Power a Server Off and then On"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_power_cycle"


@register_command
class PostV2ServersServerIdActionsPowerOff(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action power-off"

    @property
    def description(self) -> str:
        return "Power a Server Off"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_power_off"


@register_command
class PostV2ServersServerIdActionsPowerOn(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action power-on"

    @property
    def description(self) -> str:
        return "Power a Server On"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_power_on"


@register_command
class PostV2ServersServerIdActionsReboot(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action reboot"

    @property
    def description(self) -> str:
        return "Request a Server Perform a Reboot"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_reboot"


@register_command
class PostV2ServersServerIdActionsShutdown(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action shutdown"

    @property
    def description(self) -> str:
        return "Request a Server Perform a Shutdown"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_shutdown"


@register_command
class PostV2ServersServerIdActionsChangeAdvancedFeatures(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-advanced-features"

    @property
    def description(self) -> str:
        return "Change the Advanced Features of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_advanced_features"


@register_command
class PostV2ServersServerIdActionsChangeAdvancedFirewallRules(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-advanced-firewall-rules"

    @property
    def description(self) -> str:
        return "Change the Advanced Firewall Rules for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_advanced_firewall_rules"


@register_command
class PostV2ServersServerIdActionsChangeKernel(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-kernel"

    @property
    def description(self) -> str:
        return "Change the Kernel of a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_kernel"


@register_command
class PostV2ServersServerIdActionsChangePartner(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-partner"

    @property
    def description(self) -> str:
        return "Add, Update or Remove a Partner Server for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_partner"


@register_command
class PostV2ServersServerIdActionsDisableSelinux(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action disable-selinux"

    @property
    def description(self) -> str:
        return "Disable SE Linux for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_disable_selinux"


@register_command
class PostV2ServersServerIdActionsRebuild(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action rebuild"

    @property
    def description(self) -> str:
        return "Rebuild an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_rebuild"


@register_command
class PostV2ServersServerIdActionsResize(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action resize"

    @property
    def description(self) -> str:
        return "Update the Size and Related Options for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_resize"


@register_command
class PostV2ServersServerIdActionsAddDisk(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action add-disk"

    @property
    def description(self) -> str:
        return "Create an Additional Disk for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_add_disk"


@register_command
class PostV2ServersServerIdActionsResizeDisk(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action resize-disk"

    @property
    def description(self) -> str:
        return "Alter the Size of an Existing Disk for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_resize_disk"


@register_command
class PostV2ServersServerIdActionsDeleteDisk(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action delete-disk"

    @property
    def description(self) -> str:
        return "Delete an Additional Disk for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_delete_disk"


@register_command
class PostV2ServersServerIdActionsChangeIpv6ReverseNameservers(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-ipv6-reverse-nameservers"

    @property
    def description(self) -> str:
        return "Update the IPv6 Reverse Name Servers for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_ipv_6_reverse_nameservers"


@register_command
class PostV2ServersServerIdActionsChangeReverseName(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-reverse-name"

    @property
    def description(self) -> str:
        return "Change the Reverse Name for an IPv4 Address on a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_reverse_name"


@register_command
class PostV2ServersServerIdActionsRename(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action rename"

    @property
    def description(self) -> str:
        return "Rename a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_rename"


@register_command
class PostV2ServersServerIdActionsChangeIpv6(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-ipv6"

    @property
    def description(self) -> str:
        return "Enable or Disable IPv6 for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_ipv_6"


@register_command
class PostV2ServersServerIdActionsChangePortBlocking(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-port-blocking"

    @property
    def description(self) -> str:
        return "Change the Port Blocking for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_port_blocking"


@register_command
class PostV2ServersServerIdActionsEnableIpv6(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action enable-ipv6"

    @property
    def description(self) -> str:
        return "Enable IPv6 for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_enable_ipv_6"


@register_command
class PostV2ServersServerIdActionsChangeNetwork(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-network"

    @property
    def description(self) -> str:
        return "Move a Server to an Existing Network"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_network"


@register_command
class PostV2ServersServerIdActionsChangeSeparatePrivateNetworkInterface(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-separate-private-network-interface"

    @property
    def description(self) -> str:
        return "Enable or Disable a Separate Private Network Interface for a Server in a VPC"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_separate_private_network_interface"


@register_command
class PostV2ServersServerIdActionsChangeSourceAndDestinationCheck(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-source-and-destination-check"

    @property
    def description(self) -> str:
        return "Enable or Disable Network Source and Destination Checks for a Server in a VPC"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_source_and_destination_check"


@register_command
class PostV2ServersServerIdActionsChangeVpcIpv4(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action change-vpc-ipv4"

    @property
    def description(self) -> str:
        return "Change the IPv4 Address for a Server in a VPC"

    @property
    def module_path(self) -> str:
        return ".commands.server_actions.post_v_2_servers_server_id_actions_change_vpc_ipv_4"


@register_command
class GetV2ServersServerId(ModuleRunner):
    @property
    def name(self) -> str:
        return "server get"

    @property
    def description(self) -> str:
        return "Fetch an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id"


@register_command
class DeleteV2ServersServerId(ModuleRunner):
    @property
    def name(self) -> str:
        return "server delete"

    @property
    def description(self) -> str:
        return "Cancel an Existing Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.delete_v2_servers_server_id"


@register_command
class GetV2Servers(ModuleRunner):
    @property
    def name(self) -> str:
        return "server list"

    @property
    def description(self) -> str:
        return "List All Servers"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers"


@register_command
class PostV2Servers(ModuleRunner):
    @property
    def name(self) -> str:
        return "server create"

    @property
    def description(self) -> str:
        return "Create a New Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.post_v2_servers"


@register_command
class GetV2ServersServerIdActionsActionId(ModuleRunner):
    @property
    def name(self) -> str:
        return "server action get"

    @property
    def description(self) -> str:
        return "Fetch an Action for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_actions_action_id"


@register_command
class GetV2ServersServerIdAdvancedFirewallRules(ModuleRunner):
    @property
    def name(self) -> str:
        return "server firewall list"

    @property
    def description(self) -> str:
        return "Fetch All Advanced Firewall Rules for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_advanced_firewall_rules"


@register_command
class GetV2ServersServerIdAvailableAdvancedFeatures(ModuleRunner):
    @property
    def name(self) -> str:
        return "server feature list"

    @property
    def description(self) -> str:
        return "Fetch the Currently Available Advanced Features for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_available_advanced_features"


@register_command
class GetV2ServersServerIdBackups(ModuleRunner):
    @property
    def name(self) -> str:
        return "server backup list"

    @property
    def description(self) -> str:
        return "List All Backups for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_backups"


@register_command
class PostV2ServersServerIdBackups(ModuleRunner):
    @property
    def name(self) -> str:
        return "server backup upload"

    @property
    def description(self) -> str:
        return "Upload a Backup for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.post_v2_servers_server_id_backups"


@register_command
class GetV2ServersServerIdKernels(ModuleRunner):
    @property
    def name(self) -> str:
        return "server kernel list"

    @property
    def description(self) -> str:
        return "List all Available Kernels for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_kernels"


@register_command
class GetV2ServersServerIdSnapshots(ModuleRunner):
    @property
    def name(self) -> str:
        return "server snapshot list"

    @property
    def description(self) -> str:
        return "List all Snapshots for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_snapshots"


@register_command
class GetV2ServersServerIdThresholdAlerts(ModuleRunner):
    @property
    def name(self) -> str:
        return "server alert get"

    @property
    def description(self) -> str:
        return "Fetch the Currently Set Threshold Alerts for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_threshold_alerts"


@register_command
class GetV2ServersThresholdAlerts(ModuleRunner):
    @property
    def name(self) -> str:
        return "server alert list"

    @property
    def description(self) -> str:
        return "List any Servers that have a Current Exceeded Threshold Alert"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_threshold_alerts"


@register_command
class GetV2ServersServerIdSoftware(ModuleRunner):
    @property
    def name(self) -> str:
        return "server software"

    @property
    def description(self) -> str:
        return "List all Enabled Software for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_software"


@register_command
class GetV2ServersServerIdUserData(ModuleRunner):
    @property
    def name(self) -> str:
        return "server user-data"

    @property
    def description(self) -> str:
        return "Fetch the Currently Set UserData for a Server"

    @property
    def module_path(self) -> str:
        return ".commands.servers.get_v2_servers_server_id_user_data"


@register_command
class GetV2Sizes(ModuleRunner):
    @property
    def name(self) -> str:
        return "size list"

    @property
    def description(self) -> str:
        return "List All Available Sizes"

    @property
    def module_path(self) -> str:
        return ".commands.sizes.get_v2_sizes"


@register_command
class GetV2SoftwareSoftwareId(ModuleRunner):
    @property
    def name(self) -> str:
        return "software get"

    @property
    def description(self) -> str:
        return "Fetch Existing Software"

    @property
    def module_path(self) -> str:
        return ".commands.software.get_v2_software_software_id"


@register_command
class GetV2Software(ModuleRunner):
    @property
    def name(self) -> str:
        return "software list"

    @property
    def description(self) -> str:
        return "List All Available Software"

    @property
    def module_path(self) -> str:
        return ".commands.software.get_v2_software"


@register_command
class GetV2SoftwareOperatingSystemOperatingSystemIdOrSlug(ModuleRunner):
    @property
    def name(self) -> str:
        return "software operating-system"

    @property
    def description(self) -> str:
        return "List All Available Software for an Existing Operating System"

    @property
    def module_path(self) -> str:
        return ".commands.software.get_v2_software_operating_system_operating_system_id_or_slug"


@register_command
class GetV2VpcsVpcId(ModuleRunner):
    @property
    def name(self) -> str:
        return "vpc get"

    @property
    def description(self) -> str:
        return "Fetch an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpcs.get_v2_vpcs_vpc_id"


@register_command
class PutV2VpcsVpcId(ModuleRunner):
    @property
    def name(self) -> str:
        return "vpc update"

    @property
    def description(self) -> str:
        return "Update an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpcs.put_v2_vpcs_vpc_id"


@register_command
class DeleteV2VpcsVpcId(ModuleRunner):
    @property
    def name(self) -> str:
        return "vpc delete"

    @property
    def description(self) -> str:
        return "Delete an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpcs.delete_v2_vpcs_vpc_id"


@register_command
class PatchV2VpcsVpcId(ModuleRunner):
    @property
    def name(self) -> str:
        return "vpc patch"

    @property
    def description(self) -> str:
        return "Update an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpcs.patch_v2_vpcs_vpc_id"


@register_command
class GetV2Vpcs(ModuleRunner):
    @property
    def name(self) -> str:
        return "vpc list"

    @property
    def description(self) -> str:
        return "List All Existing VPCs"

    @property
    def module_path(self) -> str:
        return ".commands.vpcs.get_v2_vpcs"


@register_command
class PostV2Vpcs(ModuleRunner):
    @property
    def name(self) -> str:
        return "vpc create"

    @property
    def description(self) -> str:
        return "Create a New VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpcs.post_v2_vpcs"


@register_command
class GetV2VpcsVpcIdMembers(ModuleRunner):
    @property
    def name(self) -> str:
        return "vpc members"

    @property
    def description(self) -> str:
        return "List All Members of an Existing VPC"

    @property
    def module_path(self) -> str:
        return ".commands.vpcs.get_v2_vpcs_vpc_id_members"
