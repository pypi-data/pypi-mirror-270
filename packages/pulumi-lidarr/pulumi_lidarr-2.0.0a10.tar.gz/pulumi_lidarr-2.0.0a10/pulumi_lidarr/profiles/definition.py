# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['DefinitionArgs', 'Definition']

@pulumi.input_type
class DefinitionArgs:
    def __init__(__self__, *,
                 title: pulumi.Input[str],
                 max_size: Optional[pulumi.Input[float]] = None,
                 min_size: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a Definition resource.
        :param pulumi.Input[str] title: Quality Definition Title.
        :param pulumi.Input[float] max_size: Maximum size MB/min.
        :param pulumi.Input[float] min_size: Minimum size MB/min.
        """
        pulumi.set(__self__, "title", title)
        if max_size is not None:
            pulumi.set(__self__, "max_size", max_size)
        if min_size is not None:
            pulumi.set(__self__, "min_size", min_size)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        Quality Definition Title.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[float]]:
        """
        Maximum size MB/min.
        """
        return pulumi.get(self, "max_size")

    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_size", value)

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[float]]:
        """
        Minimum size MB/min.
        """
        return pulumi.get(self, "min_size")

    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_size", value)


@pulumi.input_type
class _DefinitionState:
    def __init__(__self__, *,
                 max_size: Optional[pulumi.Input[float]] = None,
                 min_size: Optional[pulumi.Input[float]] = None,
                 quality_id: Optional[pulumi.Input[int]] = None,
                 quality_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Definition resources.
        :param pulumi.Input[float] max_size: Maximum size MB/min.
        :param pulumi.Input[float] min_size: Minimum size MB/min.
        :param pulumi.Input[int] quality_id: Quality ID.
        :param pulumi.Input[str] quality_name: Quality Name.
        :param pulumi.Input[str] title: Quality Definition Title.
        """
        if max_size is not None:
            pulumi.set(__self__, "max_size", max_size)
        if min_size is not None:
            pulumi.set(__self__, "min_size", min_size)
        if quality_id is not None:
            pulumi.set(__self__, "quality_id", quality_id)
        if quality_name is not None:
            pulumi.set(__self__, "quality_name", quality_name)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> Optional[pulumi.Input[float]]:
        """
        Maximum size MB/min.
        """
        return pulumi.get(self, "max_size")

    @max_size.setter
    def max_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_size", value)

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> Optional[pulumi.Input[float]]:
        """
        Minimum size MB/min.
        """
        return pulumi.get(self, "min_size")

    @min_size.setter
    def min_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "min_size", value)

    @property
    @pulumi.getter(name="qualityId")
    def quality_id(self) -> Optional[pulumi.Input[int]]:
        """
        Quality ID.
        """
        return pulumi.get(self, "quality_id")

    @quality_id.setter
    def quality_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "quality_id", value)

    @property
    @pulumi.getter(name="qualityName")
    def quality_name(self) -> Optional[pulumi.Input[str]]:
        """
        Quality Name.
        """
        return pulumi.get(self, "quality_name")

    @quality_name.setter
    def quality_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "quality_name", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Quality Definition Title.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class Definition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 max_size: Optional[pulumi.Input[float]] = None,
                 min_size: Optional[pulumi.Input[float]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- subcategory:Profiles -->Quality Definition resource.
        For more information refer to [Quality Definition](https://wiki.servarr.com/lidarr/settings#quality-1) documentation.

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:Profiles/definition:Definition example 10
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] max_size: Maximum size MB/min.
        :param pulumi.Input[float] min_size: Minimum size MB/min.
        :param pulumi.Input[str] title: Quality Definition Title.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Profiles -->Quality Definition resource.
        For more information refer to [Quality Definition](https://wiki.servarr.com/lidarr/settings#quality-1) documentation.

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:Profiles/definition:Definition example 10
        ```

        :param str resource_name: The name of the resource.
        :param DefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 max_size: Optional[pulumi.Input[float]] = None,
                 min_size: Optional[pulumi.Input[float]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DefinitionArgs.__new__(DefinitionArgs)

            __props__.__dict__["max_size"] = max_size
            __props__.__dict__["min_size"] = min_size
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["quality_id"] = None
            __props__.__dict__["quality_name"] = None
        super(Definition, __self__).__init__(
            'lidarr:Profiles/definition:Definition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            max_size: Optional[pulumi.Input[float]] = None,
            min_size: Optional[pulumi.Input[float]] = None,
            quality_id: Optional[pulumi.Input[int]] = None,
            quality_name: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None) -> 'Definition':
        """
        Get an existing Definition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] max_size: Maximum size MB/min.
        :param pulumi.Input[float] min_size: Minimum size MB/min.
        :param pulumi.Input[int] quality_id: Quality ID.
        :param pulumi.Input[str] quality_name: Quality Name.
        :param pulumi.Input[str] title: Quality Definition Title.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DefinitionState.__new__(_DefinitionState)

        __props__.__dict__["max_size"] = max_size
        __props__.__dict__["min_size"] = min_size
        __props__.__dict__["quality_id"] = quality_id
        __props__.__dict__["quality_name"] = quality_name
        __props__.__dict__["title"] = title
        return Definition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="maxSize")
    def max_size(self) -> pulumi.Output[float]:
        """
        Maximum size MB/min.
        """
        return pulumi.get(self, "max_size")

    @property
    @pulumi.getter(name="minSize")
    def min_size(self) -> pulumi.Output[float]:
        """
        Minimum size MB/min.
        """
        return pulumi.get(self, "min_size")

    @property
    @pulumi.getter(name="qualityId")
    def quality_id(self) -> pulumi.Output[int]:
        """
        Quality ID.
        """
        return pulumi.get(self, "quality_id")

    @property
    @pulumi.getter(name="qualityName")
    def quality_name(self) -> pulumi.Output[str]:
        """
        Quality Name.
        """
        return pulumi.get(self, "quality_name")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        Quality Definition Title.
        """
        return pulumi.get(self, "title")

