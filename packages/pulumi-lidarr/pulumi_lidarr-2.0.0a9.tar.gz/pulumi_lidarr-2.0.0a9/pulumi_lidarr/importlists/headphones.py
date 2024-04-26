# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['HeadphonesArgs', 'Headphones']

@pulumi.input_type
class HeadphonesArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str],
                 base_url: pulumi.Input[str],
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 metadata_profile_id: Optional[pulumi.Input[int]] = None,
                 monitor_new_items: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 should_monitor_existing: Optional[pulumi.Input[bool]] = None,
                 should_search: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Headphones resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] metadata_profile_id: Metadata profile ID.
        :param pulumi.Input[str] monitor_new_items: Monitor new items.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[bool] should_monitor_existing: Should monitor existing flag.
        :param pulumi.Input[bool] should_search: Should search flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "api_key", api_key)
        pulumi.set(__self__, "base_url", base_url)
        if enable_automatic_add is not None:
            pulumi.set(__self__, "enable_automatic_add", enable_automatic_add)
        if list_order is not None:
            pulumi.set(__self__, "list_order", list_order)
        if metadata_profile_id is not None:
            pulumi.set(__self__, "metadata_profile_id", metadata_profile_id)
        if monitor_new_items is not None:
            pulumi.set(__self__, "monitor_new_items", monitor_new_items)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if quality_profile_id is not None:
            pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        if root_folder_path is not None:
            pulumi.set(__self__, "root_folder_path", root_folder_path)
        if should_monitor is not None:
            pulumi.set(__self__, "should_monitor", should_monitor)
        if should_monitor_existing is not None:
            pulumi.set(__self__, "should_monitor_existing", should_monitor_existing)
        if should_search is not None:
            pulumi.set(__self__, "should_search", should_search)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Input[str]:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_key", value)

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
    @pulumi.getter(name="listOrder")
    def list_order(self) -> Optional[pulumi.Input[int]]:
        """
        List order.
        """
        return pulumi.get(self, "list_order")

    @list_order.setter
    def list_order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "list_order", value)

    @property
    @pulumi.getter(name="metadataProfileId")
    def metadata_profile_id(self) -> Optional[pulumi.Input[int]]:
        """
        Metadata profile ID.
        """
        return pulumi.get(self, "metadata_profile_id")

    @metadata_profile_id.setter
    def metadata_profile_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "metadata_profile_id", value)

    @property
    @pulumi.getter(name="monitorNewItems")
    def monitor_new_items(self) -> Optional[pulumi.Input[str]]:
        """
        Monitor new items.
        """
        return pulumi.get(self, "monitor_new_items")

    @monitor_new_items.setter
    def monitor_new_items(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "monitor_new_items", value)

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
    @pulumi.getter(name="shouldMonitorExisting")
    def should_monitor_existing(self) -> Optional[pulumi.Input[bool]]:
        """
        Should monitor existing flag.
        """
        return pulumi.get(self, "should_monitor_existing")

    @should_monitor_existing.setter
    def should_monitor_existing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "should_monitor_existing", value)

    @property
    @pulumi.getter(name="shouldSearch")
    def should_search(self) -> Optional[pulumi.Input[bool]]:
        """
        Should search flag.
        """
        return pulumi.get(self, "should_search")

    @should_search.setter
    def should_search(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "should_search", value)

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
class _HeadphonesState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 metadata_profile_id: Optional[pulumi.Input[int]] = None,
                 monitor_new_items: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 should_monitor_existing: Optional[pulumi.Input[bool]] = None,
                 should_search: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Headphones resources.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] metadata_profile_id: Metadata profile ID.
        :param pulumi.Input[str] monitor_new_items: Monitor new items.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[bool] should_monitor_existing: Should monitor existing flag.
        :param pulumi.Input[bool] should_search: Should search flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if base_url is not None:
            pulumi.set(__self__, "base_url", base_url)
        if enable_automatic_add is not None:
            pulumi.set(__self__, "enable_automatic_add", enable_automatic_add)
        if list_order is not None:
            pulumi.set(__self__, "list_order", list_order)
        if metadata_profile_id is not None:
            pulumi.set(__self__, "metadata_profile_id", metadata_profile_id)
        if monitor_new_items is not None:
            pulumi.set(__self__, "monitor_new_items", monitor_new_items)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if quality_profile_id is not None:
            pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        if root_folder_path is not None:
            pulumi.set(__self__, "root_folder_path", root_folder_path)
        if should_monitor is not None:
            pulumi.set(__self__, "should_monitor", should_monitor)
        if should_monitor_existing is not None:
            pulumi.set(__self__, "should_monitor_existing", should_monitor_existing)
        if should_search is not None:
            pulumi.set(__self__, "should_search", should_search)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

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
    @pulumi.getter(name="listOrder")
    def list_order(self) -> Optional[pulumi.Input[int]]:
        """
        List order.
        """
        return pulumi.get(self, "list_order")

    @list_order.setter
    def list_order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "list_order", value)

    @property
    @pulumi.getter(name="metadataProfileId")
    def metadata_profile_id(self) -> Optional[pulumi.Input[int]]:
        """
        Metadata profile ID.
        """
        return pulumi.get(self, "metadata_profile_id")

    @metadata_profile_id.setter
    def metadata_profile_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "metadata_profile_id", value)

    @property
    @pulumi.getter(name="monitorNewItems")
    def monitor_new_items(self) -> Optional[pulumi.Input[str]]:
        """
        Monitor new items.
        """
        return pulumi.get(self, "monitor_new_items")

    @monitor_new_items.setter
    def monitor_new_items(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "monitor_new_items", value)

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
    @pulumi.getter(name="shouldMonitorExisting")
    def should_monitor_existing(self) -> Optional[pulumi.Input[bool]]:
        """
        Should monitor existing flag.
        """
        return pulumi.get(self, "should_monitor_existing")

    @should_monitor_existing.setter
    def should_monitor_existing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "should_monitor_existing", value)

    @property
    @pulumi.getter(name="shouldSearch")
    def should_search(self) -> Optional[pulumi.Input[bool]]:
        """
        Should search flag.
        """
        return pulumi.get(self, "should_search")

    @should_search.setter
    def should_search(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "should_search", value)

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


class Headphones(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 metadata_profile_id: Optional[pulumi.Input[int]] = None,
                 monitor_new_items: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 should_monitor_existing: Optional[pulumi.Input[bool]] = None,
                 should_search: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Import Lists -->Import List Headphones resource.
        For more information refer to [Import List](https://wiki.servarr.com/lidarr/settings#import-lists) and [Headphones](https://wiki.servarr.com/lidarr/supported#headphonesimport).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.import_lists.Headphones("example",
            api_key="APIKey",
            base_url="http://127.0.0.1:8181",
            enable_automatic_add=False,
            metadata_profile_id=1,
            monitor_new_items="all",
            quality_profile_id=1,
            root_folder_path="/config",
            should_monitor="specificAlbum",
            should_search=False,
            tags=[
                1,
                2,
                3,
            ])
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:ImportLists/headphones:Headphones example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] metadata_profile_id: Metadata profile ID.
        :param pulumi.Input[str] monitor_new_items: Monitor new items.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[bool] should_monitor_existing: Should monitor existing flag.
        :param pulumi.Input[bool] should_search: Should search flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HeadphonesArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Import Lists -->Import List Headphones resource.
        For more information refer to [Import List](https://wiki.servarr.com/lidarr/settings#import-lists) and [Headphones](https://wiki.servarr.com/lidarr/supported#headphonesimport).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.import_lists.Headphones("example",
            api_key="APIKey",
            base_url="http://127.0.0.1:8181",
            enable_automatic_add=False,
            metadata_profile_id=1,
            monitor_new_items="all",
            quality_profile_id=1,
            root_folder_path="/config",
            should_monitor="specificAlbum",
            should_search=False,
            tags=[
                1,
                2,
                3,
            ])
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:ImportLists/headphones:Headphones example 1
        ```

        :param str resource_name: The name of the resource.
        :param HeadphonesArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HeadphonesArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 metadata_profile_id: Optional[pulumi.Input[int]] = None,
                 monitor_new_items: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 should_monitor_existing: Optional[pulumi.Input[bool]] = None,
                 should_search: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HeadphonesArgs.__new__(HeadphonesArgs)

            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            if base_url is None and not opts.urn:
                raise TypeError("Missing required property 'base_url'")
            __props__.__dict__["base_url"] = base_url
            __props__.__dict__["enable_automatic_add"] = enable_automatic_add
            __props__.__dict__["list_order"] = list_order
            __props__.__dict__["metadata_profile_id"] = metadata_profile_id
            __props__.__dict__["monitor_new_items"] = monitor_new_items
            __props__.__dict__["name"] = name
            __props__.__dict__["quality_profile_id"] = quality_profile_id
            __props__.__dict__["root_folder_path"] = root_folder_path
            __props__.__dict__["should_monitor"] = should_monitor
            __props__.__dict__["should_monitor_existing"] = should_monitor_existing
            __props__.__dict__["should_search"] = should_search
            __props__.__dict__["tags"] = tags
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Headphones, __self__).__init__(
            'lidarr:ImportLists/headphones:Headphones',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            base_url: Optional[pulumi.Input[str]] = None,
            enable_automatic_add: Optional[pulumi.Input[bool]] = None,
            list_order: Optional[pulumi.Input[int]] = None,
            metadata_profile_id: Optional[pulumi.Input[int]] = None,
            monitor_new_items: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            quality_profile_id: Optional[pulumi.Input[int]] = None,
            root_folder_path: Optional[pulumi.Input[str]] = None,
            should_monitor: Optional[pulumi.Input[str]] = None,
            should_monitor_existing: Optional[pulumi.Input[bool]] = None,
            should_search: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Headphones':
        """
        Get an existing Headphones resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] metadata_profile_id: Metadata profile ID.
        :param pulumi.Input[str] monitor_new_items: Monitor new items.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[bool] should_monitor_existing: Should monitor existing flag.
        :param pulumi.Input[bool] should_search: Should search flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HeadphonesState.__new__(_HeadphonesState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["base_url"] = base_url
        __props__.__dict__["enable_automatic_add"] = enable_automatic_add
        __props__.__dict__["list_order"] = list_order
        __props__.__dict__["metadata_profile_id"] = metadata_profile_id
        __props__.__dict__["monitor_new_items"] = monitor_new_items
        __props__.__dict__["name"] = name
        __props__.__dict__["quality_profile_id"] = quality_profile_id
        __props__.__dict__["root_folder_path"] = root_folder_path
        __props__.__dict__["should_monitor"] = should_monitor
        __props__.__dict__["should_monitor_existing"] = should_monitor_existing
        __props__.__dict__["should_search"] = should_search
        __props__.__dict__["tags"] = tags
        return Headphones(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Output[str]:
        """
        Base URL.
        """
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter(name="enableAutomaticAdd")
    def enable_automatic_add(self) -> pulumi.Output[bool]:
        """
        Enable automatic add flag.
        """
        return pulumi.get(self, "enable_automatic_add")

    @property
    @pulumi.getter(name="listOrder")
    def list_order(self) -> pulumi.Output[int]:
        """
        List order.
        """
        return pulumi.get(self, "list_order")

    @property
    @pulumi.getter(name="metadataProfileId")
    def metadata_profile_id(self) -> pulumi.Output[int]:
        """
        Metadata profile ID.
        """
        return pulumi.get(self, "metadata_profile_id")

    @property
    @pulumi.getter(name="monitorNewItems")
    def monitor_new_items(self) -> pulumi.Output[str]:
        """
        Monitor new items.
        """
        return pulumi.get(self, "monitor_new_items")

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
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> pulumi.Output[str]:
        """
        Root folder path.
        """
        return pulumi.get(self, "root_folder_path")

    @property
    @pulumi.getter(name="shouldMonitor")
    def should_monitor(self) -> pulumi.Output[str]:
        """
        Should monitor.
        """
        return pulumi.get(self, "should_monitor")

    @property
    @pulumi.getter(name="shouldMonitorExisting")
    def should_monitor_existing(self) -> pulumi.Output[bool]:
        """
        Should monitor existing flag.
        """
        return pulumi.get(self, "should_monitor_existing")

    @property
    @pulumi.getter(name="shouldSearch")
    def should_search(self) -> pulumi.Output[bool]:
        """
        Should search flag.
        """
        return pulumi.get(self, "should_search")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

