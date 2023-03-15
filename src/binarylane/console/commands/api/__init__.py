""" Contains methods for accessing the API """
from __future__ import annotations

import re
from typing import List

from binarylane.console.runners import Descriptor

__all__ = ["descriptors"]
descriptors: List[Descriptor] = []


def add_descriptor(module_path: str, name: str, description: str) -> None:
    # Many API operation summaries are written title-cased (like a headline), rather than as a sentence.
    description = re.sub(r" ([A-Z])([a-z]+\b)", lambda m: " " + m.group(1).lower() + m.group(2), description)

    descriptors.append(Descriptor(module_path, name, description))


add_descriptor(
    ".commands.api.get_v2_account",
    "account get",
    "Fetch Information About the Current Account",
)
add_descriptor(
    ".commands.api.get_v2_actions_action_id",
    "action get",
    "Fetch an Existing Action",
)
add_descriptor(
    ".commands.api.get_v2_actions",
    "action list",
    "List All Actions",
)
add_descriptor(
    ".commands.api.post_v2_actions_action_id_proceed",
    "action proceed",
    "Respond to a UserInteractionRequired Action",
)
add_descriptor(
    ".commands.api.get_v2_customers_my_balance",
    "account balance",
    "Fetch Current Balance Information",
)
add_descriptor(
    ".commands.api.get_v2_customers_my_invoices_invoice_id",
    "account invoice get",
    "Fetch an Invoice",
)
add_descriptor(
    ".commands.api.get_v2_customers_my_invoices",
    "account invoice list",
    "Fetch Invoices",
)
add_descriptor(
    ".commands.api.get_v2_customers_my_unpaid_payment_failed_invoices",
    "account invoice overdue",
    "Fetch Unpaid Failed Invoices",
)
add_descriptor(
    ".commands.api.get_v2_data_usages_server_id_current",
    "server data-usage get",
    "Fetch the Current Data Usage (Transfer) for a Server",
)
add_descriptor(
    ".commands.api.get_v2_data_usages_current",
    "server data-usage list",
    "Fetch all Current Data Usage (Transfer) for All Servers",
)
add_descriptor(
    ".commands.api.get_v2_domains_nameservers",
    "domain nameservers list",
    "List All Public Nameservers",
)
add_descriptor(
    ".commands.api.post_v2_domains_refresh_nameserver_cache",
    "domain refresh-nameserver-cache",
    "Refresh Cached Nameserver Domain Records",
)
add_descriptor(
    ".commands.api.get_v2_domains",
    "domain list",
    "List All Domains",
)
add_descriptor(
    ".commands.api.post_v2_domains",
    "domain create",
    "Create a New Domain",
)
add_descriptor(
    ".commands.api.get_v2_domains_domain_name",
    "domain get",
    "Fetch an Existing Domain",
)
add_descriptor(
    ".commands.api.delete_v2_domains_domain_name",
    "domain delete",
    "Delete an Existing Domain",
)
add_descriptor(
    ".commands.api.get_v2_domains_domain_name_records",
    "domain record list",
    "List All Domain Records for a Domain",
)
add_descriptor(
    ".commands.api.post_v2_domains_domain_name_records",
    "domain record create",
    "Create a New Domain Record",
)
add_descriptor(
    ".commands.api.get_v2_domains_domain_name_records_record_id",
    "domain record get",
    "Fetch an Existing Domain Record",
)
add_descriptor(
    ".commands.api.put_v2_domains_domain_name_records_record_id",
    "domain record update",
    "Update an Existing Domain Record",
)
add_descriptor(
    ".commands.api.delete_v2_domains_domain_name_records_record_id",
    "domain record delete",
    "Delete an Existing Domain Record",
)
add_descriptor(
    ".commands.api.get_v2_failover_ips_server_id",
    "server failover-ip get",
    "Fetch the Failover IPs for a Server",
)
add_descriptor(
    ".commands.api.post_v2_failover_ips_server_id",
    "server failover-ip update",
    "Sets the List of Failover IPs that are Assigned to a Server",
)
add_descriptor(
    ".commands.api.get_v2_failover_ips_server_id_available",
    "server failover-ip available",
    "Fetch a List of all Failover IPs that are Available to be Assigned to a Server",
)
add_descriptor(
    ".commands.api.get_v2_images",
    "image list",
    "List All Images",
)
add_descriptor(
    ".commands.api.get_v2_images_image_id_or_slug",
    "image get",
    "Fetch an Existing Image",
)
add_descriptor(
    ".commands.api.put_v2_images_image_id",
    "image update",
    "Update an Existing Image",
)
add_descriptor(
    ".commands.api.get_v2_images_image_id_download",
    "image download",
    "Download an Existing Image",
)
add_descriptor(
    ".commands.api.get_v2_account_keys_key_id",
    "ssh-key get",
    "Fetch an Existing SSH Key",
)
add_descriptor(
    ".commands.api.put_v2_account_keys_key_id",
    "ssh-key update",
    "Update an Existing SSH Key",
)
add_descriptor(
    ".commands.api.delete_v2_account_keys_key_id",
    "ssh-key delete",
    "Delete an Existing SSH Key",
)
add_descriptor(
    ".commands.api.get_v2_account_keys",
    "ssh-key list",
    "List All SSH Keys",
)
add_descriptor(
    ".commands.api.post_v2_account_keys",
    "ssh-key create",
    "Add a New SSH Key",
)
add_descriptor(
    ".commands.api.get_v2_load_balancers_load_balancer_id",
    "load-balancer get",
    "Fetch an Existing Load Balancer",
)
add_descriptor(
    ".commands.api.put_v2_load_balancers_load_balancer_id",
    "load-balancer update",
    "Update an Existing Load Balancer",
)
add_descriptor(
    ".commands.api.delete_v2_load_balancers_load_balancer_id",
    "load-balancer delete",
    "Cancel an Existing Load Balancer",
)
add_descriptor(
    ".commands.api.get_v2_load_balancers",
    "load-balancer list",
    "List all Load Balancers",
)
add_descriptor(
    ".commands.api.post_v2_load_balancers",
    "load-balancer create",
    "Create a New Load Balancer",
)
add_descriptor(
    ".commands.api.get_v2_load_balancers_availability",
    "load-balancer availability",
    "Fetch Load Balancer Availability and Pricing",
)
add_descriptor(
    ".commands.api.post_v2_load_balancers_load_balancer_id_servers",
    "load-balancer server create",
    "Add Servers to an Existing Load Balancer",
)
add_descriptor(
    ".commands.api.delete_v2_load_balancers_load_balancer_id_servers",
    "load-balancer server delete",
    "Remove Servers from an Existing Load Balancer",
)
add_descriptor(
    ".commands.api.post_v2_load_balancers_load_balancer_id_forwarding_rules",
    "load-balancer rule create",
    "Add Forwarding Rules to an Existing Load Balancer",
)
add_descriptor(
    ".commands.api.delete_v2_load_balancers_load_balancer_id_forwarding_rules",
    "load-balancer rule delete",
    "Remove Forwarding Rules from an Existing Load Balancer",
)
add_descriptor(
    ".commands.api.get_v2_regions",
    "region list",
    "List all Regions",
)
add_descriptor(
    ".commands.api.get_v2_reverse_names_ipv6",
    "server ipv6-ptr-ns list",
    "Fetch all Existing IPv6 Name Server Records",
)
add_descriptor(
    ".commands.api.post_v2_reverse_names_ipv6",
    "server ipv6-ptr-ns update",
    "Create New or Update Existing IPv6 Name Server Records",
)
add_descriptor(
    ".commands.api.get_v2_samplesets_server_id_latest",
    "server metrics get",
    "Fetch the Latest Performance and Usage Data Sample Set for a Server",
)
add_descriptor(
    ".commands.api.get_v2_samplesets_server_id",
    "server metrics list",
    "Fetch all of the Performance and Usage Data Sample Sets for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_actions",
    "server action list",
    "List All Actions for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_threshold_alerts",
    "server action change-threshold-alerts",
    "Set or Update the Threshold Alerts for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_is_running",
    "server action is-running",
    "Check if a Server is Running",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_ping",
    "server action ping",
    "Attempt to Ping a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_uncancel",
    "server action uncancel",
    "Revert the Cancellation of a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_uptime",
    "server action uptime",
    "Check the Uptime of a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_attach_backup",
    "server action attach-backup",
    "Attach a Backup to a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_backup_schedule",
    "server action change-backup-schedule",
    "Change the Backup Schedule of a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_manage_offsite_backup_copies",
    "server action change-manage-offsite-backup-copies",
    "Change the Management of Offsite Backup Copies",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_offsite_backup_location",
    "server action change-offsite-backup-location",
    "Change the Offsite Backup Location of a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_clone_using_backup",
    "server action clone-using-backup",
    "Restore a Backup of a Server to a Different Existing Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_detach_backup",
    "server action detach-backup",
    "Detach Any Attached Backup from a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_disable_backups",
    "server action disable-backups",
    "Disable Backups for an Existing Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_enable_backups",
    "server action enable-backups",
    "Enable Two Daily Backups for an Existing Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_restore",
    "server action restore",
    "Restore a Backup to a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_take_backup",
    "server action take-backup",
    "Take a Backup of a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_password_reset",
    "server action password-reset",
    "Reset the Password of a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_power_cycle",
    "server action power-cycle",
    "Power a Server Off and then On",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_power_off",
    "server action power-off",
    "Power a Server Off",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_power_on",
    "server action power-on",
    "Power a Server On",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_reboot",
    "server action reboot",
    "Request a Server Perform a Reboot",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_shutdown",
    "server action shutdown",
    "Request a Server Perform a Shutdown",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_advanced_features",
    "server action change-advanced-features",
    "Change the Advanced Features of a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_advanced_firewall_rules",
    "server action change-advanced-firewall-rules",
    "Change the Advanced Firewall Rules for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_kernel",
    "server action change-kernel",
    "Change the Kernel of a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_partner",
    "server action change-partner",
    "Add, Update or Remove a Partner Server for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_disable_selinux",
    "server action disable-selinux",
    "Disable SE Linux for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_rebuild",
    "server action rebuild",
    "Rebuild an Existing Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_resize",
    "server action resize",
    "Update the Size and Related Options for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_add_disk",
    "server action add-disk",
    "Create an Additional Disk for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_resize_disk",
    "server action resize-disk",
    "Alter the Size of an Existing Disk for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_delete_disk",
    "server action delete-disk",
    "Delete an Additional Disk for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_ipv_6_reverse_nameservers",
    "server action change-ipv6-reverse-nameservers",
    "Update the IPv6 Reverse Name Servers for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_reverse_name",
    "server action change-reverse-name",
    "Change the Reverse Name for an IPv4 Address on a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_rename",
    "server action rename",
    "Rename a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_ipv_6",
    "server action change-ipv6",
    "Enable or Disable IPv6 for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_port_blocking",
    "server action change-port-blocking",
    "Change the Port Blocking for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_enable_ipv_6",
    "server action enable-ipv6",
    "Enable IPv6 for a Server",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_network",
    "server action change-network",
    "Move a Server to an Existing Network",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_separate_private_network_interface",
    "server action change-separate-private-network-interface",
    "Enable or Disable a Separate Private Network Interface for a Server in a VPC",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_source_and_destination_check",
    "server action change-source-and-destination-check",
    "Enable or Disable Network Source and Destination Checks for a Server in a VPC",
)
add_descriptor(
    ".commands.api.post_v_2_servers_server_id_actions_change_vpc_ipv_4",
    "server action change-vpc-ipv4",
    "Change the IPv4 Address for a Server in a VPC",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id",
    "server get",
    "Fetch an Existing Server",
)
add_descriptor(
    ".commands.api.delete_v2_servers_server_id",
    "server delete",
    "Cancel an Existing Server",
)
add_descriptor(
    ".commands.api.get_v2_servers",
    "server list",
    "List All Servers",
)
add_descriptor(
    ".commands.api.post_v2_servers",
    "server create",
    "Create a New Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_actions_action_id",
    "server action get",
    "Fetch an Action for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_advanced_firewall_rules",
    "server firewall list",
    "Fetch All Advanced Firewall Rules for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_available_advanced_features",
    "server feature list",
    "Fetch the Currently Available Advanced Features for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_backups",
    "server backup list",
    "List All Backups for a Server",
)
add_descriptor(
    ".commands.api.post_v2_servers_server_id_backups",
    "server backup upload",
    "Upload a Backup for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_kernels",
    "server kernel list",
    "List all Available Kernels for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_snapshots",
    "server snapshot list",
    "List all Snapshots for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_threshold_alerts",
    "server alert get",
    "Fetch the Currently Set Threshold Alerts for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_threshold_alerts",
    "server alert list",
    "List any Servers that have a Current Exceeded Threshold Alert",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_software",
    "server software",
    "List all Enabled Software for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_user_data",
    "server user-data",
    "Fetch the Currently Set UserData for a Server",
)
add_descriptor(
    ".commands.api.get_v2_servers_server_id_console",
    "server console",
    "Fetch the Console URLs for a Server",
)
add_descriptor(
    ".commands.api.get_v2_sizes",
    "size list",
    "List All Available Sizes",
)
add_descriptor(
    ".commands.api.get_v2_software_software_id",
    "software get",
    "Fetch Existing Software",
)
add_descriptor(
    ".commands.api.get_v2_software",
    "software list",
    "List All Available Software",
)
add_descriptor(
    ".commands.api.get_v2_software_operating_system_operating_system_id_or_slug",
    "software operating-system",
    "List All Available Software for an Existing Operating System",
)
add_descriptor(
    ".commands.api.get_v2_vpcs_vpc_id",
    "vpc get",
    "Fetch an Existing VPC",
)
add_descriptor(
    ".commands.api.put_v2_vpcs_vpc_id",
    "vpc update",
    "Update an Existing VPC",
)
add_descriptor(
    ".commands.api.delete_v2_vpcs_vpc_id",
    "vpc delete",
    "Delete an Existing VPC",
)
add_descriptor(
    ".commands.api.patch_v2_vpcs_vpc_id",
    "vpc patch",
    "Update an Existing VPC",
)
add_descriptor(
    ".commands.api.get_v2_vpcs",
    "vpc list",
    "List All Existing VPCs",
)
add_descriptor(
    ".commands.api.post_v2_vpcs",
    "vpc create",
    "Create a New VPC",
)
add_descriptor(
    ".commands.api.get_v2_vpcs_vpc_id_members",
    "vpc members",
    "List All Members of an Existing VPC",
)
