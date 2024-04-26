# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TagArgs', 'Tag']

@pulumi.input_type
class TagArgs:
    def __init__(__self__, *,
                 label: pulumi.Input[str]):
        """
        The set of arguments for constructing a Tag resource.
        :param pulumi.Input[str] label: Tag label. It must be lowercase.
        """
        pulumi.set(__self__, "label", label)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        Tag label. It must be lowercase.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)


@pulumi.input_type
class _TagState:
    def __init__(__self__, *,
                 label: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Tag resources.
        :param pulumi.Input[str] label: Tag label. It must be lowercase.
        """
        if label is not None:
            pulumi.set(__self__, "label", label)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        Tag label. It must be lowercase.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)


class Tag(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- subcategory:Tags -->
        Tag resource.
        For more information refer to [Tags](https://wiki.servarr.com/sonarr/settings#tags) documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sonarr as sonarr

        example = sonarr.tags.Tag("example", label="some-value")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import sonarr:Tags/tag:Tag example 10
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] label: Tag label. It must be lowercase.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Tags -->
        Tag resource.
        For more information refer to [Tags](https://wiki.servarr.com/sonarr/settings#tags) documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_sonarr as sonarr

        example = sonarr.tags.Tag("example", label="some-value")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import sonarr:Tags/tag:Tag example 10
        ```

        :param str resource_name: The name of the resource.
        :param TagArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TagArgs.__new__(TagArgs)

            if label is None and not opts.urn:
                raise TypeError("Missing required property 'label'")
            __props__.__dict__["label"] = label
        super(Tag, __self__).__init__(
            'sonarr:Tags/tag:Tag',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            label: Optional[pulumi.Input[str]] = None) -> 'Tag':
        """
        Get an existing Tag resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] label: Tag label. It must be lowercase.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TagState.__new__(_TagState)

        __props__.__dict__["label"] = label
        return Tag(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        Tag label. It must be lowercase.
        """
        return pulumi.get(self, "label")

