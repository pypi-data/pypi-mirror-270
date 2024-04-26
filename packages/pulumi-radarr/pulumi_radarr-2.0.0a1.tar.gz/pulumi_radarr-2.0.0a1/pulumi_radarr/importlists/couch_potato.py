# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CouchPotatoArgs', 'CouchPotato']

@pulumi.input_type
class CouchPotatoArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str],
                 link: pulumi.Input[str],
                 minimum_availability: pulumi.Input[str],
                 monitor: pulumi.Input[str],
                 only_active: pulumi.Input[bool],
                 port: pulumi.Input[int],
                 quality_profile_id: pulumi.Input[int],
                 root_folder_path: pulumi.Input[str],
                 enable_auto: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 search_on_add: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 url_base: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CouchPotato resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] link: Link.
        :param pulumi.Input[str] minimum_availability: Minimum availability.
        :param pulumi.Input[str] monitor: Should monitor.
        :param pulumi.Input[bool] only_active: Only active.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] enable_auto: Enable automatic add flag.
        :param pulumi.Input[bool] enabled: Enabled flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[bool] search_on_add: Search on add flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] url_base: Base URL.
        """
        pulumi.set(__self__, "api_key", api_key)
        pulumi.set(__self__, "link", link)
        pulumi.set(__self__, "minimum_availability", minimum_availability)
        pulumi.set(__self__, "monitor", monitor)
        pulumi.set(__self__, "only_active", only_active)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        pulumi.set(__self__, "root_folder_path", root_folder_path)
        if enable_auto is not None:
            pulumi.set(__self__, "enable_auto", enable_auto)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if list_order is not None:
            pulumi.set(__self__, "list_order", list_order)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if search_on_add is not None:
            pulumi.set(__self__, "search_on_add", search_on_add)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if url_base is not None:
            pulumi.set(__self__, "url_base", url_base)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter
    def link(self) -> pulumi.Input[str]:
        """
        Link.
        """
        return pulumi.get(self, "link")

    @link.setter
    def link(self, value: pulumi.Input[str]):
        pulumi.set(self, "link", value)

    @property
    @pulumi.getter(name="minimumAvailability")
    def minimum_availability(self) -> pulumi.Input[str]:
        """
        Minimum availability.
        """
        return pulumi.get(self, "minimum_availability")

    @minimum_availability.setter
    def minimum_availability(self, value: pulumi.Input[str]):
        pulumi.set(self, "minimum_availability", value)

    @property
    @pulumi.getter
    def monitor(self) -> pulumi.Input[str]:
        """
        Should monitor.
        """
        return pulumi.get(self, "monitor")

    @monitor.setter
    def monitor(self, value: pulumi.Input[str]):
        pulumi.set(self, "monitor", value)

    @property
    @pulumi.getter(name="onlyActive")
    def only_active(self) -> pulumi.Input[bool]:
        """
        Only active.
        """
        return pulumi.get(self, "only_active")

    @only_active.setter
    def only_active(self, value: pulumi.Input[bool]):
        pulumi.set(self, "only_active", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> pulumi.Input[int]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @quality_profile_id.setter
    def quality_profile_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "quality_profile_id", value)

    @property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> pulumi.Input[str]:
        """
        Root folder path.
        """
        return pulumi.get(self, "root_folder_path")

    @root_folder_path.setter
    def root_folder_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "root_folder_path", value)

    @property
    @pulumi.getter(name="enableAuto")
    def enable_auto(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable automatic add flag.
        """
        return pulumi.get(self, "enable_auto")

    @enable_auto.setter
    def enable_auto(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_auto", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enabled flag.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="listOrder")
    def list_order(self) -> Optional[pulumi.Input[int]]:
        """
        List order.
        """
        return pulumi.get(self, "list_order")

    @list_order.setter
    def list_order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "list_order", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Import List name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="searchOnAdd")
    def search_on_add(self) -> Optional[pulumi.Input[bool]]:
        """
        Search on add flag.
        """
        return pulumi.get(self, "search_on_add")

    @search_on_add.setter
    def search_on_add(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "search_on_add", value)

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
    @pulumi.getter(name="urlBase")
    def url_base(self) -> Optional[pulumi.Input[str]]:
        """
        Base URL.
        """
        return pulumi.get(self, "url_base")

    @url_base.setter
    def url_base(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url_base", value)


@pulumi.input_type
class _CouchPotatoState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 enable_auto: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 link: Optional[pulumi.Input[str]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 minimum_availability: Optional[pulumi.Input[str]] = None,
                 monitor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 only_active: Optional[pulumi.Input[bool]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 search_on_add: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 url_base: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CouchPotato resources.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[bool] enable_auto: Enable automatic add flag.
        :param pulumi.Input[bool] enabled: Enabled flag.
        :param pulumi.Input[str] link: Link.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[str] minimum_availability: Minimum availability.
        :param pulumi.Input[str] monitor: Should monitor.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[bool] only_active: Only active.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] search_on_add: Search on add flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] url_base: Base URL.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if enable_auto is not None:
            pulumi.set(__self__, "enable_auto", enable_auto)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if link is not None:
            pulumi.set(__self__, "link", link)
        if list_order is not None:
            pulumi.set(__self__, "list_order", list_order)
        if minimum_availability is not None:
            pulumi.set(__self__, "minimum_availability", minimum_availability)
        if monitor is not None:
            pulumi.set(__self__, "monitor", monitor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if only_active is not None:
            pulumi.set(__self__, "only_active", only_active)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if quality_profile_id is not None:
            pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        if root_folder_path is not None:
            pulumi.set(__self__, "root_folder_path", root_folder_path)
        if search_on_add is not None:
            pulumi.set(__self__, "search_on_add", search_on_add)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if url_base is not None:
            pulumi.set(__self__, "url_base", url_base)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="enableAuto")
    def enable_auto(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable automatic add flag.
        """
        return pulumi.get(self, "enable_auto")

    @enable_auto.setter
    def enable_auto(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_auto", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Enabled flag.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def link(self) -> Optional[pulumi.Input[str]]:
        """
        Link.
        """
        return pulumi.get(self, "link")

    @link.setter
    def link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "link", value)

    @property
    @pulumi.getter(name="listOrder")
    def list_order(self) -> Optional[pulumi.Input[int]]:
        """
        List order.
        """
        return pulumi.get(self, "list_order")

    @list_order.setter
    def list_order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "list_order", value)

    @property
    @pulumi.getter(name="minimumAvailability")
    def minimum_availability(self) -> Optional[pulumi.Input[str]]:
        """
        Minimum availability.
        """
        return pulumi.get(self, "minimum_availability")

    @minimum_availability.setter
    def minimum_availability(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "minimum_availability", value)

    @property
    @pulumi.getter
    def monitor(self) -> Optional[pulumi.Input[str]]:
        """
        Should monitor.
        """
        return pulumi.get(self, "monitor")

    @monitor.setter
    def monitor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "monitor", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Import List name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="onlyActive")
    def only_active(self) -> Optional[pulumi.Input[bool]]:
        """
        Only active.
        """
        return pulumi.get(self, "only_active")

    @only_active.setter
    def only_active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "only_active", value)

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
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> Optional[pulumi.Input[int]]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @quality_profile_id.setter
    def quality_profile_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "quality_profile_id", value)

    @property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> Optional[pulumi.Input[str]]:
        """
        Root folder path.
        """
        return pulumi.get(self, "root_folder_path")

    @root_folder_path.setter
    def root_folder_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "root_folder_path", value)

    @property
    @pulumi.getter(name="searchOnAdd")
    def search_on_add(self) -> Optional[pulumi.Input[bool]]:
        """
        Search on add flag.
        """
        return pulumi.get(self, "search_on_add")

    @search_on_add.setter
    def search_on_add(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "search_on_add", value)

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
    @pulumi.getter(name="urlBase")
    def url_base(self) -> Optional[pulumi.Input[str]]:
        """
        Base URL.
        """
        return pulumi.get(self, "url_base")

    @url_base.setter
    def url_base(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url_base", value)


class CouchPotato(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 enable_auto: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 link: Optional[pulumi.Input[str]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 minimum_availability: Optional[pulumi.Input[str]] = None,
                 monitor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 only_active: Optional[pulumi.Input[bool]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 search_on_add: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 url_base: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- subcategory:Import Lists -->
        Import List Couch Potato resource.
        For more information refer to [Import List](https://wiki.servarr.com/radarr/settings#import-lists) and [Couch Potato](https://wiki.servarr.com/radarr/supported#couchpotatoimport).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_radarr as radarr

        example = radarr.import_lists.CouchPotato("example",
            api_key="APIKey",
            enable_auto=False,
            enabled=True,
            link="http://localhost",
            minimum_availability="tba",
            monitor="none",
            only_active=True,
            port=5050,
            quality_profile_id=1,
            root_folder_path="/config",
            search_on_add=False)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import radarr:ImportLists/couchPotato:CouchPotato example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[bool] enable_auto: Enable automatic add flag.
        :param pulumi.Input[bool] enabled: Enabled flag.
        :param pulumi.Input[str] link: Link.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[str] minimum_availability: Minimum availability.
        :param pulumi.Input[str] monitor: Should monitor.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[bool] only_active: Only active.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] search_on_add: Search on add flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] url_base: Base URL.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CouchPotatoArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Import Lists -->
        Import List Couch Potato resource.
        For more information refer to [Import List](https://wiki.servarr.com/radarr/settings#import-lists) and [Couch Potato](https://wiki.servarr.com/radarr/supported#couchpotatoimport).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_radarr as radarr

        example = radarr.import_lists.CouchPotato("example",
            api_key="APIKey",
            enable_auto=False,
            enabled=True,
            link="http://localhost",
            minimum_availability="tba",
            monitor="none",
            only_active=True,
            port=5050,
            quality_profile_id=1,
            root_folder_path="/config",
            search_on_add=False)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import radarr:ImportLists/couchPotato:CouchPotato example 1
        ```

        :param str resource_name: The name of the resource.
        :param CouchPotatoArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CouchPotatoArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 enable_auto: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 link: Optional[pulumi.Input[str]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 minimum_availability: Optional[pulumi.Input[str]] = None,
                 monitor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 only_active: Optional[pulumi.Input[bool]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 search_on_add: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 url_base: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CouchPotatoArgs.__new__(CouchPotatoArgs)

            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["enable_auto"] = enable_auto
            __props__.__dict__["enabled"] = enabled
            if link is None and not opts.urn:
                raise TypeError("Missing required property 'link'")
            __props__.__dict__["link"] = link
            __props__.__dict__["list_order"] = list_order
            if minimum_availability is None and not opts.urn:
                raise TypeError("Missing required property 'minimum_availability'")
            __props__.__dict__["minimum_availability"] = minimum_availability
            if monitor is None and not opts.urn:
                raise TypeError("Missing required property 'monitor'")
            __props__.__dict__["monitor"] = monitor
            __props__.__dict__["name"] = name
            if only_active is None and not opts.urn:
                raise TypeError("Missing required property 'only_active'")
            __props__.__dict__["only_active"] = only_active
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            if quality_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'quality_profile_id'")
            __props__.__dict__["quality_profile_id"] = quality_profile_id
            if root_folder_path is None and not opts.urn:
                raise TypeError("Missing required property 'root_folder_path'")
            __props__.__dict__["root_folder_path"] = root_folder_path
            __props__.__dict__["search_on_add"] = search_on_add
            __props__.__dict__["tags"] = tags
            __props__.__dict__["url_base"] = url_base
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(CouchPotato, __self__).__init__(
            'radarr:ImportLists/couchPotato:CouchPotato',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            enable_auto: Optional[pulumi.Input[bool]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            link: Optional[pulumi.Input[str]] = None,
            list_order: Optional[pulumi.Input[int]] = None,
            minimum_availability: Optional[pulumi.Input[str]] = None,
            monitor: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            only_active: Optional[pulumi.Input[bool]] = None,
            port: Optional[pulumi.Input[int]] = None,
            quality_profile_id: Optional[pulumi.Input[int]] = None,
            root_folder_path: Optional[pulumi.Input[str]] = None,
            search_on_add: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            url_base: Optional[pulumi.Input[str]] = None) -> 'CouchPotato':
        """
        Get an existing CouchPotato resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[bool] enable_auto: Enable automatic add flag.
        :param pulumi.Input[bool] enabled: Enabled flag.
        :param pulumi.Input[str] link: Link.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[str] minimum_availability: Minimum availability.
        :param pulumi.Input[str] monitor: Should monitor.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[bool] only_active: Only active.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] search_on_add: Search on add flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] url_base: Base URL.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CouchPotatoState.__new__(_CouchPotatoState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["enable_auto"] = enable_auto
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["link"] = link
        __props__.__dict__["list_order"] = list_order
        __props__.__dict__["minimum_availability"] = minimum_availability
        __props__.__dict__["monitor"] = monitor
        __props__.__dict__["name"] = name
        __props__.__dict__["only_active"] = only_active
        __props__.__dict__["port"] = port
        __props__.__dict__["quality_profile_id"] = quality_profile_id
        __props__.__dict__["root_folder_path"] = root_folder_path
        __props__.__dict__["search_on_add"] = search_on_add
        __props__.__dict__["tags"] = tags
        __props__.__dict__["url_base"] = url_base
        return CouchPotato(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="enableAuto")
    def enable_auto(self) -> pulumi.Output[bool]:
        """
        Enable automatic add flag.
        """
        return pulumi.get(self, "enable_auto")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Enabled flag.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def link(self) -> pulumi.Output[str]:
        """
        Link.
        """
        return pulumi.get(self, "link")

    @property
    @pulumi.getter(name="listOrder")
    def list_order(self) -> pulumi.Output[int]:
        """
        List order.
        """
        return pulumi.get(self, "list_order")

    @property
    @pulumi.getter(name="minimumAvailability")
    def minimum_availability(self) -> pulumi.Output[str]:
        """
        Minimum availability.
        """
        return pulumi.get(self, "minimum_availability")

    @property
    @pulumi.getter
    def monitor(self) -> pulumi.Output[str]:
        """
        Should monitor.
        """
        return pulumi.get(self, "monitor")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Import List name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="onlyActive")
    def only_active(self) -> pulumi.Output[bool]:
        """
        Only active.
        """
        return pulumi.get(self, "only_active")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> pulumi.Output[int]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> pulumi.Output[str]:
        """
        Root folder path.
        """
        return pulumi.get(self, "root_folder_path")

    @property
    @pulumi.getter(name="searchOnAdd")
    def search_on_add(self) -> pulumi.Output[bool]:
        """
        Search on add flag.
        """
        return pulumi.get(self, "search_on_add")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="urlBase")
    def url_base(self) -> pulumi.Output[str]:
        """
        Base URL.
        """
        return pulumi.get(self, "url_base")

