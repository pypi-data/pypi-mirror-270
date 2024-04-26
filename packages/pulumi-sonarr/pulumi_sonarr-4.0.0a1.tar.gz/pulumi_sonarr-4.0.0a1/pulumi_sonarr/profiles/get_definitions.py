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
    'GetDefinitionsResult',
    'AwaitableGetDefinitionsResult',
    'get_definitions',
    'get_definitions_output',
]

@pulumi.output_type
class GetDefinitionsResult:
    """
    A collection of values returned by getDefinitions.
    """
    def __init__(__self__, id=None, quality_definitions=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if quality_definitions and not isinstance(quality_definitions, list):
            raise TypeError("Expected argument 'quality_definitions' to be a list")
        pulumi.set(__self__, "quality_definitions", quality_definitions)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="qualityDefinitions")
    def quality_definitions(self) -> Sequence['outputs.GetDefinitionsQualityDefinitionResult']:
        """
        Quality Definition list.
        """
        return pulumi.get(self, "quality_definitions")


class AwaitableGetDefinitionsResult(GetDefinitionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDefinitionsResult(
            id=self.id,
            quality_definitions=self.quality_definitions)


def get_definitions(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDefinitionsResult:
    """
    <!-- subcategory:Profiles -->
    List all available Quality Definitions.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example = sonarr.Profiles.get_definitions()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sonarr:Profiles/getDefinitions:getDefinitions', __args__, opts=opts, typ=GetDefinitionsResult).value

    return AwaitableGetDefinitionsResult(
        id=pulumi.get(__ret__, 'id'),
        quality_definitions=pulumi.get(__ret__, 'quality_definitions'))


@_utilities.lift_output_func(get_definitions)
def get_definitions_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDefinitionsResult]:
    """
    <!-- subcategory:Profiles -->
    List all available Quality Definitions.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example = sonarr.Profiles.get_definitions()
    ```
    """
    ...
