from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.license_ import License
from ..models.size_options_request import SizeOptionsRequest
from ..models.ssh_key_request import SshKeyRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateServerRequest")


@attr.s(auto_attribs=True)
class CreateServerRequest:
    """
    Attributes:
        size (str): The slug of the selected size.
        image (Union[int, str]): The slug or id of the selected operating system. Example: 5.
        region (str): The slug of the selected region.
        name (Union[Unset, None, str]):
        backups (Union[Unset, None, bool]): If true this will enable two daily backups for the server.
            Options.daily_backups will override this value if provided. Setting this to false has no effect.
        ipv6 (Union[Unset, None, bool]): If true this will enable IPv6 for this server.
        vpc_id (Union[Unset, None, int]): Leave null to use default (public) network for the selected region.
        ssh_keys (Union[Unset, None, List[Union[int, str]]]): This may be either the SSH keys Ids or fingerprints. If
            this is null or not provided any SSH keys that have been marked as default will be deployed (if the operating
            system supports SSH keys). Submit an empty array to disable deployment of default keys.
        new_ssh_key (Union[Unset, None, SshKeyRequest]):
        options (Union[Unset, None, SizeOptionsRequest]):
        licenses (Union[Unset, None, List[License]]):
        user_data (Union[Unset, None, str]): If provided this will be used to initialise the new server. This must be
            left null if the Image does not support UserData, see DistributionInfo.Features for more information.
        port_blocking (Union[Unset, None, bool]): Port blocking of outgoing connections for email, SSH and Remote
            Desktop (TCP ports 22, 25, and 3389) is enabled by default for all new servers. If this is false port blocking
            will be disabled. Disabling port blocking is only available to reviewed accounts.
    """

    size: str
    image: Union[int, str]
    region: str
    name: Union[Unset, None, str] = UNSET
    backups: Union[Unset, None, bool] = UNSET
    ipv6: Union[Unset, None, bool] = UNSET
    vpc_id: Union[Unset, None, int] = UNSET
    ssh_keys: Union[Unset, None, List[Union[int, str]]] = UNSET
    new_ssh_key: Union[Unset, None, SshKeyRequest] = UNSET
    options: Union[Unset, None, SizeOptionsRequest] = UNSET
    licenses: Union[Unset, None, List[License]] = UNSET
    user_data: Union[Unset, None, str] = UNSET
    port_blocking: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        size = self.size
        image: Union[int, str]

        image = self.image

        region = self.region
        name = self.name
        backups = self.backups
        ipv6 = self.ipv6
        vpc_id = self.vpc_id
        ssh_keys: Union[Unset, None, List[Union[int, str]]] = UNSET
        if not isinstance(self.ssh_keys, Unset):
            if self.ssh_keys is None:
                ssh_keys = None
            else:
                ssh_keys = []
                for ssh_keys_item_data in self.ssh_keys:
                    ssh_keys_item: Union[int, str]

                    ssh_keys_item = ssh_keys_item_data

                    ssh_keys.append(ssh_keys_item)

        new_ssh_key: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.new_ssh_key, Unset):
            new_ssh_key = self.new_ssh_key.to_dict() if self.new_ssh_key else None

        options: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict() if self.options else None

        licenses: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.licenses, Unset):
            if self.licenses is None:
                licenses = None
            else:
                licenses = []
                for licenses_item_data in self.licenses:
                    licenses_item = licenses_item_data.to_dict()

                    licenses.append(licenses_item)

        user_data = self.user_data
        port_blocking = self.port_blocking

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size": size,
                "image": image,
                "region": region,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if backups is not UNSET:
            field_dict["backups"] = backups
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if vpc_id is not UNSET:
            field_dict["vpc_id"] = vpc_id
        if ssh_keys is not UNSET:
            field_dict["ssh_keys"] = ssh_keys
        if new_ssh_key is not UNSET:
            field_dict["new_ssh_key"] = new_ssh_key
        if options is not UNSET:
            field_dict["options"] = options
        if licenses is not UNSET:
            field_dict["licenses"] = licenses
        if user_data is not UNSET:
            field_dict["user_data"] = user_data
        if port_blocking is not UNSET:
            field_dict["port_blocking"] = port_blocking

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        size = d.pop("size")

        def _parse_image(data: object) -> Union[int, str]:
            return cast(Union[int, str], data)

        image = _parse_image(d.pop("image"))

        region = d.pop("region")

        name = d.pop("name", UNSET)

        backups = d.pop("backups", UNSET)

        ipv6 = d.pop("ipv6", UNSET)

        vpc_id = d.pop("vpc_id", UNSET)

        ssh_keys = []
        _ssh_keys = d.pop("ssh_keys", UNSET)
        for ssh_keys_item_data in _ssh_keys or []:

            def _parse_ssh_keys_item(data: object) -> Union[int, str]:
                return cast(Union[int, str], data)

            ssh_keys_item = _parse_ssh_keys_item(ssh_keys_item_data)

            ssh_keys.append(ssh_keys_item)

        _new_ssh_key = d.pop("new_ssh_key", UNSET)
        new_ssh_key: Union[Unset, None, SshKeyRequest]
        if _new_ssh_key is None:
            new_ssh_key = None
        elif isinstance(_new_ssh_key, Unset):
            new_ssh_key = UNSET
        else:
            new_ssh_key = SshKeyRequest.from_dict(_new_ssh_key)

        _options = d.pop("options", UNSET)
        options: Union[Unset, None, SizeOptionsRequest]
        if _options is None:
            options = None
        elif isinstance(_options, Unset):
            options = UNSET
        else:
            options = SizeOptionsRequest.from_dict(_options)

        licenses = []
        _licenses = d.pop("licenses", UNSET)
        for licenses_item_data in _licenses or []:
            licenses_item = License.from_dict(licenses_item_data)

            licenses.append(licenses_item)

        user_data = d.pop("user_data", UNSET)

        port_blocking = d.pop("port_blocking", UNSET)

        create_server_request = cls(
            size=size,
            image=image,
            region=region,
            name=name,
            backups=backups,
            ipv6=ipv6,
            vpc_id=vpc_id,
            ssh_keys=ssh_keys,
            new_ssh_key=new_ssh_key,
            options=options,
            licenses=licenses,
            user_data=user_data,
            port_blocking=port_blocking,
        )

        create_server_request.additional_properties = d
        return create_server_request

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
