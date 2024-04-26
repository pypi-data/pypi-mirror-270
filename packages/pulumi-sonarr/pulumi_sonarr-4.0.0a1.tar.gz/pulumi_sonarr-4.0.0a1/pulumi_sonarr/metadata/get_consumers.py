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
    'GetConsumersResult',
    'AwaitableGetConsumersResult',
    'get_consumers',
    'get_consumers_output',
]

@pulumi.output_type
class GetConsumersResult:
    """
    A collection of values returned by getConsumers.
    """
    def __init__(__self__, id=None, metadata_consumers=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata_consumers and not isinstance(metadata_consumers, list):
            raise TypeError("Expected argument 'metadata_consumers' to be a list")
        pulumi.set(__self__, "metadata_consumers", metadata_consumers)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="metadataConsumers")
    def metadata_consumers(self) -> Sequence['outputs.GetConsumersMetadataConsumerResult']:
        """
        MetadataConsumer list.
        """
        return pulumi.get(self, "metadata_consumers")


class AwaitableGetConsumersResult(GetConsumersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConsumersResult(
            id=self.id,
            metadata_consumers=self.metadata_consumers)


def get_consumers(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConsumersResult:
    """
    <!-- subcategory:Metadata -->
    List all available Metadata Consumers.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example = sonarr.Metadata.get_consumers()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sonarr:Metadata/getConsumers:getConsumers', __args__, opts=opts, typ=GetConsumersResult).value

    return AwaitableGetConsumersResult(
        id=pulumi.get(__ret__, 'id'),
        metadata_consumers=pulumi.get(__ret__, 'metadata_consumers'))


@_utilities.lift_output_func(get_consumers)
def get_consumers_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConsumersResult]:
    """
    <!-- subcategory:Metadata -->
    List all available Metadata Consumers.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example = sonarr.Metadata.get_consumers()
    ```
    """
    ...
