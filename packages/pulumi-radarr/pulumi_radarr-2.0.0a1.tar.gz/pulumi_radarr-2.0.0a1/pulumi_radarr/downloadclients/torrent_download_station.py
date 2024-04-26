# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TorrentDownloadStationArgs', 'TorrentDownloadStation']

@pulumi.input_type
class TorrentDownloadStationArgs:
    def __init__(__self__, *,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TorrentDownloadStation resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[str] password: Password.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        :param pulumi.Input[str] username: Username.
        """
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if remove_completed_downloads is not None:
            pulumi.set(__self__, "remove_completed_downloads", remove_completed_downloads)
        if remove_failed_downloads is not None:
            pulumi.set(__self__, "remove_failed_downloads", remove_failed_downloads)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if use_ssl is not None:
            pulumi.set(__self__, "use_ssl", use_ssl)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        host.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Download Client name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @remove_completed_downloads.setter
    def remove_completed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_completed_downloads", value)

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @remove_failed_downloads.setter
    def remove_failed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_failed_downloads", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[pulumi.Input[bool]]:
        """
        Use SSL flag.
        """
        return pulumi.get(self, "use_ssl")

    @use_ssl.setter
    def use_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_ssl", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class _TorrentDownloadStationState:
    def __init__(__self__, *,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TorrentDownloadStation resources.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[str] password: Password.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        :param pulumi.Input[str] username: Username.
        """
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if remove_completed_downloads is not None:
            pulumi.set(__self__, "remove_completed_downloads", remove_completed_downloads)
        if remove_failed_downloads is not None:
            pulumi.set(__self__, "remove_failed_downloads", remove_failed_downloads)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if use_ssl is not None:
            pulumi.set(__self__, "use_ssl", use_ssl)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        host.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Download Client name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @remove_completed_downloads.setter
    def remove_completed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_completed_downloads", value)

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @remove_failed_downloads.setter
    def remove_failed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_failed_downloads", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[pulumi.Input[bool]]:
        """
        Use SSL flag.
        """
        return pulumi.get(self, "use_ssl")

    @use_ssl.setter
    def use_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_ssl", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class TorrentDownloadStation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- subcategory:Download Clients -->
        Download Client TorrentDownloadStation resource.
        For more information refer to [Download Client](https://wiki.servarr.com/radarr/settings#download-clients) and [TorrentDownloadStation](https://wiki.servarr.com/radarr/supported#torrentdownloadstation).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_radarr as radarr

        example = radarr.download_clients.TorrentDownloadStation("example",
            enable=True,
            host="downloadstation",
            port=5000,
            priority=1)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import radarr:DownloadClients/torrentDownloadStation:TorrentDownloadStation example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[str] password: Password.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        :param pulumi.Input[str] username: Username.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TorrentDownloadStationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Download Clients -->
        Download Client TorrentDownloadStation resource.
        For more information refer to [Download Client](https://wiki.servarr.com/radarr/settings#download-clients) and [TorrentDownloadStation](https://wiki.servarr.com/radarr/supported#torrentdownloadstation).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_radarr as radarr

        example = radarr.download_clients.TorrentDownloadStation("example",
            enable=True,
            host="downloadstation",
            port=5000,
            priority=1)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import radarr:DownloadClients/torrentDownloadStation:TorrentDownloadStation example 1
        ```

        :param str resource_name: The name of the resource.
        :param TorrentDownloadStationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TorrentDownloadStationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TorrentDownloadStationArgs.__new__(TorrentDownloadStationArgs)

            __props__.__dict__["enable"] = enable
            __props__.__dict__["host"] = host
            __props__.__dict__["name"] = name
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["port"] = port
            __props__.__dict__["priority"] = priority
            __props__.__dict__["remove_completed_downloads"] = remove_completed_downloads
            __props__.__dict__["remove_failed_downloads"] = remove_failed_downloads
            __props__.__dict__["tags"] = tags
            __props__.__dict__["use_ssl"] = use_ssl
            __props__.__dict__["username"] = username
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(TorrentDownloadStation, __self__).__init__(
            'radarr:DownloadClients/torrentDownloadStation:TorrentDownloadStation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            host: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
            remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            use_ssl: Optional[pulumi.Input[bool]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'TorrentDownloadStation':
        """
        Get an existing TorrentDownloadStation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[str] password: Password.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        :param pulumi.Input[str] username: Username.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TorrentDownloadStationState.__new__(_TorrentDownloadStationState)

        __props__.__dict__["enable"] = enable
        __props__.__dict__["host"] = host
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["port"] = port
        __props__.__dict__["priority"] = priority
        __props__.__dict__["remove_completed_downloads"] = remove_completed_downloads
        __props__.__dict__["remove_failed_downloads"] = remove_failed_downloads
        __props__.__dict__["tags"] = tags
        __props__.__dict__["use_ssl"] = use_ssl
        __props__.__dict__["username"] = username
        return TorrentDownloadStation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        host.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Download Client name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[str]:
        """
        Password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> pulumi.Output[bool]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> pulumi.Output[bool]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> pulumi.Output[bool]:
        """
        Use SSL flag.
        """
        return pulumi.get(self, "use_ssl")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        Username.
        """
        return pulumi.get(self, "username")

