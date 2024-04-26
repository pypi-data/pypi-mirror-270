# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TraktPopularArgs', 'TraktPopular']

@pulumi.input_type
class TraktPopularArgs:
    def __init__(__self__, *,
                 enable_automatic_add: pulumi.Input[bool],
                 quality_profile_id: pulumi.Input[int],
                 root_folder_path: pulumi.Input[str],
                 season_folder: pulumi.Input[bool],
                 series_type: pulumi.Input[str],
                 should_monitor: pulumi.Input[str],
                 trakt_list_type: pulumi.Input[int],
                 access_token: Optional[pulumi.Input[str]] = None,
                 auth_user: Optional[pulumi.Input[str]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 genres: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rating: Optional[pulumi.Input[str]] = None,
                 refresh_token: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 trakt_additional_parameters: Optional[pulumi.Input[str]] = None,
                 years: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TraktPopular resource.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] season_folder: Season folder flag.
        :param pulumi.Input[str] series_type: Series type.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[int] trakt_list_type: Trakt list type. '0' Trending, '1' Popular, '2' Anticipated, '3' TopWatchedByWeek, '4' TopWatchedByMonth, '5' TopWatchedByYear, '6' TopWatchedByAllTime, '7' RecommendedByWeek, '8' RecommendedByMonth, '9' RecommendedByYear, '10' RecommendedByAllTime.
        :param pulumi.Input[str] access_token: Access token.
        :param pulumi.Input[str] auth_user: Auth User.
        :param pulumi.Input[str] expires: Expires.
        :param pulumi.Input[str] genres: Genres.
        :param pulumi.Input[int] limit: Limit.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[str] rating: Rating.
        :param pulumi.Input[str] refresh_token: Refresh token.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] trakt_additional_parameters: Trakt additional parameters.
        :param pulumi.Input[str] years: Years.
        """
        pulumi.set(__self__, "enable_automatic_add", enable_automatic_add)
        pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        pulumi.set(__self__, "root_folder_path", root_folder_path)
        pulumi.set(__self__, "season_folder", season_folder)
        pulumi.set(__self__, "series_type", series_type)
        pulumi.set(__self__, "should_monitor", should_monitor)
        pulumi.set(__self__, "trakt_list_type", trakt_list_type)
        if access_token is not None:
            pulumi.set(__self__, "access_token", access_token)
        if auth_user is not None:
            pulumi.set(__self__, "auth_user", auth_user)
        if expires is not None:
            pulumi.set(__self__, "expires", expires)
        if genres is not None:
            pulumi.set(__self__, "genres", genres)
        if limit is not None:
            pulumi.set(__self__, "limit", limit)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rating is not None:
            pulumi.set(__self__, "rating", rating)
        if refresh_token is not None:
            pulumi.set(__self__, "refresh_token", refresh_token)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if trakt_additional_parameters is not None:
            pulumi.set(__self__, "trakt_additional_parameters", trakt_additional_parameters)
        if years is not None:
            pulumi.set(__self__, "years", years)

    @property
    @pulumi.getter(name="enableAutomaticAdd")
    def enable_automatic_add(self) -> pulumi.Input[bool]:
        """
        Enable automatic add flag.
        """
        return pulumi.get(self, "enable_automatic_add")

    @enable_automatic_add.setter
    def enable_automatic_add(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enable_automatic_add", value)

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> pulumi.Input[int]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @quality_profile_id.setter
    def quality_profile_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "quality_profile_id", value)

    @property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> pulumi.Input[str]:
        """
        Root folder path.
        """
        return pulumi.get(self, "root_folder_path")

    @root_folder_path.setter
    def root_folder_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "root_folder_path", value)

    @property
    @pulumi.getter(name="seasonFolder")
    def season_folder(self) -> pulumi.Input[bool]:
        """
        Season folder flag.
        """
        return pulumi.get(self, "season_folder")

    @season_folder.setter
    def season_folder(self, value: pulumi.Input[bool]):
        pulumi.set(self, "season_folder", value)

    @property
    @pulumi.getter(name="seriesType")
    def series_type(self) -> pulumi.Input[str]:
        """
        Series type.
        """
        return pulumi.get(self, "series_type")

    @series_type.setter
    def series_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "series_type", value)

    @property
    @pulumi.getter(name="shouldMonitor")
    def should_monitor(self) -> pulumi.Input[str]:
        """
        Should monitor.
        """
        return pulumi.get(self, "should_monitor")

    @should_monitor.setter
    def should_monitor(self, value: pulumi.Input[str]):
        pulumi.set(self, "should_monitor", value)

    @property
    @pulumi.getter(name="traktListType")
    def trakt_list_type(self) -> pulumi.Input[int]:
        """
        Trakt list type. '0' Trending, '1' Popular, '2' Anticipated, '3' TopWatchedByWeek, '4' TopWatchedByMonth, '5' TopWatchedByYear, '6' TopWatchedByAllTime, '7' RecommendedByWeek, '8' RecommendedByMonth, '9' RecommendedByYear, '10' RecommendedByAllTime.
        """
        return pulumi.get(self, "trakt_list_type")

    @trakt_list_type.setter
    def trakt_list_type(self, value: pulumi.Input[int]):
        pulumi.set(self, "trakt_list_type", value)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[str]]:
        """
        Access token.
        """
        return pulumi.get(self, "access_token")

    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_token", value)

    @property
    @pulumi.getter(name="authUser")
    def auth_user(self) -> Optional[pulumi.Input[str]]:
        """
        Auth User.
        """
        return pulumi.get(self, "auth_user")

    @auth_user.setter
    def auth_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_user", value)

    @property
    @pulumi.getter
    def expires(self) -> Optional[pulumi.Input[str]]:
        """
        Expires.
        """
        return pulumi.get(self, "expires")

    @expires.setter
    def expires(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires", value)

    @property
    @pulumi.getter
    def genres(self) -> Optional[pulumi.Input[str]]:
        """
        Genres.
        """
        return pulumi.get(self, "genres")

    @genres.setter
    def genres(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "genres", value)

    @property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[int]]:
        """
        Limit.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "limit", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Import List name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def rating(self) -> Optional[pulumi.Input[str]]:
        """
        Rating.
        """
        return pulumi.get(self, "rating")

    @rating.setter
    def rating(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rating", value)

    @property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[str]]:
        """
        Refresh token.
        """
        return pulumi.get(self, "refresh_token")

    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "refresh_token", value)

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

    @property
    @pulumi.getter(name="traktAdditionalParameters")
    def trakt_additional_parameters(self) -> Optional[pulumi.Input[str]]:
        """
        Trakt additional parameters.
        """
        return pulumi.get(self, "trakt_additional_parameters")

    @trakt_additional_parameters.setter
    def trakt_additional_parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trakt_additional_parameters", value)

    @property
    @pulumi.getter
    def years(self) -> Optional[pulumi.Input[str]]:
        """
        Years.
        """
        return pulumi.get(self, "years")

    @years.setter
    def years(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "years", value)


@pulumi.input_type
class _TraktPopularState:
    def __init__(__self__, *,
                 access_token: Optional[pulumi.Input[str]] = None,
                 auth_user: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 genres: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 rating: Optional[pulumi.Input[str]] = None,
                 refresh_token: Optional[pulumi.Input[str]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 season_folder: Optional[pulumi.Input[bool]] = None,
                 series_type: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 trakt_additional_parameters: Optional[pulumi.Input[str]] = None,
                 trakt_list_type: Optional[pulumi.Input[int]] = None,
                 years: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TraktPopular resources.
        :param pulumi.Input[str] access_token: Access token.
        :param pulumi.Input[str] auth_user: Auth User.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[str] expires: Expires.
        :param pulumi.Input[str] genres: Genres.
        :param pulumi.Input[int] limit: Limit.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] rating: Rating.
        :param pulumi.Input[str] refresh_token: Refresh token.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] season_folder: Season folder flag.
        :param pulumi.Input[str] series_type: Series type.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] trakt_additional_parameters: Trakt additional parameters.
        :param pulumi.Input[int] trakt_list_type: Trakt list type. '0' Trending, '1' Popular, '2' Anticipated, '3' TopWatchedByWeek, '4' TopWatchedByMonth, '5' TopWatchedByYear, '6' TopWatchedByAllTime, '7' RecommendedByWeek, '8' RecommendedByMonth, '9' RecommendedByYear, '10' RecommendedByAllTime.
        :param pulumi.Input[str] years: Years.
        """
        if access_token is not None:
            pulumi.set(__self__, "access_token", access_token)
        if auth_user is not None:
            pulumi.set(__self__, "auth_user", auth_user)
        if enable_automatic_add is not None:
            pulumi.set(__self__, "enable_automatic_add", enable_automatic_add)
        if expires is not None:
            pulumi.set(__self__, "expires", expires)
        if genres is not None:
            pulumi.set(__self__, "genres", genres)
        if limit is not None:
            pulumi.set(__self__, "limit", limit)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if quality_profile_id is not None:
            pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        if rating is not None:
            pulumi.set(__self__, "rating", rating)
        if refresh_token is not None:
            pulumi.set(__self__, "refresh_token", refresh_token)
        if root_folder_path is not None:
            pulumi.set(__self__, "root_folder_path", root_folder_path)
        if season_folder is not None:
            pulumi.set(__self__, "season_folder", season_folder)
        if series_type is not None:
            pulumi.set(__self__, "series_type", series_type)
        if should_monitor is not None:
            pulumi.set(__self__, "should_monitor", should_monitor)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if trakt_additional_parameters is not None:
            pulumi.set(__self__, "trakt_additional_parameters", trakt_additional_parameters)
        if trakt_list_type is not None:
            pulumi.set(__self__, "trakt_list_type", trakt_list_type)
        if years is not None:
            pulumi.set(__self__, "years", years)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[str]]:
        """
        Access token.
        """
        return pulumi.get(self, "access_token")

    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_token", value)

    @property
    @pulumi.getter(name="authUser")
    def auth_user(self) -> Optional[pulumi.Input[str]]:
        """
        Auth User.
        """
        return pulumi.get(self, "auth_user")

    @auth_user.setter
    def auth_user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_user", value)

    @property
    @pulumi.getter(name="enableAutomaticAdd")
    def enable_automatic_add(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable automatic add flag.
        """
        return pulumi.get(self, "enable_automatic_add")

    @enable_automatic_add.setter
    def enable_automatic_add(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_automatic_add", value)

    @property
    @pulumi.getter
    def expires(self) -> Optional[pulumi.Input[str]]:
        """
        Expires.
        """
        return pulumi.get(self, "expires")

    @expires.setter
    def expires(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires", value)

    @property
    @pulumi.getter
    def genres(self) -> Optional[pulumi.Input[str]]:
        """
        Genres.
        """
        return pulumi.get(self, "genres")

    @genres.setter
    def genres(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "genres", value)

    @property
    @pulumi.getter
    def limit(self) -> Optional[pulumi.Input[int]]:
        """
        Limit.
        """
        return pulumi.get(self, "limit")

    @limit.setter
    def limit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "limit", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Import List name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> Optional[pulumi.Input[int]]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @quality_profile_id.setter
    def quality_profile_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "quality_profile_id", value)

    @property
    @pulumi.getter
    def rating(self) -> Optional[pulumi.Input[str]]:
        """
        Rating.
        """
        return pulumi.get(self, "rating")

    @rating.setter
    def rating(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rating", value)

    @property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> Optional[pulumi.Input[str]]:
        """
        Refresh token.
        """
        return pulumi.get(self, "refresh_token")

    @refresh_token.setter
    def refresh_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "refresh_token", value)

    @property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> Optional[pulumi.Input[str]]:
        """
        Root folder path.
        """
        return pulumi.get(self, "root_folder_path")

    @root_folder_path.setter
    def root_folder_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "root_folder_path", value)

    @property
    @pulumi.getter(name="seasonFolder")
    def season_folder(self) -> Optional[pulumi.Input[bool]]:
        """
        Season folder flag.
        """
        return pulumi.get(self, "season_folder")

    @season_folder.setter
    def season_folder(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "season_folder", value)

    @property
    @pulumi.getter(name="seriesType")
    def series_type(self) -> Optional[pulumi.Input[str]]:
        """
        Series type.
        """
        return pulumi.get(self, "series_type")

    @series_type.setter
    def series_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "series_type", value)

    @property
    @pulumi.getter(name="shouldMonitor")
    def should_monitor(self) -> Optional[pulumi.Input[str]]:
        """
        Should monitor.
        """
        return pulumi.get(self, "should_monitor")

    @should_monitor.setter
    def should_monitor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "should_monitor", value)

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

    @property
    @pulumi.getter(name="traktAdditionalParameters")
    def trakt_additional_parameters(self) -> Optional[pulumi.Input[str]]:
        """
        Trakt additional parameters.
        """
        return pulumi.get(self, "trakt_additional_parameters")

    @trakt_additional_parameters.setter
    def trakt_additional_parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trakt_additional_parameters", value)

    @property
    @pulumi.getter(name="traktListType")
    def trakt_list_type(self) -> Optional[pulumi.Input[int]]:
        """
        Trakt list type. '0' Trending, '1' Popular, '2' Anticipated, '3' TopWatchedByWeek, '4' TopWatchedByMonth, '5' TopWatchedByYear, '6' TopWatchedByAllTime, '7' RecommendedByWeek, '8' RecommendedByMonth, '9' RecommendedByYear, '10' RecommendedByAllTime.
        """
        return pulumi.get(self, "trakt_list_type")

    @trakt_list_type.setter
    def trakt_list_type(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "trakt_list_type", value)

    @property
    @pulumi.getter
    def years(self) -> Optional[pulumi.Input[str]]:
        """
        Years.
        """
        return pulumi.get(self, "years")

    @years.setter
    def years(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "years", value)


class TraktPopular(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_token: Optional[pulumi.Input[str]] = None,
                 auth_user: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 genres: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 rating: Optional[pulumi.Input[str]] = None,
                 refresh_token: Optional[pulumi.Input[str]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 season_folder: Optional[pulumi.Input[bool]] = None,
                 series_type: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 trakt_additional_parameters: Optional[pulumi.Input[str]] = None,
                 trakt_list_type: Optional[pulumi.Input[int]] = None,
                 years: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- subcategory:Import Lists -->
        ImportList TraktPopular resource.
        For more information refer to [Import List](https://wiki.servarr.com/sonarr/settings#import-lists) and [TraktPopular](https://wiki.servarr.com/sonarr/supported#trakt_popular).

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import sonarr:ImportLists/traktPopular:TraktPopular example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_token: Access token.
        :param pulumi.Input[str] auth_user: Auth User.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[str] expires: Expires.
        :param pulumi.Input[str] genres: Genres.
        :param pulumi.Input[int] limit: Limit.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] rating: Rating.
        :param pulumi.Input[str] refresh_token: Refresh token.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] season_folder: Season folder flag.
        :param pulumi.Input[str] series_type: Series type.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] trakt_additional_parameters: Trakt additional parameters.
        :param pulumi.Input[int] trakt_list_type: Trakt list type. '0' Trending, '1' Popular, '2' Anticipated, '3' TopWatchedByWeek, '4' TopWatchedByMonth, '5' TopWatchedByYear, '6' TopWatchedByAllTime, '7' RecommendedByWeek, '8' RecommendedByMonth, '9' RecommendedByYear, '10' RecommendedByAllTime.
        :param pulumi.Input[str] years: Years.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TraktPopularArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Import Lists -->
        ImportList TraktPopular resource.
        For more information refer to [Import List](https://wiki.servarr.com/sonarr/settings#import-lists) and [TraktPopular](https://wiki.servarr.com/sonarr/supported#trakt_popular).

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import sonarr:ImportLists/traktPopular:TraktPopular example 1
        ```

        :param str resource_name: The name of the resource.
        :param TraktPopularArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TraktPopularArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_token: Optional[pulumi.Input[str]] = None,
                 auth_user: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 genres: Optional[pulumi.Input[str]] = None,
                 limit: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 rating: Optional[pulumi.Input[str]] = None,
                 refresh_token: Optional[pulumi.Input[str]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 season_folder: Optional[pulumi.Input[bool]] = None,
                 series_type: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 trakt_additional_parameters: Optional[pulumi.Input[str]] = None,
                 trakt_list_type: Optional[pulumi.Input[int]] = None,
                 years: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TraktPopularArgs.__new__(TraktPopularArgs)

            __props__.__dict__["access_token"] = None if access_token is None else pulumi.Output.secret(access_token)
            __props__.__dict__["auth_user"] = auth_user
            if enable_automatic_add is None and not opts.urn:
                raise TypeError("Missing required property 'enable_automatic_add'")
            __props__.__dict__["enable_automatic_add"] = enable_automatic_add
            __props__.__dict__["expires"] = expires
            __props__.__dict__["genres"] = genres
            __props__.__dict__["limit"] = limit
            __props__.__dict__["name"] = name
            if quality_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'quality_profile_id'")
            __props__.__dict__["quality_profile_id"] = quality_profile_id
            __props__.__dict__["rating"] = rating
            __props__.__dict__["refresh_token"] = None if refresh_token is None else pulumi.Output.secret(refresh_token)
            if root_folder_path is None and not opts.urn:
                raise TypeError("Missing required property 'root_folder_path'")
            __props__.__dict__["root_folder_path"] = root_folder_path
            if season_folder is None and not opts.urn:
                raise TypeError("Missing required property 'season_folder'")
            __props__.__dict__["season_folder"] = season_folder
            if series_type is None and not opts.urn:
                raise TypeError("Missing required property 'series_type'")
            __props__.__dict__["series_type"] = series_type
            if should_monitor is None and not opts.urn:
                raise TypeError("Missing required property 'should_monitor'")
            __props__.__dict__["should_monitor"] = should_monitor
            __props__.__dict__["tags"] = tags
            __props__.__dict__["trakt_additional_parameters"] = trakt_additional_parameters
            if trakt_list_type is None and not opts.urn:
                raise TypeError("Missing required property 'trakt_list_type'")
            __props__.__dict__["trakt_list_type"] = trakt_list_type
            __props__.__dict__["years"] = years
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["accessToken", "refreshToken"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(TraktPopular, __self__).__init__(
            'sonarr:ImportLists/traktPopular:TraktPopular',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_token: Optional[pulumi.Input[str]] = None,
            auth_user: Optional[pulumi.Input[str]] = None,
            enable_automatic_add: Optional[pulumi.Input[bool]] = None,
            expires: Optional[pulumi.Input[str]] = None,
            genres: Optional[pulumi.Input[str]] = None,
            limit: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            quality_profile_id: Optional[pulumi.Input[int]] = None,
            rating: Optional[pulumi.Input[str]] = None,
            refresh_token: Optional[pulumi.Input[str]] = None,
            root_folder_path: Optional[pulumi.Input[str]] = None,
            season_folder: Optional[pulumi.Input[bool]] = None,
            series_type: Optional[pulumi.Input[str]] = None,
            should_monitor: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            trakt_additional_parameters: Optional[pulumi.Input[str]] = None,
            trakt_list_type: Optional[pulumi.Input[int]] = None,
            years: Optional[pulumi.Input[str]] = None) -> 'TraktPopular':
        """
        Get an existing TraktPopular resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_token: Access token.
        :param pulumi.Input[str] auth_user: Auth User.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[str] expires: Expires.
        :param pulumi.Input[str] genres: Genres.
        :param pulumi.Input[int] limit: Limit.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] rating: Rating.
        :param pulumi.Input[str] refresh_token: Refresh token.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[bool] season_folder: Season folder flag.
        :param pulumi.Input[str] series_type: Series type.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] trakt_additional_parameters: Trakt additional parameters.
        :param pulumi.Input[int] trakt_list_type: Trakt list type. '0' Trending, '1' Popular, '2' Anticipated, '3' TopWatchedByWeek, '4' TopWatchedByMonth, '5' TopWatchedByYear, '6' TopWatchedByAllTime, '7' RecommendedByWeek, '8' RecommendedByMonth, '9' RecommendedByYear, '10' RecommendedByAllTime.
        :param pulumi.Input[str] years: Years.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TraktPopularState.__new__(_TraktPopularState)

        __props__.__dict__["access_token"] = access_token
        __props__.__dict__["auth_user"] = auth_user
        __props__.__dict__["enable_automatic_add"] = enable_automatic_add
        __props__.__dict__["expires"] = expires
        __props__.__dict__["genres"] = genres
        __props__.__dict__["limit"] = limit
        __props__.__dict__["name"] = name
        __props__.__dict__["quality_profile_id"] = quality_profile_id
        __props__.__dict__["rating"] = rating
        __props__.__dict__["refresh_token"] = refresh_token
        __props__.__dict__["root_folder_path"] = root_folder_path
        __props__.__dict__["season_folder"] = season_folder
        __props__.__dict__["series_type"] = series_type
        __props__.__dict__["should_monitor"] = should_monitor
        __props__.__dict__["tags"] = tags
        __props__.__dict__["trakt_additional_parameters"] = trakt_additional_parameters
        __props__.__dict__["trakt_list_type"] = trakt_list_type
        __props__.__dict__["years"] = years
        return TraktPopular(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> pulumi.Output[str]:
        """
        Access token.
        """
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter(name="authUser")
    def auth_user(self) -> pulumi.Output[str]:
        """
        Auth User.
        """
        return pulumi.get(self, "auth_user")

    @property
    @pulumi.getter(name="enableAutomaticAdd")
    def enable_automatic_add(self) -> pulumi.Output[bool]:
        """
        Enable automatic add flag.
        """
        return pulumi.get(self, "enable_automatic_add")

    @property
    @pulumi.getter
    def expires(self) -> pulumi.Output[str]:
        """
        Expires.
        """
        return pulumi.get(self, "expires")

    @property
    @pulumi.getter
    def genres(self) -> pulumi.Output[str]:
        """
        Genres.
        """
        return pulumi.get(self, "genres")

    @property
    @pulumi.getter
    def limit(self) -> pulumi.Output[int]:
        """
        Limit.
        """
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Import List name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> pulumi.Output[int]:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @property
    @pulumi.getter
    def rating(self) -> pulumi.Output[str]:
        """
        Rating.
        """
        return pulumi.get(self, "rating")

    @property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> pulumi.Output[str]:
        """
        Refresh token.
        """
        return pulumi.get(self, "refresh_token")

    @property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> pulumi.Output[str]:
        """
        Root folder path.
        """
        return pulumi.get(self, "root_folder_path")

    @property
    @pulumi.getter(name="seasonFolder")
    def season_folder(self) -> pulumi.Output[bool]:
        """
        Season folder flag.
        """
        return pulumi.get(self, "season_folder")

    @property
    @pulumi.getter(name="seriesType")
    def series_type(self) -> pulumi.Output[str]:
        """
        Series type.
        """
        return pulumi.get(self, "series_type")

    @property
    @pulumi.getter(name="shouldMonitor")
    def should_monitor(self) -> pulumi.Output[str]:
        """
        Should monitor.
        """
        return pulumi.get(self, "should_monitor")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="traktAdditionalParameters")
    def trakt_additional_parameters(self) -> pulumi.Output[str]:
        """
        Trakt additional parameters.
        """
        return pulumi.get(self, "trakt_additional_parameters")

    @property
    @pulumi.getter(name="traktListType")
    def trakt_list_type(self) -> pulumi.Output[int]:
        """
        Trakt list type. '0' Trending, '1' Popular, '2' Anticipated, '3' TopWatchedByWeek, '4' TopWatchedByMonth, '5' TopWatchedByYear, '6' TopWatchedByAllTime, '7' RecommendedByWeek, '8' RecommendedByMonth, '9' RecommendedByYear, '10' RecommendedByAllTime.
        """
        return pulumi.get(self, "trakt_list_type")

    @property
    @pulumi.getter
    def years(self) -> pulumi.Output[str]:
        """
        Years.
        """
        return pulumi.get(self, "years")

