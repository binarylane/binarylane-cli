from ...client.api.server.server_tagged_action import sync
from ...client.client import Client
from ...runner import CommandRunner


class Command(CommandRunner):
    @property
    def name(self):
        return "server_tagged-action"

    @property
    def description(self):
        return """Perform an Action on Servers by Tag"""

    def configure(self, parser):
        """Add arguments for server_tagged-action"""

        # Unknown Union[AddDisk, AttachBackup, ChangeAdvancedFeatures, ChangeAdvancedFirewallRules, ChangeBackupSchedule, ChangeIpv6, ChangeIpv6ReverseNameservers, ChangeKernel, ChangeManageOffsiteBackupCopies, ChangeNetwork, ChangeOffsiteBackupLocation, ChangePartner, ChangePortBlocking, ChangeReverseName, ChangeSeparatePrivateNetworkInterface, ChangeSourceAndDestinationCheck, ChangeThresholdAlerts, ChangeVpcIpv4, CloneUsingBackup, DeleteDisk, DetachBackup, DisableBackups, DisableSelinux, EnableBackups, EnableIpv6, IsRunning, PasswordReset, Ping, PowerCycle, PowerOff, PowerOn, Reboot, Rebuild, Rename, Resize, ResizeDisk, Restore, Shutdown, TakeBackup, Uncancel, Uptime] union_property.py.jinja

    def request(
        self,
        client: Client,
    ):
        return sync(
            client=client,
        )
