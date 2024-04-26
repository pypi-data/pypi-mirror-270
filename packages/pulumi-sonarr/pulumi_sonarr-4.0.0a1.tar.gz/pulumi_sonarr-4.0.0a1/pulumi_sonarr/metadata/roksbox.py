# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RoksboxArgs', 'Roksbox']

@pulumi.input_type
class RoksboxArgs:
    def __init__(__self__, *,
                 episode_images: pulumi.Input[bool],
                 episode_metadata: pulumi.Input[bool],
                 season_images: pulumi.Input[bool],
                 series_images: pulumi.Input[bool],
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Roksbox resource.
        :param pulumi.Input[bool] episode_images: Episode images flag.
        :param pulumi.Input[bool] episode_metadata: Episode metadata flag.
        :param pulumi.Input[bool] season_images: Season images flag.
        :param pulumi.Input[bool] series_images: Series images flag.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "episode_images", episode_images)
        pulumi.set(__self__, "episode_metadata", episode_metadata)
        pulumi.set(__self__, "season_images", season_images)
        pulumi.set(__self__, "series_images", series_images)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="episodeImages")
    def episode_images(self) -> pulumi.Input[bool]:
        """
        Episode images flag.
        """
        return pulumi.get(self, "episode_images")

    @episode_images.setter
    def episode_images(self, value: pulumi.Input[bool]):
        pulumi.set(self, "episode_images", value)

    @property
    @pulumi.getter(name="episodeMetadata")
    def episode_metadata(self) -> pulumi.Input[bool]:
        """
        Episode metadata flag.
        """
        return pulumi.get(self, "episode_metadata")

    @episode_metadata.setter
    def episode_metadata(self, value: pulumi.Input[bool]):
        pulumi.set(self, "episode_metadata", value)

    @property
    @pulumi.getter(name="seasonImages")
    def season_images(self) -> pulumi.Input[bool]:
        """
        Season images flag.
        """
        return pulumi.get(self, "season_images")

    @season_images.setter
    def season_images(self, value: pulumi.Input[bool]):
        pulumi.set(self, "season_images", value)

    @property
    @pulumi.getter(name="seriesImages")
    def series_images(self) -> pulumi.Input[bool]:
        """
        Series images flag.
        """
        return pulumi.get(self, "series_images")

    @series_images.setter
    def series_images(self, value: pulumi.Input[bool]):
        pulumi.set(self, "series_images", value)

    @property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
class _RoksboxState:
    def __init__(__self__, *,
                 enable: Optional[pulumi.Input[bool]] = None,
                 episode_images: Optional[pulumi.Input[bool]] = None,
                 episode_metadata: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 season_images: Optional[pulumi.Input[bool]] = None,
                 series_images: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Roksbox resources.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[bool] episode_images: Episode images flag.
        :param pulumi.Input[bool] episode_metadata: Episode metadata flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[bool] season_images: Season images flag.
        :param pulumi.Input[bool] series_images: Series images flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if episode_images is not None:
            pulumi.set(__self__, "episode_images", episode_images)
        if episode_metadata is not None:
            pulumi.set(__self__, "episode_metadata", episode_metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if season_images is not None:
            pulumi.set(__self__, "season_images", season_images)
        if series_images is not None:
            pulumi.set(__self__, "series_images", series_images)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter(name="episodeImages")
    def episode_images(self) -> Optional[pulumi.Input[bool]]:
        """
        Episode images flag.
        """
        return pulumi.get(self, "episode_images")

    @episode_images.setter
    def episode_images(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "episode_images", value)

    @property
    @pulumi.getter(name="episodeMetadata")
    def episode_metadata(self) -> Optional[pulumi.Input[bool]]:
        """
        Episode metadata flag.
        """
        return pulumi.get(self, "episode_metadata")

    @episode_metadata.setter
    def episode_metadata(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "episode_metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="seasonImages")
    def season_images(self) -> Optional[pulumi.Input[bool]]:
        """
        Season images flag.
        """
        return pulumi.get(self, "season_images")

    @season_images.setter
    def season_images(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "season_images", value)

    @property
    @pulumi.getter(name="seriesImages")
    def series_images(self) -> Optional[pulumi.Input[bool]]:
        """
        Series images flag.
        """
        return pulumi.get(self, "series_images")

    @series_images.setter
    def series_images(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "series_images", value)

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


class Roksbox(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 episode_images: Optional[pulumi.Input[bool]] = None,
                 episode_metadata: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 season_images: Optional[pulumi.Input[bool]] = None,
                 series_images: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Metadata -->
        Metadata Roksbox resource.
        For more information refer to [Metadata](https://wiki.servarr.com/sonarr/settings#metadata) and [ROKSBOX](https://wiki.servarr.com/sonarr/supported#roksboxmetadata).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sonarr as sonarr

        example = sonarr.metadata.Roksbox("example",
            enable=True,
            episode_images=False,
            episode_metadata=True,
            season_images=True,
            series_images=False)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import sonarr:Metadata/roksbox:Roksbox example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[bool] episode_images: Episode images flag.
        :param pulumi.Input[bool] episode_metadata: Episode metadata flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[bool] season_images: Season images flag.
        :param pulumi.Input[bool] series_images: Series images flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoksboxArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Metadata -->
        Metadata Roksbox resource.
        For more information refer to [Metadata](https://wiki.servarr.com/sonarr/settings#metadata) and [ROKSBOX](https://wiki.servarr.com/sonarr/supported#roksboxmetadata).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sonarr as sonarr

        example = sonarr.metadata.Roksbox("example",
            enable=True,
            episode_images=False,
            episode_metadata=True,
            season_images=True,
            series_images=False)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import sonarr:Metadata/roksbox:Roksbox example 1
        ```

        :param str resource_name: The name of the resource.
        :param RoksboxArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoksboxArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 episode_images: Optional[pulumi.Input[bool]] = None,
                 episode_metadata: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 season_images: Optional[pulumi.Input[bool]] = None,
                 series_images: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoksboxArgs.__new__(RoksboxArgs)

            __props__.__dict__["enable"] = enable
            if episode_images is None and not opts.urn:
                raise TypeError("Missing required property 'episode_images'")
            __props__.__dict__["episode_images"] = episode_images
            if episode_metadata is None and not opts.urn:
                raise TypeError("Missing required property 'episode_metadata'")
            __props__.__dict__["episode_metadata"] = episode_metadata
            __props__.__dict__["name"] = name
            if season_images is None and not opts.urn:
                raise TypeError("Missing required property 'season_images'")
            __props__.__dict__["season_images"] = season_images
            if series_images is None and not opts.urn:
                raise TypeError("Missing required property 'series_images'")
            __props__.__dict__["series_images"] = series_images
            __props__.__dict__["tags"] = tags
        super(Roksbox, __self__).__init__(
            'sonarr:Metadata/roksbox:Roksbox',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            episode_images: Optional[pulumi.Input[bool]] = None,
            episode_metadata: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            season_images: Optional[pulumi.Input[bool]] = None,
            series_images: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Roksbox':
        """
        Get an existing Roksbox resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[bool] episode_images: Episode images flag.
        :param pulumi.Input[bool] episode_metadata: Episode metadata flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[bool] season_images: Season images flag.
        :param pulumi.Input[bool] series_images: Series images flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoksboxState.__new__(_RoksboxState)

        __props__.__dict__["enable"] = enable
        __props__.__dict__["episode_images"] = episode_images
        __props__.__dict__["episode_metadata"] = episode_metadata
        __props__.__dict__["name"] = name
        __props__.__dict__["season_images"] = season_images
        __props__.__dict__["series_images"] = series_images
        __props__.__dict__["tags"] = tags
        return Roksbox(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter(name="episodeImages")
    def episode_images(self) -> pulumi.Output[bool]:
        """
        Episode images flag.
        """
        return pulumi.get(self, "episode_images")

    @property
    @pulumi.getter(name="episodeMetadata")
    def episode_metadata(self) -> pulumi.Output[bool]:
        """
        Episode metadata flag.
        """
        return pulumi.get(self, "episode_metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="seasonImages")
    def season_images(self) -> pulumi.Output[bool]:
        """
        Season images flag.
        """
        return pulumi.get(self, "season_images")

    @property
    @pulumi.getter(name="seriesImages")
    def series_images(self) -> pulumi.Output[bool]:
        """
        Series images flag.
        """
        return pulumi.get(self, "series_images")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

