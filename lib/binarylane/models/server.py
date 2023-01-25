from __future__ import annotations

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from binarylane.models.advanced_server_features import AdvancedServerFeatures
from binarylane.models.attached_backup import AttachedBackup
from binarylane.models.backup_settings import BackupSettings
from binarylane.models.backup_window import BackupWindow
from binarylane.models.disk import Disk
from binarylane.models.host import Host
from binarylane.models.image import Image
from binarylane.models.kernel import Kernel
from binarylane.models.networks import Networks
from binarylane.models.region import Region
from binarylane.models.rescue_console import RescueConsole
from binarylane.models.selected_size_options import SelectedSizeOptions
from binarylane.models.server_status import ServerStatus
from binarylane.models.size import Size
from binarylane.types import UNSET, Unset

T = TypeVar("T", bound="Server")


@attr.s(auto_attribs=True)
class Server:
    """
    Attributes:
        id (int): The ID of this server.
        name (str): The hostname of this server.
        memory (int): The memory in MB of this server.
        vcpus (int): The number of virtual CPUs of this server.
        disk (int): The total disk in GB of this server.
        created_at (datetime.datetime): The date and time in ISO8601 format of this server's initial creation.
        status (ServerStatus):
            | Value | Description |
            | ----- | ----------- |
            | new | The server is currently in the process of building and is not yet available for use. |
            | active | The server is available for use. |
            | archive | The server is powered off due to cancellation or non payment. |
            | off | The server has been powered off, but may be powered back on. |

        backup_ids (List[int]): A list of the currently existing backup image IDs for this server (if any).
        features (List[str]): A list of the currently enabled features on this server.
        region (Region): The region this server is allocated to.
        image (Image): The base image used to create this server.
        size (Size): The currently selected size for this server.
        size_slug (str): The slug of the currently selected size for this server.
        networks (Networks): A list of the networks of the server.
        disks (List[Disk]): A list of the disks that are currently attached to the server.
        backup_settings (BackupSettings): Detailed backup settings for the server.
        rescue_console (RescueConsole): Details of the rescue console for this server.
        failover_ips (List[str]): A list of any assigned failover IP addresses for this server.
        host (Host): Summary information about the host of this server.
        password_change_supported (bool): If this is true the password_reset server action can be called to change a
            user's password. If this is false the password_reset server action will merely clear the root/administrator
            password allowing the password to be changed via the web console.
        advanced_features (AdvancedServerFeatures): The currently enabled advanced features, machine type and processor
            flags.
        vpc_id (Union[Unset, None, int]): The VPC ID that this server is allocated to. If this value is null the server
            is in the default (public) network for the region.
        selected_size_options (Union[Unset, None, SelectedSizeOptions]): An object that details the selected options for
            the current size.
        kernel (Union[Unset, None, Kernel]): The currently selected kernel for the server.
        next_backup_window (Union[Unset, None, BackupWindow]): The details of the next scheduled backup, if any.
        cancelled_at (Union[Unset, None, datetime.datetime]): If the server has been cancelled, this is the date and
            time in ISO8601 format of that cancellation.
        partner_id (Union[Unset, None, int]): The server ID of the partner of this server, if one has been assigned.
        permalink (Union[Unset, None, str]): A randomly generated two-word identifier assigned to servers in regions
            that support this feature.
        attached_backup (Union[Unset, None, AttachedBackup]): An object that provides details of any backup image
            currently attached to the server..
    """

    id: int
    name: str
    memory: int
    vcpus: int
    disk: int
    created_at: datetime.datetime
    status: ServerStatus
    backup_ids: List[int]
    features: List[str]
    region: Region
    image: Image
    size: Size
    size_slug: str
    networks: Networks
    disks: List[Disk]
    backup_settings: BackupSettings
    rescue_console: RescueConsole
    failover_ips: List[str]
    host: Host
    password_change_supported: bool
    advanced_features: AdvancedServerFeatures
    vpc_id: Union[Unset, None, int] = UNSET
    selected_size_options: Union[Unset, None, SelectedSizeOptions] = UNSET
    kernel: Union[Unset, None, Kernel] = UNSET
    next_backup_window: Union[Unset, None, BackupWindow] = UNSET
    cancelled_at: Union[Unset, None, datetime.datetime] = UNSET
    partner_id: Union[Unset, None, int] = UNSET
    permalink: Union[Unset, None, str] = UNSET
    attached_backup: Union[Unset, None, AttachedBackup] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        memory = self.memory
        vcpus = self.vcpus
        disk = self.disk
        created_at = self.created_at.isoformat()

        status = self.status.value

        backup_ids = self.backup_ids

        features = self.features

        region = self.region.to_dict()

        image = self.image.to_dict()

        size = self.size.to_dict()

        size_slug = self.size_slug
        networks = self.networks.to_dict()

        disks = []
        for disks_item_data in self.disks:
            disks_item = disks_item_data.to_dict()

            disks.append(disks_item)

        backup_settings = self.backup_settings.to_dict()

        rescue_console = self.rescue_console.to_dict()

        failover_ips = self.failover_ips

        host = self.host.to_dict()

        password_change_supported = self.password_change_supported
        advanced_features = self.advanced_features.to_dict()

        vpc_id = self.vpc_id
        selected_size_options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.selected_size_options, Unset):
            selected_size_options = self.selected_size_options.to_dict() if self.selected_size_options else None

        kernel: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.kernel, Unset):
            kernel = self.kernel.to_dict() if self.kernel else None

        next_backup_window: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.next_backup_window, Unset):
            next_backup_window = self.next_backup_window.to_dict() if self.next_backup_window else None

        cancelled_at: Union[Unset, None, str] = UNSET
        if not isinstance(self.cancelled_at, Unset):
            cancelled_at = self.cancelled_at.isoformat() if self.cancelled_at else None

        partner_id = self.partner_id
        permalink = self.permalink
        attached_backup: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attached_backup, Unset):
            attached_backup = self.attached_backup.to_dict() if self.attached_backup else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "memory": memory,
                "vcpus": vcpus,
                "disk": disk,
                "created_at": created_at,
                "status": status,
                "backup_ids": backup_ids,
                "features": features,
                "region": region,
                "image": image,
                "size": size,
                "size_slug": size_slug,
                "networks": networks,
                "disks": disks,
                "backup_settings": backup_settings,
                "rescue_console": rescue_console,
                "failover_ips": failover_ips,
                "host": host,
                "password_change_supported": password_change_supported,
                "advanced_features": advanced_features,
            }
        )
        if vpc_id is not UNSET:
            field_dict["vpc_id"] = vpc_id
        if selected_size_options is not UNSET:
            field_dict["selected_size_options"] = selected_size_options
        if kernel is not UNSET:
            field_dict["kernel"] = kernel
        if next_backup_window is not UNSET:
            field_dict["next_backup_window"] = next_backup_window
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if partner_id is not UNSET:
            field_dict["partner_id"] = partner_id
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if attached_backup is not UNSET:
            field_dict["attached_backup"] = attached_backup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        memory = d.pop("memory")

        vcpus = d.pop("vcpus")

        disk = d.pop("disk")

        created_at = isoparse(d.pop("created_at"))

        status = ServerStatus(d.pop("status"))

        backup_ids = cast(List[int], d.pop("backup_ids"))

        features = cast(List[str], d.pop("features"))

        region = Region.from_dict(d.pop("region"))

        image = Image.from_dict(d.pop("image"))

        size = Size.from_dict(d.pop("size"))

        size_slug = d.pop("size_slug")

        networks = Networks.from_dict(d.pop("networks"))

        disks = []
        _disks = d.pop("disks")
        for disks_item_data in _disks:
            disks_item = Disk.from_dict(disks_item_data)

            disks.append(disks_item)

        backup_settings = BackupSettings.from_dict(d.pop("backup_settings"))

        rescue_console = RescueConsole.from_dict(d.pop("rescue_console"))

        failover_ips = cast(List[str], d.pop("failover_ips"))

        host = Host.from_dict(d.pop("host"))

        password_change_supported = d.pop("password_change_supported")

        advanced_features = AdvancedServerFeatures.from_dict(d.pop("advanced_features"))

        vpc_id = d.pop("vpc_id", UNSET)

        _selected_size_options = d.pop("selected_size_options", UNSET)
        selected_size_options: Union[Unset, None, SelectedSizeOptions]
        if _selected_size_options is None:
            selected_size_options = None
        elif isinstance(_selected_size_options, Unset):
            selected_size_options = UNSET
        else:
            selected_size_options = SelectedSizeOptions.from_dict(_selected_size_options)

        _kernel = d.pop("kernel", UNSET)
        kernel: Union[Unset, None, Kernel]
        if _kernel is None:
            kernel = None
        elif isinstance(_kernel, Unset):
            kernel = UNSET
        else:
            kernel = Kernel.from_dict(_kernel)

        _next_backup_window = d.pop("next_backup_window", UNSET)
        next_backup_window: Union[Unset, None, BackupWindow]
        if _next_backup_window is None:
            next_backup_window = None
        elif isinstance(_next_backup_window, Unset):
            next_backup_window = UNSET
        else:
            next_backup_window = BackupWindow.from_dict(_next_backup_window)

        _cancelled_at = d.pop("cancelled_at", UNSET)
        cancelled_at: Union[Unset, None, datetime.datetime]
        if _cancelled_at is None:
            cancelled_at = None
        elif isinstance(_cancelled_at, Unset):
            cancelled_at = UNSET
        else:
            cancelled_at = isoparse(_cancelled_at)

        partner_id = d.pop("partner_id", UNSET)

        permalink = d.pop("permalink", UNSET)

        _attached_backup = d.pop("attached_backup", UNSET)
        attached_backup: Union[Unset, None, AttachedBackup]
        if _attached_backup is None:
            attached_backup = None
        elif isinstance(_attached_backup, Unset):
            attached_backup = UNSET
        else:
            attached_backup = AttachedBackup.from_dict(_attached_backup)

        server = cls(
            id=id,
            name=name,
            memory=memory,
            vcpus=vcpus,
            disk=disk,
            created_at=created_at,
            status=status,
            backup_ids=backup_ids,
            features=features,
            region=region,
            image=image,
            size=size,
            size_slug=size_slug,
            networks=networks,
            disks=disks,
            backup_settings=backup_settings,
            rescue_console=rescue_console,
            failover_ips=failover_ips,
            host=host,
            password_change_supported=password_change_supported,
            advanced_features=advanced_features,
            vpc_id=vpc_id,
            selected_size_options=selected_size_options,
            kernel=kernel,
            next_backup_window=next_backup_window,
            cancelled_at=cancelled_at,
            partner_id=partner_id,
            permalink=permalink,
            attached_backup=attached_backup,
        )

        server.additional_properties = d
        return server

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
