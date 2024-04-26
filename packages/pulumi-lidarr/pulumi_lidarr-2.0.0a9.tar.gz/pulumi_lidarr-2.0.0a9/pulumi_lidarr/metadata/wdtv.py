# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WdtvArgs', 'Wdtv']

@pulumi.input_type
class WdtvArgs:
    def __init__(__self__, *,
                 track_metadata: pulumi.Input[bool],
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Wdtv resource.
        :param pulumi.Input[bool] track_metadata: Track metadata flag.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "track_metadata", track_metadata)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="trackMetadata")
    def track_metadata(self) -> pulumi.Input[bool]:
        """
        Track metadata flag.
        """
        return pulumi.get(self, "track_metadata")

    @track_metadata.setter
    def track_metadata(self, value: pulumi.Input[bool]):
        pulumi.set(self, "track_metadata", value)

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
class _WdtvState:
    def __init__(__self__, *,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 track_metadata: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Wdtv resources.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] track_metadata: Track metadata flag.
        """
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if track_metadata is not None:
            pulumi.set(__self__, "track_metadata", track_metadata)

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

    @property
    @pulumi.getter(name="trackMetadata")
    def track_metadata(self) -> Optional[pulumi.Input[bool]]:
        """
        Track metadata flag.
        """
        return pulumi.get(self, "track_metadata")

    @track_metadata.setter
    def track_metadata(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "track_metadata", value)


class Wdtv(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 track_metadata: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        <!-- subcategory:Metadata -->Metadata Wdtv resource.
        For more information refer to [Metadata](https://wiki.servarr.com/lidarr/settings#metadata) and [WDTV](https://wiki.servarr.com/lidarr/supported#wdtvmetadata).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.metadata.Wdtv("example",
            enable=True,
            track_metadata=True)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:Metadata/wdtv:Wdtv example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] track_metadata: Track metadata flag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WdtvArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Metadata -->Metadata Wdtv resource.
        For more information refer to [Metadata](https://wiki.servarr.com/lidarr/settings#metadata) and [WDTV](https://wiki.servarr.com/lidarr/supported#wdtvmetadata).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.metadata.Wdtv("example",
            enable=True,
            track_metadata=True)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:Metadata/wdtv:Wdtv example 1
        ```

        :param str resource_name: The name of the resource.
        :param WdtvArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WdtvArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 track_metadata: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WdtvArgs.__new__(WdtvArgs)

            __props__.__dict__["enable"] = enable
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            if track_metadata is None and not opts.urn:
                raise TypeError("Missing required property 'track_metadata'")
            __props__.__dict__["track_metadata"] = track_metadata
        super(Wdtv, __self__).__init__(
            'lidarr:Metadata/wdtv:Wdtv',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            track_metadata: Optional[pulumi.Input[bool]] = None) -> 'Wdtv':
        """
        Get an existing Wdtv resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] track_metadata: Track metadata flag.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WdtvState.__new__(_WdtvState)

        __props__.__dict__["enable"] = enable
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["track_metadata"] = track_metadata
        return Wdtv(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Metadata name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trackMetadata")
    def track_metadata(self) -> pulumi.Output[bool]:
        """
        Track metadata flag.
        """
        return pulumi.get(self, "track_metadata")

