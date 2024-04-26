# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['Stevenlu2Args', 'Stevenlu2']

@pulumi.input_type
class Stevenlu2Args:
    def __init__(__self__, *,
                 min_score: pulumi.Input[int],
                 minimum_availability: pulumi.Input[str],
                 monitor: pulumi.Input[str],
                 quality_profile_id: pulumi.Input[int],
                 root_folder_path: pulumi.Input[str],
                 source: pulumi.Input[int],
                 enable_auto: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 search_on_add: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Stevenlu2 resource.
        :param pulumi.Input[int] min_score: Min score.
        :param pulumi.Input[str] minimum_availability: Minimum availability.
        :param pulumi.Input[str] monitor: Should monitor.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[int] source: Source.`0` Standard, `1` Imdb, `2` Metacritic, `3` RottenTomatoes,
        :param pulumi.Input[bool] enable_auto: Enable automatic add flag.
        :param pulumi.Input[bool] enabled: Enabled flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[bool] search_on_add: Search on add flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "min_score", min_score)
        pulumi.set(__self__, "minimum_availability", minimum_availability)
        pulumi.set(__self__, "monitor", monitor)
        pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        pulumi.set(__self__, "root_folder_path", root_folder_path)
        pulumi.set(__self__, "source", source)
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

    @property
    @pulumi.getter(name="minScore")
    def min_score(self) -> pulumi.Input[int]:
        """
        Min score.
        """
        return pulumi.get(self, "min_score")

    @min_score.setter
    def min_score(self, value: pulumi.Input[int]):
        pulumi.set(self, "min_score", value)

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
    @pulumi.getter
    def source(self) -> pulumi.Input[int]:
        """
        Source.`0` Standard, `1` Imdb, `2` Metacritic, `3` RottenTomatoes,
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[int]):
        pulumi.set(self, "source", value)

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


@pulumi.input_type
class _Stevenlu2State:
    def __init__(__self__, *,
                 enable_auto: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 min_score: Optional[pulumi.Input[int]] = None,
                 minimum_availability: Optional[pulumi.Input[str]] = None,
                 monitor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 search_on_add: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Stevenlu2 resources.
        :param pulumi.Input[bool] enable_auto: Enable automatic add flag.
        :param pulumi.Input[bool] enabled: Enabled flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] min_score: Min score.
        :param pulumi.Input[str] minimum_availability: Minimum availability.
        :param pulumi.Input[str] monitor: Should monitor.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] search_on_add: Search on add flag.
        :param pulumi.Input[int] source: Source.`0` Standard, `1` Imdb, `2` Metacritic, `3` RottenTomatoes,
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if enable_auto is not None:
            pulumi.set(__self__, "enable_auto", enable_auto)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if list_order is not None:
            pulumi.set(__self__, "list_order", list_order)
        if min_score is not None:
            pulumi.set(__self__, "min_score", min_score)
        if minimum_availability is not None:
            pulumi.set(__self__, "minimum_availability", minimum_availability)
        if monitor is not None:
            pulumi.set(__self__, "monitor", monitor)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if quality_profile_id is not None:
            pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        if root_folder_path is not None:
            pulumi.set(__self__, "root_folder_path", root_folder_path)
        if search_on_add is not None:
            pulumi.set(__self__, "search_on_add", search_on_add)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="minScore")
    def min_score(self) -> Optional[pulumi.Input[int]]:
        """
        Min score.
        """
        return pulumi.get(self, "min_score")

    @min_score.setter
    def min_score(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_score", value)

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
    def source(self) -> Optional[pulumi.Input[int]]:
        """
        Source.`0` Standard, `1` Imdb, `2` Metacritic, `3` RottenTomatoes,
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "source", value)

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


class Stevenlu2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_auto: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 min_score: Optional[pulumi.Input[int]] = None,
                 minimum_availability: Optional[pulumi.Input[str]] = None,
                 monitor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 search_on_add: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Import Lists -->
        Import List Stevenlu2 resource.
        For more information refer to [Import List](https://wiki.servarr.com/radarr/settings#import-lists) and [Stevenlu2](https://wiki.servarr.com/radarr/supported#stevenlu2import).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_radarr as radarr

        example = radarr.import_lists.Stevenlu2("example",
            enable_auto=False,
            enabled=True,
            min_score=5,
            minimum_availability="tba",
            monitor="none",
            quality_profile_id=1,
            root_folder_path="/config",
            search_on_add=False,
            source=0)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import radarr:ImportLists/stevenlu2:Stevenlu2 example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_auto: Enable automatic add flag.
        :param pulumi.Input[bool] enabled: Enabled flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] min_score: Min score.
        :param pulumi.Input[str] minimum_availability: Minimum availability.
        :param pulumi.Input[str] monitor: Should monitor.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] search_on_add: Search on add flag.
        :param pulumi.Input[int] source: Source.`0` Standard, `1` Imdb, `2` Metacritic, `3` RottenTomatoes,
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Stevenlu2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Import Lists -->
        Import List Stevenlu2 resource.
        For more information refer to [Import List](https://wiki.servarr.com/radarr/settings#import-lists) and [Stevenlu2](https://wiki.servarr.com/radarr/supported#stevenlu2import).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_radarr as radarr

        example = radarr.import_lists.Stevenlu2("example",
            enable_auto=False,
            enabled=True,
            min_score=5,
            minimum_availability="tba",
            monitor="none",
            quality_profile_id=1,
            root_folder_path="/config",
            search_on_add=False,
            source=0)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import radarr:ImportLists/stevenlu2:Stevenlu2 example 1
        ```

        :param str resource_name: The name of the resource.
        :param Stevenlu2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(Stevenlu2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable_auto: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 min_score: Optional[pulumi.Input[int]] = None,
                 minimum_availability: Optional[pulumi.Input[str]] = None,
                 monitor: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 search_on_add: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = Stevenlu2Args.__new__(Stevenlu2Args)

            __props__.__dict__["enable_auto"] = enable_auto
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["list_order"] = list_order
            if min_score is None and not opts.urn:
                raise TypeError("Missing required property 'min_score'")
            __props__.__dict__["min_score"] = min_score
            if minimum_availability is None and not opts.urn:
                raise TypeError("Missing required property 'minimum_availability'")
            __props__.__dict__["minimum_availability"] = minimum_availability
            if monitor is None and not opts.urn:
                raise TypeError("Missing required property 'monitor'")
            __props__.__dict__["monitor"] = monitor
            __props__.__dict__["name"] = name
            if quality_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'quality_profile_id'")
            __props__.__dict__["quality_profile_id"] = quality_profile_id
            if root_folder_path is None and not opts.urn:
                raise TypeError("Missing required property 'root_folder_path'")
            __props__.__dict__["root_folder_path"] = root_folder_path
            __props__.__dict__["search_on_add"] = search_on_add
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
        super(Stevenlu2, __self__).__init__(
            'radarr:ImportLists/stevenlu2:Stevenlu2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable_auto: Optional[pulumi.Input[bool]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            list_order: Optional[pulumi.Input[int]] = None,
            min_score: Optional[pulumi.Input[int]] = None,
            minimum_availability: Optional[pulumi.Input[str]] = None,
            monitor: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            quality_profile_id: Optional[pulumi.Input[int]] = None,
            root_folder_path: Optional[pulumi.Input[str]] = None,
            search_on_add: Optional[pulumi.Input[bool]] = None,
            source: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Stevenlu2':
        """
        Get an existing Stevenlu2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable_auto: Enable automatic add flag.
        :param pulumi.Input[bool] enabled: Enabled flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] min_score: Min score.
        :param pulumi.Input[str] minimum_availability: Minimum availability.
        :param pulumi.Input[str] monitor: Should monitor.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] search_on_add: Search on add flag.
        :param pulumi.Input[int] source: Source.`0` Standard, `1` Imdb, `2` Metacritic, `3` RottenTomatoes,
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _Stevenlu2State.__new__(_Stevenlu2State)

        __props__.__dict__["enable_auto"] = enable_auto
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["list_order"] = list_order
        __props__.__dict__["min_score"] = min_score
        __props__.__dict__["minimum_availability"] = minimum_availability
        __props__.__dict__["monitor"] = monitor
        __props__.__dict__["name"] = name
        __props__.__dict__["quality_profile_id"] = quality_profile_id
        __props__.__dict__["root_folder_path"] = root_folder_path
        __props__.__dict__["search_on_add"] = search_on_add
        __props__.__dict__["source"] = source
        __props__.__dict__["tags"] = tags
        return Stevenlu2(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter(name="listOrder")
    def list_order(self) -> pulumi.Output[int]:
        """
        List order.
        """
        return pulumi.get(self, "list_order")

    @property
    @pulumi.getter(name="minScore")
    def min_score(self) -> pulumi.Output[int]:
        """
        Min score.
        """
        return pulumi.get(self, "min_score")

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
    def source(self) -> pulumi.Output[int]:
        """
        Source.`0` Standard, `1` Imdb, `2` Metacritic, `3` RottenTomatoes,
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

