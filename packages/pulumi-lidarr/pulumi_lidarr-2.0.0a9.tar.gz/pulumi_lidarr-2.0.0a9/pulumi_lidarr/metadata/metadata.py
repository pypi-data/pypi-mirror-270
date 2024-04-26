# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MetadataArgs', 'Metadata']

@pulumi.input_type
class MetadataArgs:
    def __init__(__self__, *,
                 config_contract: pulumi.Input[str],
                 implementation: pulumi.Input[str],
                 album_images: Optional[pulumi.Input[bool]] = None,
                 album_metadata: Optional[pulumi.Input[bool]] = None,
                 artist_images: Optional[pulumi.Input[bool]] = None,
                 artist_metadata: Optional[pulumi.Input[bool]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 track_metadata: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Metadata resource.
        :param pulumi.Input[str] config_contract: Metadata configuration template.
        :param pulumi.Input[str] implementation: Metadata implementation name.
        :param pulumi.Input[bool] album_images: Album images flag.
        :param pulumi.Input[bool] album_metadata: Album metadata flag.
        :param pulumi.Input[bool] artist_images: Artist images flag.
        :param pulumi.Input[bool] artist_metadata: Artist metadata flag.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] track_metadata: Track metadata flag.
        """
        pulumi.set(__self__, "config_contract", config_contract)
        pulumi.set(__self__, "implementation", implementation)
        if album_images is not None:
            pulumi.set(__self__, "album_images", album_images)
        if album_metadata is not None:
            pulumi.set(__self__, "album_metadata", album_metadata)
        if artist_images is not None:
            pulumi.set(__self__, "artist_images", artist_images)
        if artist_metadata is not None:
            pulumi.set(__self__, "artist_metadata", artist_metadata)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if track_metadata is not None:
            pulumi.set(__self__, "track_metadata", track_metadata)

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> pulumi.Input[str]:
        """
        Metadata configuration template.
        """
        return pulumi.get(self, "config_contract")

    @config_contract.setter
    def config_contract(self, value: pulumi.Input[str]):
        pulumi.set(self, "config_contract", value)

    @property
    @pulumi.getter
    def implementation(self) -> pulumi.Input[str]:
        """
        Metadata implementation name.
        """
        return pulumi.get(self, "implementation")

    @implementation.setter
    def implementation(self, value: pulumi.Input[str]):
        pulumi.set(self, "implementation", value)

    @property
    @pulumi.getter(name="albumImages")
    def album_images(self) -> Optional[pulumi.Input[bool]]:
        """
        Album images flag.
        """
        return pulumi.get(self, "album_images")

    @album_images.setter
    def album_images(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "album_images", value)

    @property
    @pulumi.getter(name="albumMetadata")
    def album_metadata(self) -> Optional[pulumi.Input[bool]]:
        """
        Album metadata flag.
        """
        return pulumi.get(self, "album_metadata")

    @album_metadata.setter
    def album_metadata(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "album_metadata", value)

    @property
    @pulumi.getter(name="artistImages")
    def artist_images(self) -> Optional[pulumi.Input[bool]]:
        """
        Artist images flag.
        """
        return pulumi.get(self, "artist_images")

    @artist_images.setter
    def artist_images(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "artist_images", value)

    @property
    @pulumi.getter(name="artistMetadata")
    def artist_metadata(self) -> Optional[pulumi.Input[bool]]:
        """
        Artist metadata flag.
        """
        return pulumi.get(self, "artist_metadata")

    @artist_metadata.setter
    def artist_metadata(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "artist_metadata", value)

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


@pulumi.input_type
class _MetadataState:
    def __init__(__self__, *,
                 album_images: Optional[pulumi.Input[bool]] = None,
                 album_metadata: Optional[pulumi.Input[bool]] = None,
                 artist_images: Optional[pulumi.Input[bool]] = None,
                 artist_metadata: Optional[pulumi.Input[bool]] = None,
                 config_contract: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 implementation: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 track_metadata: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Metadata resources.
        :param pulumi.Input[bool] album_images: Album images flag.
        :param pulumi.Input[bool] album_metadata: Album metadata flag.
        :param pulumi.Input[bool] artist_images: Artist images flag.
        :param pulumi.Input[bool] artist_metadata: Artist metadata flag.
        :param pulumi.Input[str] config_contract: Metadata configuration template.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] implementation: Metadata implementation name.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] track_metadata: Track metadata flag.
        """
        if album_images is not None:
            pulumi.set(__self__, "album_images", album_images)
        if album_metadata is not None:
            pulumi.set(__self__, "album_metadata", album_metadata)
        if artist_images is not None:
            pulumi.set(__self__, "artist_images", artist_images)
        if artist_metadata is not None:
            pulumi.set(__self__, "artist_metadata", artist_metadata)
        if config_contract is not None:
            pulumi.set(__self__, "config_contract", config_contract)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if implementation is not None:
            pulumi.set(__self__, "implementation", implementation)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if track_metadata is not None:
            pulumi.set(__self__, "track_metadata", track_metadata)

    @property
    @pulumi.getter(name="albumImages")
    def album_images(self) -> Optional[pulumi.Input[bool]]:
        """
        Album images flag.
        """
        return pulumi.get(self, "album_images")

    @album_images.setter
    def album_images(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "album_images", value)

    @property
    @pulumi.getter(name="albumMetadata")
    def album_metadata(self) -> Optional[pulumi.Input[bool]]:
        """
        Album metadata flag.
        """
        return pulumi.get(self, "album_metadata")

    @album_metadata.setter
    def album_metadata(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "album_metadata", value)

    @property
    @pulumi.getter(name="artistImages")
    def artist_images(self) -> Optional[pulumi.Input[bool]]:
        """
        Artist images flag.
        """
        return pulumi.get(self, "artist_images")

    @artist_images.setter
    def artist_images(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "artist_images", value)

    @property
    @pulumi.getter(name="artistMetadata")
    def artist_metadata(self) -> Optional[pulumi.Input[bool]]:
        """
        Artist metadata flag.
        """
        return pulumi.get(self, "artist_metadata")

    @artist_metadata.setter
    def artist_metadata(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "artist_metadata", value)

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> Optional[pulumi.Input[str]]:
        """
        Metadata configuration template.
        """
        return pulumi.get(self, "config_contract")

    @config_contract.setter
    def config_contract(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_contract", value)

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
    def implementation(self) -> Optional[pulumi.Input[str]]:
        """
        Metadata implementation name.
        """
        return pulumi.get(self, "implementation")

    @implementation.setter
    def implementation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "implementation", value)

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


class Metadata(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 album_images: Optional[pulumi.Input[bool]] = None,
                 album_metadata: Optional[pulumi.Input[bool]] = None,
                 artist_images: Optional[pulumi.Input[bool]] = None,
                 artist_metadata: Optional[pulumi.Input[bool]] = None,
                 config_contract: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 implementation: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 track_metadata: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        <!-- subcategory:Metadata -->Generic Metadata resource. When possible use a specific resource instead.
        For more information refer to [Metadata](https://wiki.servarr.com/lidarr/settings#metadata) documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.metadata.Metadata("example",
            config_contract="WdtvMetadataSettings",
            enable=True,
            implementation="WdtvMetadata",
            tags=[
                1,
                2,
            ],
            track_metadata=True)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:Metadata/metadata:Metadata example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] album_images: Album images flag.
        :param pulumi.Input[bool] album_metadata: Album metadata flag.
        :param pulumi.Input[bool] artist_images: Artist images flag.
        :param pulumi.Input[bool] artist_metadata: Artist metadata flag.
        :param pulumi.Input[str] config_contract: Metadata configuration template.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] implementation: Metadata implementation name.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] track_metadata: Track metadata flag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetadataArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Metadata -->Generic Metadata resource. When possible use a specific resource instead.
        For more information refer to [Metadata](https://wiki.servarr.com/lidarr/settings#metadata) documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.metadata.Metadata("example",
            config_contract="WdtvMetadataSettings",
            enable=True,
            implementation="WdtvMetadata",
            tags=[
                1,
                2,
            ],
            track_metadata=True)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:Metadata/metadata:Metadata example 1
        ```

        :param str resource_name: The name of the resource.
        :param MetadataArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetadataArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 album_images: Optional[pulumi.Input[bool]] = None,
                 album_metadata: Optional[pulumi.Input[bool]] = None,
                 artist_images: Optional[pulumi.Input[bool]] = None,
                 artist_metadata: Optional[pulumi.Input[bool]] = None,
                 config_contract: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 implementation: Optional[pulumi.Input[str]] = None,
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
            __props__ = MetadataArgs.__new__(MetadataArgs)

            __props__.__dict__["album_images"] = album_images
            __props__.__dict__["album_metadata"] = album_metadata
            __props__.__dict__["artist_images"] = artist_images
            __props__.__dict__["artist_metadata"] = artist_metadata
            if config_contract is None and not opts.urn:
                raise TypeError("Missing required property 'config_contract'")
            __props__.__dict__["config_contract"] = config_contract
            __props__.__dict__["enable"] = enable
            if implementation is None and not opts.urn:
                raise TypeError("Missing required property 'implementation'")
            __props__.__dict__["implementation"] = implementation
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["track_metadata"] = track_metadata
        super(Metadata, __self__).__init__(
            'lidarr:Metadata/metadata:Metadata',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            album_images: Optional[pulumi.Input[bool]] = None,
            album_metadata: Optional[pulumi.Input[bool]] = None,
            artist_images: Optional[pulumi.Input[bool]] = None,
            artist_metadata: Optional[pulumi.Input[bool]] = None,
            config_contract: Optional[pulumi.Input[str]] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            implementation: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            track_metadata: Optional[pulumi.Input[bool]] = None) -> 'Metadata':
        """
        Get an existing Metadata resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] album_images: Album images flag.
        :param pulumi.Input[bool] album_metadata: Album metadata flag.
        :param pulumi.Input[bool] artist_images: Artist images flag.
        :param pulumi.Input[bool] artist_metadata: Artist metadata flag.
        :param pulumi.Input[str] config_contract: Metadata configuration template.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] implementation: Metadata implementation name.
        :param pulumi.Input[str] name: Metadata name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] track_metadata: Track metadata flag.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MetadataState.__new__(_MetadataState)

        __props__.__dict__["album_images"] = album_images
        __props__.__dict__["album_metadata"] = album_metadata
        __props__.__dict__["artist_images"] = artist_images
        __props__.__dict__["artist_metadata"] = artist_metadata
        __props__.__dict__["config_contract"] = config_contract
        __props__.__dict__["enable"] = enable
        __props__.__dict__["implementation"] = implementation
        __props__.__dict__["name"] = name
        __props__.__dict__["tags"] = tags
        __props__.__dict__["track_metadata"] = track_metadata
        return Metadata(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="albumImages")
    def album_images(self) -> pulumi.Output[bool]:
        """
        Album images flag.
        """
        return pulumi.get(self, "album_images")

    @property
    @pulumi.getter(name="albumMetadata")
    def album_metadata(self) -> pulumi.Output[bool]:
        """
        Album metadata flag.
        """
        return pulumi.get(self, "album_metadata")

    @property
    @pulumi.getter(name="artistImages")
    def artist_images(self) -> pulumi.Output[bool]:
        """
        Artist images flag.
        """
        return pulumi.get(self, "artist_images")

    @property
    @pulumi.getter(name="artistMetadata")
    def artist_metadata(self) -> pulumi.Output[bool]:
        """
        Artist metadata flag.
        """
        return pulumi.get(self, "artist_metadata")

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> pulumi.Output[str]:
        """
        Metadata configuration template.
        """
        return pulumi.get(self, "config_contract")

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def implementation(self) -> pulumi.Output[str]:
        """
        Metadata implementation name.
        """
        return pulumi.get(self, "implementation")

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

