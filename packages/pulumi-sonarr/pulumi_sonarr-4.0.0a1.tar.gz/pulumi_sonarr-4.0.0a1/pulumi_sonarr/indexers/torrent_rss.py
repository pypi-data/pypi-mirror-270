# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TorrentRssArgs', 'TorrentRss']

@pulumi.input_type
class TorrentRssArgs:
    def __init__(__self__, *,
                 base_url: pulumi.Input[str],
                 allow_zero_size: Optional[pulumi.Input[bool]] = None,
                 cookie: Optional[pulumi.Input[str]] = None,
                 download_client_id: Optional[pulumi.Input[int]] = None,
                 enable_automatic_search: Optional[pulumi.Input[bool]] = None,
                 enable_interactive_search: Optional[pulumi.Input[bool]] = None,
                 enable_rss: Optional[pulumi.Input[bool]] = None,
                 minimum_seeders: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 season_pack_seed_time: Optional[pulumi.Input[int]] = None,
                 seed_ratio: Optional[pulumi.Input[float]] = None,
                 seed_time: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a TorrentRss resource.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[bool] allow_zero_size: Allow zero size files.
        :param pulumi.Input[str] cookie: Cookie.
        :param pulumi.Input[int] download_client_id: Download client ID.
        :param pulumi.Input[bool] enable_automatic_search: Enable automatic search flag.
        :param pulumi.Input[bool] enable_interactive_search: Enable interactive search flag.
        :param pulumi.Input[bool] enable_rss: Enable RSS flag.
        :param pulumi.Input[int] minimum_seeders: Minimum seeders.
        :param pulumi.Input[str] name: IndexerTorrentRss name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[int] season_pack_seed_time: Season seed time.
        :param pulumi.Input[float] seed_ratio: Seed ratio.
        :param pulumi.Input[int] seed_time: Seed time.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "base_url", base_url)
        if allow_zero_size is not None:
            pulumi.set(__self__, "allow_zero_size", allow_zero_size)
        if cookie is not None:
            pulumi.set(__self__, "cookie", cookie)
        if download_client_id is not None:
            pulumi.set(__self__, "download_client_id", download_client_id)
        if enable_automatic_search is not None:
            pulumi.set(__self__, "enable_automatic_search", enable_automatic_search)
        if enable_interactive_search is not None:
            pulumi.set(__self__, "enable_interactive_search", enable_interactive_search)
        if enable_rss is not None:
            pulumi.set(__self__, "enable_rss", enable_rss)
        if minimum_seeders is not None:
            pulumi.set(__self__, "minimum_seeders", minimum_seeders)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if season_pack_seed_time is not None:
            pulumi.set(__self__, "season_pack_seed_time", season_pack_seed_time)
        if seed_ratio is not None:
            pulumi.set(__self__, "seed_ratio", seed_ratio)
        if seed_time is not None:
            pulumi.set(__self__, "seed_time", seed_time)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Input[str]:
        """
        Base URL.
        """
        return pulumi.get(self, "base_url")

    @base_url.setter
    def base_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_url", value)

    @property
    @pulumi.getter(name="allowZeroSize")
    def allow_zero_size(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow zero size files.
        """
        return pulumi.get(self, "allow_zero_size")

    @allow_zero_size.setter
    def allow_zero_size(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_zero_size", value)

    @property
    @pulumi.getter
    def cookie(self) -> Optional[pulumi.Input[str]]:
        """
        Cookie.
        """
        return pulumi.get(self, "cookie")

    @cookie.setter
    def cookie(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cookie", value)

    @property
    @pulumi.getter(name="downloadClientId")
    def download_client_id(self) -> Optional[pulumi.Input[int]]:
        """
        Download client ID.
        """
        return pulumi.get(self, "download_client_id")

    @download_client_id.setter
    def download_client_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "download_client_id", value)

    @property
    @pulumi.getter(name="enableAutomaticSearch")
    def enable_automatic_search(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable automatic search flag.
        """
        return pulumi.get(self, "enable_automatic_search")

    @enable_automatic_search.setter
    def enable_automatic_search(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_automatic_search", value)

    @property
    @pulumi.getter(name="enableInteractiveSearch")
    def enable_interactive_search(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable interactive search flag.
        """
        return pulumi.get(self, "enable_interactive_search")

    @enable_interactive_search.setter
    def enable_interactive_search(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_interactive_search", value)

    @property
    @pulumi.getter(name="enableRss")
    def enable_rss(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable RSS flag.
        """
        return pulumi.get(self, "enable_rss")

    @enable_rss.setter
    def enable_rss(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_rss", value)

    @property
    @pulumi.getter(name="minimumSeeders")
    def minimum_seeders(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum seeders.
        """
        return pulumi.get(self, "minimum_seeders")

    @minimum_seeders.setter
    def minimum_seeders(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minimum_seeders", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        IndexerTorrentRss name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="seasonPackSeedTime")
    def season_pack_seed_time(self) -> Optional[pulumi.Input[int]]:
        """
        Season seed time.
        """
        return pulumi.get(self, "season_pack_seed_time")

    @season_pack_seed_time.setter
    def season_pack_seed_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "season_pack_seed_time", value)

    @property
    @pulumi.getter(name="seedRatio")
    def seed_ratio(self) -> Optional[pulumi.Input[float]]:
        """
        Seed ratio.
        """
        return pulumi.get(self, "seed_ratio")

    @seed_ratio.setter
    def seed_ratio(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "seed_ratio", value)

    @property
    @pulumi.getter(name="seedTime")
    def seed_time(self) -> Optional[pulumi.Input[int]]:
        """
        Seed time.
        """
        return pulumi.get(self, "seed_time")

    @seed_time.setter
    def seed_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "seed_time", value)

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
class _TorrentRssState:
    def __init__(__self__, *,
                 allow_zero_size: Optional[pulumi.Input[bool]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 cookie: Optional[pulumi.Input[str]] = None,
                 download_client_id: Optional[pulumi.Input[int]] = None,
                 enable_automatic_search: Optional[pulumi.Input[bool]] = None,
                 enable_interactive_search: Optional[pulumi.Input[bool]] = None,
                 enable_rss: Optional[pulumi.Input[bool]] = None,
                 minimum_seeders: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 season_pack_seed_time: Optional[pulumi.Input[int]] = None,
                 seed_ratio: Optional[pulumi.Input[float]] = None,
                 seed_time: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering TorrentRss resources.
        :param pulumi.Input[bool] allow_zero_size: Allow zero size files.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[str] cookie: Cookie.
        :param pulumi.Input[int] download_client_id: Download client ID.
        :param pulumi.Input[bool] enable_automatic_search: Enable automatic search flag.
        :param pulumi.Input[bool] enable_interactive_search: Enable interactive search flag.
        :param pulumi.Input[bool] enable_rss: Enable RSS flag.
        :param pulumi.Input[int] minimum_seeders: Minimum seeders.
        :param pulumi.Input[str] name: IndexerTorrentRss name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[int] season_pack_seed_time: Season seed time.
        :param pulumi.Input[float] seed_ratio: Seed ratio.
        :param pulumi.Input[int] seed_time: Seed time.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if allow_zero_size is not None:
            pulumi.set(__self__, "allow_zero_size", allow_zero_size)
        if base_url is not None:
            pulumi.set(__self__, "base_url", base_url)
        if cookie is not None:
            pulumi.set(__self__, "cookie", cookie)
        if download_client_id is not None:
            pulumi.set(__self__, "download_client_id", download_client_id)
        if enable_automatic_search is not None:
            pulumi.set(__self__, "enable_automatic_search", enable_automatic_search)
        if enable_interactive_search is not None:
            pulumi.set(__self__, "enable_interactive_search", enable_interactive_search)
        if enable_rss is not None:
            pulumi.set(__self__, "enable_rss", enable_rss)
        if minimum_seeders is not None:
            pulumi.set(__self__, "minimum_seeders", minimum_seeders)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if season_pack_seed_time is not None:
            pulumi.set(__self__, "season_pack_seed_time", season_pack_seed_time)
        if seed_ratio is not None:
            pulumi.set(__self__, "seed_ratio", seed_ratio)
        if seed_time is not None:
            pulumi.set(__self__, "seed_time", seed_time)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="allowZeroSize")
    def allow_zero_size(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow zero size files.
        """
        return pulumi.get(self, "allow_zero_size")

    @allow_zero_size.setter
    def allow_zero_size(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_zero_size", value)

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> Optional[pulumi.Input[str]]:
        """
        Base URL.
        """
        return pulumi.get(self, "base_url")

    @base_url.setter
    def base_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_url", value)

    @property
    @pulumi.getter
    def cookie(self) -> Optional[pulumi.Input[str]]:
        """
        Cookie.
        """
        return pulumi.get(self, "cookie")

    @cookie.setter
    def cookie(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cookie", value)

    @property
    @pulumi.getter(name="downloadClientId")
    def download_client_id(self) -> Optional[pulumi.Input[int]]:
        """
        Download client ID.
        """
        return pulumi.get(self, "download_client_id")

    @download_client_id.setter
    def download_client_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "download_client_id", value)

    @property
    @pulumi.getter(name="enableAutomaticSearch")
    def enable_automatic_search(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable automatic search flag.
        """
        return pulumi.get(self, "enable_automatic_search")

    @enable_automatic_search.setter
    def enable_automatic_search(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_automatic_search", value)

    @property
    @pulumi.getter(name="enableInteractiveSearch")
    def enable_interactive_search(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable interactive search flag.
        """
        return pulumi.get(self, "enable_interactive_search")

    @enable_interactive_search.setter
    def enable_interactive_search(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_interactive_search", value)

    @property
    @pulumi.getter(name="enableRss")
    def enable_rss(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable RSS flag.
        """
        return pulumi.get(self, "enable_rss")

    @enable_rss.setter
    def enable_rss(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_rss", value)

    @property
    @pulumi.getter(name="minimumSeeders")
    def minimum_seeders(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum seeders.
        """
        return pulumi.get(self, "minimum_seeders")

    @minimum_seeders.setter
    def minimum_seeders(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "minimum_seeders", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        IndexerTorrentRss name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="seasonPackSeedTime")
    def season_pack_seed_time(self) -> Optional[pulumi.Input[int]]:
        """
        Season seed time.
        """
        return pulumi.get(self, "season_pack_seed_time")

    @season_pack_seed_time.setter
    def season_pack_seed_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "season_pack_seed_time", value)

    @property
    @pulumi.getter(name="seedRatio")
    def seed_ratio(self) -> Optional[pulumi.Input[float]]:
        """
        Seed ratio.
        """
        return pulumi.get(self, "seed_ratio")

    @seed_ratio.setter
    def seed_ratio(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "seed_ratio", value)

    @property
    @pulumi.getter(name="seedTime")
    def seed_time(self) -> Optional[pulumi.Input[int]]:
        """
        Seed time.
        """
        return pulumi.get(self, "seed_time")

    @seed_time.setter
    def seed_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "seed_time", value)

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


class TorrentRss(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_zero_size: Optional[pulumi.Input[bool]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 cookie: Optional[pulumi.Input[str]] = None,
                 download_client_id: Optional[pulumi.Input[int]] = None,
                 enable_automatic_search: Optional[pulumi.Input[bool]] = None,
                 enable_interactive_search: Optional[pulumi.Input[bool]] = None,
                 enable_rss: Optional[pulumi.Input[bool]] = None,
                 minimum_seeders: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 season_pack_seed_time: Optional[pulumi.Input[int]] = None,
                 seed_ratio: Optional[pulumi.Input[float]] = None,
                 seed_time: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Indexers -->
        Indexer Torrent RSS resource.
        For more information refer to [Indexer](https://wiki.servarr.com/sonarr/settings#indexers) and [Torrent RSS](https://wiki.servarr.com/sonarr/supported#torrentrssindexer).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sonarr as sonarr

        example = sonarr.indexers.TorrentRss("example",
            allow_zero_size=True,
            base_url="https://rss.io",
            enable_automatic_search=True,
            minimum_seeders=1)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import sonarr:Indexers/torrentRss:TorrentRss example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_zero_size: Allow zero size files.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[str] cookie: Cookie.
        :param pulumi.Input[int] download_client_id: Download client ID.
        :param pulumi.Input[bool] enable_automatic_search: Enable automatic search flag.
        :param pulumi.Input[bool] enable_interactive_search: Enable interactive search flag.
        :param pulumi.Input[bool] enable_rss: Enable RSS flag.
        :param pulumi.Input[int] minimum_seeders: Minimum seeders.
        :param pulumi.Input[str] name: IndexerTorrentRss name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[int] season_pack_seed_time: Season seed time.
        :param pulumi.Input[float] seed_ratio: Seed ratio.
        :param pulumi.Input[int] seed_time: Seed time.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TorrentRssArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Indexers -->
        Indexer Torrent RSS resource.
        For more information refer to [Indexer](https://wiki.servarr.com/sonarr/settings#indexers) and [Torrent RSS](https://wiki.servarr.com/sonarr/supported#torrentrssindexer).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sonarr as sonarr

        example = sonarr.indexers.TorrentRss("example",
            allow_zero_size=True,
            base_url="https://rss.io",
            enable_automatic_search=True,
            minimum_seeders=1)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import sonarr:Indexers/torrentRss:TorrentRss example 1
        ```

        :param str resource_name: The name of the resource.
        :param TorrentRssArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TorrentRssArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_zero_size: Optional[pulumi.Input[bool]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 cookie: Optional[pulumi.Input[str]] = None,
                 download_client_id: Optional[pulumi.Input[int]] = None,
                 enable_automatic_search: Optional[pulumi.Input[bool]] = None,
                 enable_interactive_search: Optional[pulumi.Input[bool]] = None,
                 enable_rss: Optional[pulumi.Input[bool]] = None,
                 minimum_seeders: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 season_pack_seed_time: Optional[pulumi.Input[int]] = None,
                 seed_ratio: Optional[pulumi.Input[float]] = None,
                 seed_time: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TorrentRssArgs.__new__(TorrentRssArgs)

            __props__.__dict__["allow_zero_size"] = allow_zero_size
            if base_url is None and not opts.urn:
                raise TypeError("Missing required property 'base_url'")
            __props__.__dict__["base_url"] = base_url
            __props__.__dict__["cookie"] = cookie
            __props__.__dict__["download_client_id"] = download_client_id
            __props__.__dict__["enable_automatic_search"] = enable_automatic_search
            __props__.__dict__["enable_interactive_search"] = enable_interactive_search
            __props__.__dict__["enable_rss"] = enable_rss
            __props__.__dict__["minimum_seeders"] = minimum_seeders
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["season_pack_seed_time"] = season_pack_seed_time
            __props__.__dict__["seed_ratio"] = seed_ratio
            __props__.__dict__["seed_time"] = seed_time
            __props__.__dict__["tags"] = tags
        super(TorrentRss, __self__).__init__(
            'sonarr:Indexers/torrentRss:TorrentRss',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_zero_size: Optional[pulumi.Input[bool]] = None,
            base_url: Optional[pulumi.Input[str]] = None,
            cookie: Optional[pulumi.Input[str]] = None,
            download_client_id: Optional[pulumi.Input[int]] = None,
            enable_automatic_search: Optional[pulumi.Input[bool]] = None,
            enable_interactive_search: Optional[pulumi.Input[bool]] = None,
            enable_rss: Optional[pulumi.Input[bool]] = None,
            minimum_seeders: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            season_pack_seed_time: Optional[pulumi.Input[int]] = None,
            seed_ratio: Optional[pulumi.Input[float]] = None,
            seed_time: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'TorrentRss':
        """
        Get an existing TorrentRss resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_zero_size: Allow zero size files.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[str] cookie: Cookie.
        :param pulumi.Input[int] download_client_id: Download client ID.
        :param pulumi.Input[bool] enable_automatic_search: Enable automatic search flag.
        :param pulumi.Input[bool] enable_interactive_search: Enable interactive search flag.
        :param pulumi.Input[bool] enable_rss: Enable RSS flag.
        :param pulumi.Input[int] minimum_seeders: Minimum seeders.
        :param pulumi.Input[str] name: IndexerTorrentRss name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[int] season_pack_seed_time: Season seed time.
        :param pulumi.Input[float] seed_ratio: Seed ratio.
        :param pulumi.Input[int] seed_time: Seed time.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TorrentRssState.__new__(_TorrentRssState)

        __props__.__dict__["allow_zero_size"] = allow_zero_size
        __props__.__dict__["base_url"] = base_url
        __props__.__dict__["cookie"] = cookie
        __props__.__dict__["download_client_id"] = download_client_id
        __props__.__dict__["enable_automatic_search"] = enable_automatic_search
        __props__.__dict__["enable_interactive_search"] = enable_interactive_search
        __props__.__dict__["enable_rss"] = enable_rss
        __props__.__dict__["minimum_seeders"] = minimum_seeders
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["season_pack_seed_time"] = season_pack_seed_time
        __props__.__dict__["seed_ratio"] = seed_ratio
        __props__.__dict__["seed_time"] = seed_time
        __props__.__dict__["tags"] = tags
        return TorrentRss(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowZeroSize")
    def allow_zero_size(self) -> pulumi.Output[bool]:
        """
        Allow zero size files.
        """
        return pulumi.get(self, "allow_zero_size")

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Output[str]:
        """
        Base URL.
        """
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter
    def cookie(self) -> pulumi.Output[str]:
        """
        Cookie.
        """
        return pulumi.get(self, "cookie")

    @property
    @pulumi.getter(name="downloadClientId")
    def download_client_id(self) -> pulumi.Output[int]:
        """
        Download client ID.
        """
        return pulumi.get(self, "download_client_id")

    @property
    @pulumi.getter(name="enableAutomaticSearch")
    def enable_automatic_search(self) -> pulumi.Output[bool]:
        """
        Enable automatic search flag.
        """
        return pulumi.get(self, "enable_automatic_search")

    @property
    @pulumi.getter(name="enableInteractiveSearch")
    def enable_interactive_search(self) -> pulumi.Output[bool]:
        """
        Enable interactive search flag.
        """
        return pulumi.get(self, "enable_interactive_search")

    @property
    @pulumi.getter(name="enableRss")
    def enable_rss(self) -> pulumi.Output[bool]:
        """
        Enable RSS flag.
        """
        return pulumi.get(self, "enable_rss")

    @property
    @pulumi.getter(name="minimumSeeders")
    def minimum_seeders(self) -> pulumi.Output[int]:
        """
        Minimum seeders.
        """
        return pulumi.get(self, "minimum_seeders")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        IndexerTorrentRss name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="seasonPackSeedTime")
    def season_pack_seed_time(self) -> pulumi.Output[int]:
        """
        Season seed time.
        """
        return pulumi.get(self, "season_pack_seed_time")

    @property
    @pulumi.getter(name="seedRatio")
    def seed_ratio(self) -> pulumi.Output[float]:
        """
        Seed ratio.
        """
        return pulumi.get(self, "seed_ratio")

    @property
    @pulumi.getter(name="seedTime")
    def seed_time(self) -> pulumi.Output[int]:
        """
        Seed time.
        """
        return pulumi.get(self, "seed_time")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

