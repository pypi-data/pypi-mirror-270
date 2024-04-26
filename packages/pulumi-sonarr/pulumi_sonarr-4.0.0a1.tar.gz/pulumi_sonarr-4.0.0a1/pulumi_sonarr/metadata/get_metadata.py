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
    'GetMetadataResult',
    'AwaitableGetMetadataResult',
    'get_metadata',
    'get_metadata_output',
]

@pulumi.output_type
class GetMetadataResult:
    """
    A collection of values returned by getMetadata.
    """
    def __init__(__self__, config_contract=None, enable=None, episode_images=None, episode_metadata=None, id=None, implementation=None, name=None, season_images=None, series_images=None, series_metadata=None, series_metadata_url=None, tags=None):
        if config_contract and not isinstance(config_contract, str):
            raise TypeError("Expected argument 'config_contract' to be a str")
        pulumi.set(__self__, "config_contract", config_contract)
        if enable and not isinstance(enable, bool):
            raise TypeError("Expected argument 'enable' to be a bool")
        pulumi.set(__self__, "enable", enable)
        if episode_images and not isinstance(episode_images, bool):
            raise TypeError("Expected argument 'episode_images' to be a bool")
        pulumi.set(__self__, "episode_images", episode_images)
        if episode_metadata and not isinstance(episode_metadata, bool):
            raise TypeError("Expected argument 'episode_metadata' to be a bool")
        pulumi.set(__self__, "episode_metadata", episode_metadata)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if implementation and not isinstance(implementation, str):
            raise TypeError("Expected argument 'implementation' to be a str")
        pulumi.set(__self__, "implementation", implementation)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if season_images and not isinstance(season_images, bool):
            raise TypeError("Expected argument 'season_images' to be a bool")
        pulumi.set(__self__, "season_images", season_images)
        if series_images and not isinstance(series_images, bool):
            raise TypeError("Expected argument 'series_images' to be a bool")
        pulumi.set(__self__, "series_images", series_images)
        if series_metadata and not isinstance(series_metadata, bool):
            raise TypeError("Expected argument 'series_metadata' to be a bool")
        pulumi.set(__self__, "series_metadata", series_metadata)
        if series_metadata_url and not isinstance(series_metadata_url, bool):
            raise TypeError("Expected argument 'series_metadata_url' to be a bool")
        pulumi.set(__self__, "series_metadata_url", series_metadata_url)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> str:
        """
        Metadata configuration template.
        """
        return pulumi.get(self, "config_contract")

    @property
    @pulumi.getter
    def enable(self) -> bool:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter(name="episodeImages")
    def episode_images(self) -> Optional[bool]:
        """
        Episode images flag.
        """
        return pulumi.get(self, "episode_images")

    @property
    @pulumi.getter(name="episodeMetadata")
    def episode_metadata(self) -> bool:
        """
        Episode metadata flag.
        """
        return pulumi.get(self, "episode_metadata")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Metadata ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def implementation(self) -> str:
        """
        Metadata implementation name.
        """
        return pulumi.get(self, "implementation")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="seasonImages")
    def season_images(self) -> bool:
        """
        Season images flag.
        """
        return pulumi.get(self, "season_images")

    @property
    @pulumi.getter(name="seriesImages")
    def series_images(self) -> bool:
        """
        Series images flag.
        """
        return pulumi.get(self, "series_images")

    @property
    @pulumi.getter(name="seriesMetadata")
    def series_metadata(self) -> bool:
        """
        Series metadata flag.
        """
        return pulumi.get(self, "series_metadata")

    @property
    @pulumi.getter(name="seriesMetadataUrl")
    def series_metadata_url(self) -> bool:
        """
        Series metadata URL flag.
        """
        return pulumi.get(self, "series_metadata_url")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[int]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")


class AwaitableGetMetadataResult(GetMetadataResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetadataResult(
            config_contract=self.config_contract,
            enable=self.enable,
            episode_images=self.episode_images,
            episode_metadata=self.episode_metadata,
            id=self.id,
            implementation=self.implementation,
            name=self.name,
            season_images=self.season_images,
            series_images=self.series_images,
            series_metadata=self.series_metadata,
            series_metadata_url=self.series_metadata_url,
            tags=self.tags)


def get_metadata(episode_images: Optional[bool] = None,
                 name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetadataResult:
    """
    <!-- subcategory:Metadata -->
    Single Metadata.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example = sonarr.Metadata.get_metadata(name="Example")
    ```


    :param bool episode_images: Episode images flag.
    :param str name: Metadata name.
    """
    __args__ = dict()
    __args__['episodeImages'] = episode_images
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('sonarr:Metadata/getMetadata:getMetadata', __args__, opts=opts, typ=GetMetadataResult).value

    return AwaitableGetMetadataResult(
        config_contract=pulumi.get(__ret__, 'config_contract'),
        enable=pulumi.get(__ret__, 'enable'),
        episode_images=pulumi.get(__ret__, 'episode_images'),
        episode_metadata=pulumi.get(__ret__, 'episode_metadata'),
        id=pulumi.get(__ret__, 'id'),
        implementation=pulumi.get(__ret__, 'implementation'),
        name=pulumi.get(__ret__, 'name'),
        season_images=pulumi.get(__ret__, 'season_images'),
        series_images=pulumi.get(__ret__, 'series_images'),
        series_metadata=pulumi.get(__ret__, 'series_metadata'),
        series_metadata_url=pulumi.get(__ret__, 'series_metadata_url'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_metadata)
def get_metadata_output(episode_images: Optional[pulumi.Input[Optional[bool]]] = None,
                        name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetadataResult]:
    """
    <!-- subcategory:Metadata -->
    Single Metadata.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_sonarr as sonarr

    example = sonarr.Metadata.get_metadata(name="Example")
    ```


    :param bool episode_images: Episode images flag.
    :param str name: Metadata name.
    """
    ...
