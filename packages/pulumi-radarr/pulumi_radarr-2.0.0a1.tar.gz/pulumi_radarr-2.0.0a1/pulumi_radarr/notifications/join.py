# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['JoinArgs', 'Join']

@pulumi.input_type
class JoinArgs:
    def __init__(__self__, *,
                 on_movie_delete: pulumi.Input[bool],
                 api_key: Optional[pulumi.Input[str]] = None,
                 device_names: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_download: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 on_manual_interaction_required: Optional[pulumi.Input[bool]] = None,
                 on_movie_added: Optional[pulumi.Input[bool]] = None,
                 on_movie_file_delete: Optional[pulumi.Input[bool]] = None,
                 on_movie_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Join resource.
        :param pulumi.Input[bool] on_movie_delete: On movie delete flag.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] device_names: Device names. Comma separated list.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: NotificationJoin name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_download: On download flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[bool] on_manual_interaction_required: On manual interaction required flag.
        :param pulumi.Input[bool] on_movie_added: On movie added flag.
        :param pulumi.Input[bool] on_movie_file_delete: On movie file delete flag.
        :param pulumi.Input[bool] on_movie_file_delete_for_upgrade: On movie file delete for upgrade flag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[int] priority: Priority. `-2` Silent, `-1` Quiet, `0` Normal, `1` High, `2` Emergency.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "on_movie_delete", on_movie_delete)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if device_names is not None:
            pulumi.set(__self__, "device_names", device_names)
        if include_health_warnings is not None:
            pulumi.set(__self__, "include_health_warnings", include_health_warnings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if on_application_update is not None:
            pulumi.set(__self__, "on_application_update", on_application_update)
        if on_download is not None:
            pulumi.set(__self__, "on_download", on_download)
        if on_grab is not None:
            pulumi.set(__self__, "on_grab", on_grab)
        if on_health_issue is not None:
            pulumi.set(__self__, "on_health_issue", on_health_issue)
        if on_health_restored is not None:
            pulumi.set(__self__, "on_health_restored", on_health_restored)
        if on_manual_interaction_required is not None:
            pulumi.set(__self__, "on_manual_interaction_required", on_manual_interaction_required)
        if on_movie_added is not None:
            pulumi.set(__self__, "on_movie_added", on_movie_added)
        if on_movie_file_delete is not None:
            pulumi.set(__self__, "on_movie_file_delete", on_movie_file_delete)
        if on_movie_file_delete_for_upgrade is not None:
            pulumi.set(__self__, "on_movie_file_delete_for_upgrade", on_movie_file_delete_for_upgrade)
        if on_upgrade is not None:
            pulumi.set(__self__, "on_upgrade", on_upgrade)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="onMovieDelete")
    def on_movie_delete(self) -> pulumi.Input[bool]:
        """
        On movie delete flag.
        """
        return pulumi.get(self, "on_movie_delete")

    @on_movie_delete.setter
    def on_movie_delete(self, value: pulumi.Input[bool]):
        pulumi.set(self, "on_movie_delete", value)

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
    @pulumi.getter(name="deviceNames")
    def device_names(self) -> Optional[pulumi.Input[str]]:
        """
        Device names. Comma separated list.
        """
        return pulumi.get(self, "device_names")

    @device_names.setter
    def device_names(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_names", value)

    @property
    @pulumi.getter(name="includeHealthWarnings")
    def include_health_warnings(self) -> Optional[pulumi.Input[bool]]:
        """
        Include health warnings.
        """
        return pulumi.get(self, "include_health_warnings")

    @include_health_warnings.setter
    def include_health_warnings(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_health_warnings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        NotificationJoin name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="onApplicationUpdate")
    def on_application_update(self) -> Optional[pulumi.Input[bool]]:
        """
        On application update flag.
        """
        return pulumi.get(self, "on_application_update")

    @on_application_update.setter
    def on_application_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_application_update", value)

    @property
    @pulumi.getter(name="onDownload")
    def on_download(self) -> Optional[pulumi.Input[bool]]:
        """
        On download flag.
        """
        return pulumi.get(self, "on_download")

    @on_download.setter
    def on_download(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_download", value)

    @property
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> Optional[pulumi.Input[bool]]:
        """
        On grab flag.
        """
        return pulumi.get(self, "on_grab")

    @on_grab.setter
    def on_grab(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_grab", value)

    @property
    @pulumi.getter(name="onHealthIssue")
    def on_health_issue(self) -> Optional[pulumi.Input[bool]]:
        """
        On health issue flag.
        """
        return pulumi.get(self, "on_health_issue")

    @on_health_issue.setter
    def on_health_issue(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_issue", value)

    @property
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> Optional[pulumi.Input[bool]]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @on_health_restored.setter
    def on_health_restored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_restored", value)

    @property
    @pulumi.getter(name="onManualInteractionRequired")
    def on_manual_interaction_required(self) -> Optional[pulumi.Input[bool]]:
        """
        On manual interaction required flag.
        """
        return pulumi.get(self, "on_manual_interaction_required")

    @on_manual_interaction_required.setter
    def on_manual_interaction_required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_manual_interaction_required", value)

    @property
    @pulumi.getter(name="onMovieAdded")
    def on_movie_added(self) -> Optional[pulumi.Input[bool]]:
        """
        On movie added flag.
        """
        return pulumi.get(self, "on_movie_added")

    @on_movie_added.setter
    def on_movie_added(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_movie_added", value)

    @property
    @pulumi.getter(name="onMovieFileDelete")
    def on_movie_file_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On movie file delete flag.
        """
        return pulumi.get(self, "on_movie_file_delete")

    @on_movie_file_delete.setter
    def on_movie_file_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_movie_file_delete", value)

    @property
    @pulumi.getter(name="onMovieFileDeleteForUpgrade")
    def on_movie_file_delete_for_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        On movie file delete for upgrade flag.
        """
        return pulumi.get(self, "on_movie_file_delete_for_upgrade")

    @on_movie_file_delete_for_upgrade.setter
    def on_movie_file_delete_for_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_movie_file_delete_for_upgrade", value)

    @property
    @pulumi.getter(name="onUpgrade")
    def on_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        On upgrade flag.
        """
        return pulumi.get(self, "on_upgrade")

    @on_upgrade.setter
    def on_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_upgrade", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority. `-2` Silent, `-1` Quiet, `0` Normal, `1` High, `2` Emergency.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

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
class _JoinState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 device_names: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_download: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 on_manual_interaction_required: Optional[pulumi.Input[bool]] = None,
                 on_movie_added: Optional[pulumi.Input[bool]] = None,
                 on_movie_delete: Optional[pulumi.Input[bool]] = None,
                 on_movie_file_delete: Optional[pulumi.Input[bool]] = None,
                 on_movie_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Join resources.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] device_names: Device names. Comma separated list.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: NotificationJoin name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_download: On download flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[bool] on_manual_interaction_required: On manual interaction required flag.
        :param pulumi.Input[bool] on_movie_added: On movie added flag.
        :param pulumi.Input[bool] on_movie_delete: On movie delete flag.
        :param pulumi.Input[bool] on_movie_file_delete: On movie file delete flag.
        :param pulumi.Input[bool] on_movie_file_delete_for_upgrade: On movie file delete for upgrade flag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[int] priority: Priority. `-2` Silent, `-1` Quiet, `0` Normal, `1` High, `2` Emergency.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if device_names is not None:
            pulumi.set(__self__, "device_names", device_names)
        if include_health_warnings is not None:
            pulumi.set(__self__, "include_health_warnings", include_health_warnings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if on_application_update is not None:
            pulumi.set(__self__, "on_application_update", on_application_update)
        if on_download is not None:
            pulumi.set(__self__, "on_download", on_download)
        if on_grab is not None:
            pulumi.set(__self__, "on_grab", on_grab)
        if on_health_issue is not None:
            pulumi.set(__self__, "on_health_issue", on_health_issue)
        if on_health_restored is not None:
            pulumi.set(__self__, "on_health_restored", on_health_restored)
        if on_manual_interaction_required is not None:
            pulumi.set(__self__, "on_manual_interaction_required", on_manual_interaction_required)
        if on_movie_added is not None:
            pulumi.set(__self__, "on_movie_added", on_movie_added)
        if on_movie_delete is not None:
            pulumi.set(__self__, "on_movie_delete", on_movie_delete)
        if on_movie_file_delete is not None:
            pulumi.set(__self__, "on_movie_file_delete", on_movie_file_delete)
        if on_movie_file_delete_for_upgrade is not None:
            pulumi.set(__self__, "on_movie_file_delete_for_upgrade", on_movie_file_delete_for_upgrade)
        if on_upgrade is not None:
            pulumi.set(__self__, "on_upgrade", on_upgrade)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="deviceNames")
    def device_names(self) -> Optional[pulumi.Input[str]]:
        """
        Device names. Comma separated list.
        """
        return pulumi.get(self, "device_names")

    @device_names.setter
    def device_names(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_names", value)

    @property
    @pulumi.getter(name="includeHealthWarnings")
    def include_health_warnings(self) -> Optional[pulumi.Input[bool]]:
        """
        Include health warnings.
        """
        return pulumi.get(self, "include_health_warnings")

    @include_health_warnings.setter
    def include_health_warnings(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_health_warnings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        NotificationJoin name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="onApplicationUpdate")
    def on_application_update(self) -> Optional[pulumi.Input[bool]]:
        """
        On application update flag.
        """
        return pulumi.get(self, "on_application_update")

    @on_application_update.setter
    def on_application_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_application_update", value)

    @property
    @pulumi.getter(name="onDownload")
    def on_download(self) -> Optional[pulumi.Input[bool]]:
        """
        On download flag.
        """
        return pulumi.get(self, "on_download")

    @on_download.setter
    def on_download(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_download", value)

    @property
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> Optional[pulumi.Input[bool]]:
        """
        On grab flag.
        """
        return pulumi.get(self, "on_grab")

    @on_grab.setter
    def on_grab(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_grab", value)

    @property
    @pulumi.getter(name="onHealthIssue")
    def on_health_issue(self) -> Optional[pulumi.Input[bool]]:
        """
        On health issue flag.
        """
        return pulumi.get(self, "on_health_issue")

    @on_health_issue.setter
    def on_health_issue(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_issue", value)

    @property
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> Optional[pulumi.Input[bool]]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @on_health_restored.setter
    def on_health_restored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_restored", value)

    @property
    @pulumi.getter(name="onManualInteractionRequired")
    def on_manual_interaction_required(self) -> Optional[pulumi.Input[bool]]:
        """
        On manual interaction required flag.
        """
        return pulumi.get(self, "on_manual_interaction_required")

    @on_manual_interaction_required.setter
    def on_manual_interaction_required(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_manual_interaction_required", value)

    @property
    @pulumi.getter(name="onMovieAdded")
    def on_movie_added(self) -> Optional[pulumi.Input[bool]]:
        """
        On movie added flag.
        """
        return pulumi.get(self, "on_movie_added")

    @on_movie_added.setter
    def on_movie_added(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_movie_added", value)

    @property
    @pulumi.getter(name="onMovieDelete")
    def on_movie_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On movie delete flag.
        """
        return pulumi.get(self, "on_movie_delete")

    @on_movie_delete.setter
    def on_movie_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_movie_delete", value)

    @property
    @pulumi.getter(name="onMovieFileDelete")
    def on_movie_file_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On movie file delete flag.
        """
        return pulumi.get(self, "on_movie_file_delete")

    @on_movie_file_delete.setter
    def on_movie_file_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_movie_file_delete", value)

    @property
    @pulumi.getter(name="onMovieFileDeleteForUpgrade")
    def on_movie_file_delete_for_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        On movie file delete for upgrade flag.
        """
        return pulumi.get(self, "on_movie_file_delete_for_upgrade")

    @on_movie_file_delete_for_upgrade.setter
    def on_movie_file_delete_for_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_movie_file_delete_for_upgrade", value)

    @property
    @pulumi.getter(name="onUpgrade")
    def on_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        On upgrade flag.
        """
        return pulumi.get(self, "on_upgrade")

    @on_upgrade.setter
    def on_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_upgrade", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority. `-2` Silent, `-1` Quiet, `0` Normal, `1` High, `2` Emergency.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

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


class Join(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 device_names: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_download: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 on_manual_interaction_required: Optional[pulumi.Input[bool]] = None,
                 on_movie_added: Optional[pulumi.Input[bool]] = None,
                 on_movie_delete: Optional[pulumi.Input[bool]] = None,
                 on_movie_file_delete: Optional[pulumi.Input[bool]] = None,
                 on_movie_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Notifications -->
        Notification Join resource.
        For more information refer to [Notification](https://wiki.servarr.com/radarr/settings#connect) and [Join](https://wiki.servarr.com/radarr/supported#join).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_radarr as radarr

        example = radarr.notifications.Join("example",
            api_key="Key",
            device_names="device1,device2",
            include_health_warnings=False,
            on_application_update=False,
            on_download=True,
            on_grab=False,
            on_health_issue=False,
            on_movie_added=False,
            on_movie_delete=False,
            on_movie_file_delete=False,
            on_movie_file_delete_for_upgrade=True,
            on_upgrade=True,
            priority=2)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import radarr:Notifications/join:Join example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] device_names: Device names. Comma separated list.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: NotificationJoin name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_download: On download flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[bool] on_manual_interaction_required: On manual interaction required flag.
        :param pulumi.Input[bool] on_movie_added: On movie added flag.
        :param pulumi.Input[bool] on_movie_delete: On movie delete flag.
        :param pulumi.Input[bool] on_movie_file_delete: On movie file delete flag.
        :param pulumi.Input[bool] on_movie_file_delete_for_upgrade: On movie file delete for upgrade flag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[int] priority: Priority. `-2` Silent, `-1` Quiet, `0` Normal, `1` High, `2` Emergency.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JoinArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Notifications -->
        Notification Join resource.
        For more information refer to [Notification](https://wiki.servarr.com/radarr/settings#connect) and [Join](https://wiki.servarr.com/radarr/supported#join).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_radarr as radarr

        example = radarr.notifications.Join("example",
            api_key="Key",
            device_names="device1,device2",
            include_health_warnings=False,
            on_application_update=False,
            on_download=True,
            on_grab=False,
            on_health_issue=False,
            on_movie_added=False,
            on_movie_delete=False,
            on_movie_file_delete=False,
            on_movie_file_delete_for_upgrade=True,
            on_upgrade=True,
            priority=2)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import radarr:Notifications/join:Join example 1
        ```

        :param str resource_name: The name of the resource.
        :param JoinArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JoinArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 device_names: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_download: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 on_manual_interaction_required: Optional[pulumi.Input[bool]] = None,
                 on_movie_added: Optional[pulumi.Input[bool]] = None,
                 on_movie_delete: Optional[pulumi.Input[bool]] = None,
                 on_movie_file_delete: Optional[pulumi.Input[bool]] = None,
                 on_movie_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JoinArgs.__new__(JoinArgs)

            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["device_names"] = device_names
            __props__.__dict__["include_health_warnings"] = include_health_warnings
            __props__.__dict__["name"] = name
            __props__.__dict__["on_application_update"] = on_application_update
            __props__.__dict__["on_download"] = on_download
            __props__.__dict__["on_grab"] = on_grab
            __props__.__dict__["on_health_issue"] = on_health_issue
            __props__.__dict__["on_health_restored"] = on_health_restored
            __props__.__dict__["on_manual_interaction_required"] = on_manual_interaction_required
            __props__.__dict__["on_movie_added"] = on_movie_added
            if on_movie_delete is None and not opts.urn:
                raise TypeError("Missing required property 'on_movie_delete'")
            __props__.__dict__["on_movie_delete"] = on_movie_delete
            __props__.__dict__["on_movie_file_delete"] = on_movie_file_delete
            __props__.__dict__["on_movie_file_delete_for_upgrade"] = on_movie_file_delete_for_upgrade
            __props__.__dict__["on_upgrade"] = on_upgrade
            __props__.__dict__["priority"] = priority
            __props__.__dict__["tags"] = tags
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Join, __self__).__init__(
            'radarr:Notifications/join:Join',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            device_names: Optional[pulumi.Input[str]] = None,
            include_health_warnings: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            on_application_update: Optional[pulumi.Input[bool]] = None,
            on_download: Optional[pulumi.Input[bool]] = None,
            on_grab: Optional[pulumi.Input[bool]] = None,
            on_health_issue: Optional[pulumi.Input[bool]] = None,
            on_health_restored: Optional[pulumi.Input[bool]] = None,
            on_manual_interaction_required: Optional[pulumi.Input[bool]] = None,
            on_movie_added: Optional[pulumi.Input[bool]] = None,
            on_movie_delete: Optional[pulumi.Input[bool]] = None,
            on_movie_file_delete: Optional[pulumi.Input[bool]] = None,
            on_movie_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
            on_upgrade: Optional[pulumi.Input[bool]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Join':
        """
        Get an existing Join resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] device_names: Device names. Comma separated list.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: NotificationJoin name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_download: On download flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[bool] on_manual_interaction_required: On manual interaction required flag.
        :param pulumi.Input[bool] on_movie_added: On movie added flag.
        :param pulumi.Input[bool] on_movie_delete: On movie delete flag.
        :param pulumi.Input[bool] on_movie_file_delete: On movie file delete flag.
        :param pulumi.Input[bool] on_movie_file_delete_for_upgrade: On movie file delete for upgrade flag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[int] priority: Priority. `-2` Silent, `-1` Quiet, `0` Normal, `1` High, `2` Emergency.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _JoinState.__new__(_JoinState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["device_names"] = device_names
        __props__.__dict__["include_health_warnings"] = include_health_warnings
        __props__.__dict__["name"] = name
        __props__.__dict__["on_application_update"] = on_application_update
        __props__.__dict__["on_download"] = on_download
        __props__.__dict__["on_grab"] = on_grab
        __props__.__dict__["on_health_issue"] = on_health_issue
        __props__.__dict__["on_health_restored"] = on_health_restored
        __props__.__dict__["on_manual_interaction_required"] = on_manual_interaction_required
        __props__.__dict__["on_movie_added"] = on_movie_added
        __props__.__dict__["on_movie_delete"] = on_movie_delete
        __props__.__dict__["on_movie_file_delete"] = on_movie_file_delete
        __props__.__dict__["on_movie_file_delete_for_upgrade"] = on_movie_file_delete_for_upgrade
        __props__.__dict__["on_upgrade"] = on_upgrade
        __props__.__dict__["priority"] = priority
        __props__.__dict__["tags"] = tags
        return Join(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="deviceNames")
    def device_names(self) -> pulumi.Output[Optional[str]]:
        """
        Device names. Comma separated list.
        """
        return pulumi.get(self, "device_names")

    @property
    @pulumi.getter(name="includeHealthWarnings")
    def include_health_warnings(self) -> pulumi.Output[bool]:
        """
        Include health warnings.
        """
        return pulumi.get(self, "include_health_warnings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        NotificationJoin name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="onApplicationUpdate")
    def on_application_update(self) -> pulumi.Output[bool]:
        """
        On application update flag.
        """
        return pulumi.get(self, "on_application_update")

    @property
    @pulumi.getter(name="onDownload")
    def on_download(self) -> pulumi.Output[bool]:
        """
        On download flag.
        """
        return pulumi.get(self, "on_download")

    @property
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> pulumi.Output[bool]:
        """
        On grab flag.
        """
        return pulumi.get(self, "on_grab")

    @property
    @pulumi.getter(name="onHealthIssue")
    def on_health_issue(self) -> pulumi.Output[bool]:
        """
        On health issue flag.
        """
        return pulumi.get(self, "on_health_issue")

    @property
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> pulumi.Output[bool]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @property
    @pulumi.getter(name="onManualInteractionRequired")
    def on_manual_interaction_required(self) -> pulumi.Output[bool]:
        """
        On manual interaction required flag.
        """
        return pulumi.get(self, "on_manual_interaction_required")

    @property
    @pulumi.getter(name="onMovieAdded")
    def on_movie_added(self) -> pulumi.Output[bool]:
        """
        On movie added flag.
        """
        return pulumi.get(self, "on_movie_added")

    @property
    @pulumi.getter(name="onMovieDelete")
    def on_movie_delete(self) -> pulumi.Output[bool]:
        """
        On movie delete flag.
        """
        return pulumi.get(self, "on_movie_delete")

    @property
    @pulumi.getter(name="onMovieFileDelete")
    def on_movie_file_delete(self) -> pulumi.Output[bool]:
        """
        On movie file delete flag.
        """
        return pulumi.get(self, "on_movie_file_delete")

    @property
    @pulumi.getter(name="onMovieFileDeleteForUpgrade")
    def on_movie_file_delete_for_upgrade(self) -> pulumi.Output[bool]:
        """
        On movie file delete for upgrade flag.
        """
        return pulumi.get(self, "on_movie_file_delete_for_upgrade")

    @property
    @pulumi.getter(name="onUpgrade")
    def on_upgrade(self) -> pulumi.Output[bool]:
        """
        On upgrade flag.
        """
        return pulumi.get(self, "on_upgrade")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Priority. `-2` Silent, `-1` Quiet, `0` Normal, `1` High, `2` Emergency.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

