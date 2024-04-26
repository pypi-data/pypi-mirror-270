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
    'GetConditionReleaseGroupResult',
    'AwaitableGetConditionReleaseGroupResult',
    'get_condition_release_group',
    'get_condition_release_group_output',
]

@pulumi.output_type
class GetConditionReleaseGroupResult:
    """
    A collection of values returned by getConditionReleaseGroup.
    """
    def __init__(__self__, id=None, implementation=None, name=None, negate=None, required=None, value=None):
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if implementation and not isinstance(implementation, str):
            raise TypeError("Expected argument 'implementation' to be a str")
        pulumi.set(__self__, "implementation", implementation)
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
        Custom format condition release group ID.
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
        Release group RegEx.
        """
        return pulumi.get(self, "value")


class AwaitableGetConditionReleaseGroupResult(GetConditionReleaseGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConditionReleaseGroupResult(
            id=self.id,
            implementation=self.implementation,
            name=self.name,
            negate=self.negate,
            required=self.required,
            value=self.value)


def get_condition_release_group(name: Optional[str] = None,
                                negate: Optional[bool] = None,
                                required: Optional[bool] = None,
                                value: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConditionReleaseGroupResult:
    """
    <!-- subcategory:Profiles -->
     Custom Format Condition Release Group data source.
    For more information refer to [Custom Format Conditions](https://wiki.servarr.com/sonarr/settings#conditions).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example_condition_release_group = sonarr.Profiles.get_condition_release_group(name="HDBits",
        negate=False,
        required=False,
        value=".*HDBits.*")
    example_custom_format = sonarr.profiles.CustomFormat("exampleCustomFormat",
        include_custom_format_when_renaming=False,
        specifications=[example_condition_release_group])
    ```


    :param str name: Specification name.
    :param bool negate: Negate flag.
    :param bool required: Computed flag.
    :param str value: Release group RegEx.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['negate'] = negate
    __args__['required'] = required
    __args__['value'] = value
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sonarr:Profiles/getConditionReleaseGroup:getConditionReleaseGroup', __args__, opts=opts, typ=GetConditionReleaseGroupResult).value

    return AwaitableGetConditionReleaseGroupResult(
        id=pulumi.get(__ret__, 'id'),
        implementation=pulumi.get(__ret__, 'implementation'),
        name=pulumi.get(__ret__, 'name'),
        negate=pulumi.get(__ret__, 'negate'),
        required=pulumi.get(__ret__, 'required'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_condition_release_group)
def get_condition_release_group_output(name: Optional[pulumi.Input[str]] = None,
                                       negate: Optional[pulumi.Input[bool]] = None,
                                       required: Optional[pulumi.Input[bool]] = None,
                                       value: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConditionReleaseGroupResult]:
    """
    <!-- subcategory:Profiles -->
     Custom Format Condition Release Group data source.
    For more information refer to [Custom Format Conditions](https://wiki.servarr.com/sonarr/settings#conditions).

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example_condition_release_group = sonarr.Profiles.get_condition_release_group(name="HDBits",
        negate=False,
        required=False,
        value=".*HDBits.*")
    example_custom_format = sonarr.profiles.CustomFormat("exampleCustomFormat",
        include_custom_format_when_renaming=False,
        specifications=[example_condition_release_group])
    ```


    :param str name: Specification name.
    :param bool negate: Negate flag.
    :param bool required: Computed flag.
    :param str value: Release group RegEx.
    """
    ...
