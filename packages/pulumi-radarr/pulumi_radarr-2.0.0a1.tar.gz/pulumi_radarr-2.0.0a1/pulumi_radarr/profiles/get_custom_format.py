# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetCustomFormatResult',
    'AwaitableGetCustomFormatResult',
    'get_custom_format',
    'get_custom_format_output',
]

@pulumi.output_type
class GetCustomFormatResult:
    """
    A collection of values returned by getCustomFormat.
    """
    def __init__(__self__, id=None, include_custom_format_when_renaming=None, name=None, specifications=None):
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if include_custom_format_when_renaming and not isinstance(include_custom_format_when_renaming, bool):
            raise TypeError("Expected argument 'include_custom_format_when_renaming' to be a bool")
        pulumi.set(__self__, "include_custom_format_when_renaming", include_custom_format_when_renaming)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if specifications and not isinstance(specifications, list):
            raise TypeError("Expected argument 'specifications' to be a list")
        pulumi.set(__self__, "specifications", specifications)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Custom Format ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeCustomFormatWhenRenaming")
    def include_custom_format_when_renaming(self) -> bool:
        """
        Include custom format when renaming flag.
        """
        return pulumi.get(self, "include_custom_format_when_renaming")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Custom Format name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def specifications(self) -> Sequence['outputs.GetCustomFormatSpecificationResult']:
        """
        Specifications.
        """
        return pulumi.get(self, "specifications")


class AwaitableGetCustomFormatResult(GetCustomFormatResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomFormatResult(
            id=self.id,
            include_custom_format_when_renaming=self.include_custom_format_when_renaming,
            name=self.name,
            specifications=self.specifications)


def get_custom_format(name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomFormatResult:
    """
    <!-- subcategory:Profiles -->
    Single Custom Format.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_radarr as radarr

    example = radarr.Profiles.get_custom_format(name="Example")
    ```


    :param str name: Specification name.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('radarr:Profiles/getCustomFormat:getCustomFormat', __args__, opts=opts, typ=GetCustomFormatResult).value

    return AwaitableGetCustomFormatResult(
        id=pulumi.get(__ret__, 'id'),
        include_custom_format_when_renaming=pulumi.get(__ret__, 'include_custom_format_when_renaming'),
        name=pulumi.get(__ret__, 'name'),
        specifications=pulumi.get(__ret__, 'specifications'))


@_utilities.lift_output_func(get_custom_format)
def get_custom_format_output(name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomFormatResult]:
    """
    <!-- subcategory:Profiles -->
    Single Custom Format.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_radarr as radarr

    example = radarr.Profiles.get_custom_format(name="Example")
    ```


    :param str name: Specification name.
    """
    ...
