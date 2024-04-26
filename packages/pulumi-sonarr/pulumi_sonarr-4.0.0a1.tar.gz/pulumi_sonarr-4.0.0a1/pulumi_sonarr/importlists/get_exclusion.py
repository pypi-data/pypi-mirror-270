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
    'GetExclusionResult',
    'AwaitableGetExclusionResult',
    'get_exclusion',
    'get_exclusion_output',
]

@pulumi.output_type
class GetExclusionResult:
    """
    A collection of values returned by getExclusion.
    """
    def __init__(__self__, id=None, title=None, tvdb_id=None):
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if tvdb_id and not isinstance(tvdb_id, int):
            raise TypeError("Expected argument 'tvdb_id' to be a int")
        pulumi.set(__self__, "tvdb_id", tvdb_id)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        ImportListExclusion ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Series to be excluded.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="tvdbId")
    def tvdb_id(self) -> int:
        """
        Series TVDB ID.
        """
        return pulumi.get(self, "tvdb_id")


class AwaitableGetExclusionResult(GetExclusionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExclusionResult(
            id=self.id,
            title=self.title,
            tvdb_id=self.tvdb_id)


def get_exclusion(tvdb_id: Optional[int] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExclusionResult:
    """
    <!-- subcategory:Import Lists -->
    Single ImportListExclusion.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example = sonarr.ImportLists.get_exclusion(tvdb_id=987)
    ```


    :param int tvdb_id: Series TVDB ID.
    """
    __args__ = dict()
    __args__['tvdbId'] = tvdb_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sonarr:ImportLists/getExclusion:getExclusion', __args__, opts=opts, typ=GetExclusionResult).value

    return AwaitableGetExclusionResult(
        id=pulumi.get(__ret__, 'id'),
        title=pulumi.get(__ret__, 'title'),
        tvdb_id=pulumi.get(__ret__, 'tvdb_id'))


@_utilities.lift_output_func(get_exclusion)
def get_exclusion_output(tvdb_id: Optional[pulumi.Input[int]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExclusionResult]:
    """
    <!-- subcategory:Import Lists -->
    Single ImportListExclusion.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example = sonarr.ImportLists.get_exclusion(tvdb_id=987)
    ```


    :param int tvdb_id: Series TVDB ID.
    """
    ...
