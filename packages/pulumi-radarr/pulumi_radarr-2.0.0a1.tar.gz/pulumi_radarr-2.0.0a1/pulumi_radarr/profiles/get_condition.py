# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetConditionResult',
    'AwaitableGetConditionResult',
    'get_condition',
    'get_condition_output',
]

@pulumi.output_type
class GetConditionResult:
    """
    A collection of values returned by getCondition.
    """
    def __init__(__self__, id=None, implementation=None, max=None, min=None, name=None, negate=None, required=None, value=None):
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if implementation and not isinstance(implementation, str):
            raise TypeError("Expected argument 'implementation' to be a str")
        pulumi.set(__self__, "implementation", implementation)
        if max and not isinstance(max, int):
            raise TypeError("Expected argument 'max' to be a int")
        pulumi.set(__self__, "max", max)
        if min and not isinstance(min, int):
            raise TypeError("Expected argument 'min' to be a int")
        pulumi.set(__self__, "min", min)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if negate and not isinstance(negate, bool):
            raise TypeError("Expected argument 'negate' to be a bool")
        pulumi.set(__self__, "negate", negate)
        if required and not isinstance(required, bool):
            raise TypeError("Expected argument 'required' to be a bool")
        pulumi.set(__self__, "required", required)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Custom format condition ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def implementation(self) -> str:
        """
        Implementation.
        """
        return pulumi.get(self, "implementation")

    @property
    @pulumi.getter
    def max(self) -> int:
        """
        Max.
        """
        return pulumi.get(self, "max")

    @property
    @pulumi.getter
    def min(self) -> int:
        """
        Min.
        """
        return pulumi.get(self, "min")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Specification name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def negate(self) -> bool:
        """
        Negate flag.
        """
        return pulumi.get(self, "negate")

    @property
    @pulumi.getter
    def required(self) -> bool:
        """
        Computed flag.
        """
        return pulumi.get(self, "required")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Value.
        """
        return pulumi.get(self, "value")


class AwaitableGetConditionResult(GetConditionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConditionResult(
            id=self.id,
            implementation=self.implementation,
            max=self.max,
            min=self.min,
            name=self.name,
            negate=self.negate,
            required=self.required,
            value=self.value)


def get_condition(implementation: Optional[str] = None,
                  max: Optional[int] = None,
                  min: Optional[int] = None,
                  name: Optional[str] = None,
                  negate: Optional[bool] = None,
                  required: Optional[bool] = None,
                  value: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConditionResult:
    """
    <!-- subcategory:Profiles -->
     Generic Custom Format Condition data source. When possible use a specific data source instead.
    For more information refer to [Custom Format Conditions](https://wiki.servarr.com/radarr/settings#conditions).
     To be used in conjunction with Custom Format.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_radarr as radarr

    example_condition = radarr.Profiles.get_condition(name="Example",
        implementation="SizeSpecification",
        negate=False,
        required=False,
        min=0,
        max=100)
    example_custom_format = radarr.profiles.CustomFormat("exampleCustomFormat",
        include_custom_format_when_renaming=False,
        specifications=[example_condition])
    ```


    :param str implementation: Implementation.
    :param int max: Max.
    :param int min: Min.
    :param str name: Specification name.
    :param bool negate: Negate flag.
    :param bool required: Computed flag.
    :param str value: Value.
    """
    __args__ = dict()
    __args__['implementation'] = implementation
    __args__['max'] = max
    __args__['min'] = min
    __args__['name'] = name
    __args__['negate'] = negate
    __args__['required'] = required
    __args__['value'] = value
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('radarr:Profiles/getCondition:getCondition', __args__, opts=opts, typ=GetConditionResult).value

    return AwaitableGetConditionResult(
        id=pulumi.get(__ret__, 'id'),
        implementation=pulumi.get(__ret__, 'implementation'),
        max=pulumi.get(__ret__, 'max'),
        min=pulumi.get(__ret__, 'min'),
        name=pulumi.get(__ret__, 'name'),
        negate=pulumi.get(__ret__, 'negate'),
        required=pulumi.get(__ret__, 'required'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_condition)
def get_condition_output(implementation: Optional[pulumi.Input[str]] = None,
                         max: Optional[pulumi.Input[Optional[int]]] = None,
                         min: Optional[pulumi.Input[Optional[int]]] = None,
                         name: Optional[pulumi.Input[str]] = None,
                         negate: Optional[pulumi.Input[bool]] = None,
                         required: Optional[pulumi.Input[bool]] = None,
                         value: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConditionResult]:
    """
    <!-- subcategory:Profiles -->
     Generic Custom Format Condition data source. When possible use a specific data source instead.
    For more information refer to [Custom Format Conditions](https://wiki.servarr.com/radarr/settings#conditions).
     To be used in conjunction with Custom Format.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_radarr as radarr

    example_condition = radarr.Profiles.get_condition(name="Example",
        implementation="SizeSpecification",
        negate=False,
        required=False,
        min=0,
        max=100)
    example_custom_format = radarr.profiles.CustomFormat("exampleCustomFormat",
        include_custom_format_when_renaming=False,
        specifications=[example_condition])
    ```


    :param str implementation: Implementation.
    :param int max: Max.
    :param int min: Min.
    :param str name: Specification name.
    :param bool negate: Negate flag.
    :param bool required: Computed flag.
    :param str value: Value.
    """
    ...
