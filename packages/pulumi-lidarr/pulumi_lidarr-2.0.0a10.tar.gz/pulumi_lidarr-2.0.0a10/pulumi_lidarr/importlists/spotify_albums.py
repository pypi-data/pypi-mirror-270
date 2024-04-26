# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SpotifyAlbumsArgs', 'SpotifyAlbums']

@pulumi.input_type
class SpotifyAlbumsArgs:
    def __init__(__self__, *,
                 access_token: pulumi.Input[str],
                 expires: pulumi.Input[str],
                 refresh_token: pulumi.Input[str],
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
        The set of arguments for constructing a SpotifyAlbums resource.
        :param pulumi.Input[str] access_token: Access token.
        :param pulumi.Input[str] expires: Expires.
        :param pulumi.Input[str] refresh_token: Refresh token.
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
        pulumi.set(__self__, "access_token", access_token)
        pulumi.set(__self__, "expires", expires)
        pulumi.set(__self__, "refresh_token", refresh_token)
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
    @pulumi.getter(name="accessToken")
    def access_token(self) -> pulumi.Input[str]:
        """
        Access token.
        """
        return pulumi.get(self, "access_token")

    @access_token.setter
    def access_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "access_token", value)

    @property
    @pulumi.getter
    def expires(self) -> pulumi.Input[str]:
        """
        Expires.
        """
        return pulumi.get(self, "expires")

    @expires.setter
    def expires(self, value: pulumi.Input[str]):
        pulumi.set(self, "expires", value)

    @property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> pulumi.Input[str]:
        """
        Refresh token.
        """
        return pulumi.get(self, "refresh_token")

    @refresh_token.setter
    def refresh_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "refresh_token", value)

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
class _SpotifyAlbumsState:
    def __init__(__self__, *,
                 access_token: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 metadata_profile_id: Optional[pulumi.Input[int]] = None,
                 monitor_new_items: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 refresh_token: Optional[pulumi.Input[str]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 should_monitor_existing: Optional[pulumi.Input[bool]] = None,
                 should_search: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering SpotifyAlbums resources.
        :param pulumi.Input[str] access_token: Access token.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[str] expires: Expires.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] metadata_profile_id: Metadata profile ID.
        :param pulumi.Input[str] monitor_new_items: Monitor new items.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] refresh_token: Refresh token.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[bool] should_monitor_existing: Should monitor existing flag.
        :param pulumi.Input[bool] should_search: Should search flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if access_token is not None:
            pulumi.set(__self__, "access_token", access_token)
        if enable_automatic_add is not None:
            pulumi.set(__self__, "enable_automatic_add", enable_automatic_add)
        if expires is not None:
            pulumi.set(__self__, "expires", expires)
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
        if refresh_token is not None:
            pulumi.set(__self__, "refresh_token", refresh_token)
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


class SpotifyAlbums(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_token: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 metadata_profile_id: Optional[pulumi.Input[int]] = None,
                 monitor_new_items: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 refresh_token: Optional[pulumi.Input[str]] = None,
                 root_folder_path: Optional[pulumi.Input[str]] = None,
                 should_monitor: Optional[pulumi.Input[str]] = None,
                 should_monitor_existing: Optional[pulumi.Input[bool]] = None,
                 should_search: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Import Lists -->Import List Spotify Albums resource.
        For more information refer to [Import List](https://wiki.servarr.com/lidarr/settings#import-lists) and [Spotify Albums](https://wiki.servarr.com/lidarr/supported#spotifysavedalbums).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.import_lists.SpotifyAlbums("example",
            access_token="accessToken",
            enable_automatic_add=False,
            expires="0001-01-01T00:01:00Z",
            metadata_profile_id=1,
            monitor_new_items="all",
            quality_profile_id=1,
            refresh_token="refreshToken",
            root_folder_path="/config",
            should_monitor="specificAlbum",
            should_search=False)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:ImportLists/spotifyAlbums:SpotifyAlbums example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_token: Access token.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[str] expires: Expires.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] metadata_profile_id: Metadata profile ID.
        :param pulumi.Input[str] monitor_new_items: Monitor new items.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] refresh_token: Refresh token.
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
                 args: SpotifyAlbumsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Import Lists -->Import List Spotify Albums resource.
        For more information refer to [Import List](https://wiki.servarr.com/lidarr/settings#import-lists) and [Spotify Albums](https://wiki.servarr.com/lidarr/supported#spotifysavedalbums).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.import_lists.SpotifyAlbums("example",
            access_token="accessToken",
            enable_automatic_add=False,
            expires="0001-01-01T00:01:00Z",
            metadata_profile_id=1,
            monitor_new_items="all",
            quality_profile_id=1,
            refresh_token="refreshToken",
            root_folder_path="/config",
            should_monitor="specificAlbum",
            should_search=False)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:ImportLists/spotifyAlbums:SpotifyAlbums example 1
        ```

        :param str resource_name: The name of the resource.
        :param SpotifyAlbumsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpotifyAlbumsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_token: Optional[pulumi.Input[str]] = None,
                 enable_automatic_add: Optional[pulumi.Input[bool]] = None,
                 expires: Optional[pulumi.Input[str]] = None,
                 list_order: Optional[pulumi.Input[int]] = None,
                 metadata_profile_id: Optional[pulumi.Input[int]] = None,
                 monitor_new_items: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_profile_id: Optional[pulumi.Input[int]] = None,
                 refresh_token: Optional[pulumi.Input[str]] = None,
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
            __props__ = SpotifyAlbumsArgs.__new__(SpotifyAlbumsArgs)

            if access_token is None and not opts.urn:
                raise TypeError("Missing required property 'access_token'")
            __props__.__dict__["access_token"] = None if access_token is None else pulumi.Output.secret(access_token)
            __props__.__dict__["enable_automatic_add"] = enable_automatic_add
            if expires is None and not opts.urn:
                raise TypeError("Missing required property 'expires'")
            __props__.__dict__["expires"] = expires
            __props__.__dict__["list_order"] = list_order
            __props__.__dict__["metadata_profile_id"] = metadata_profile_id
            __props__.__dict__["monitor_new_items"] = monitor_new_items
            __props__.__dict__["name"] = name
            __props__.__dict__["quality_profile_id"] = quality_profile_id
            if refresh_token is None and not opts.urn:
                raise TypeError("Missing required property 'refresh_token'")
            __props__.__dict__["refresh_token"] = None if refresh_token is None else pulumi.Output.secret(refresh_token)
            __props__.__dict__["root_folder_path"] = root_folder_path
            __props__.__dict__["should_monitor"] = should_monitor
            __props__.__dict__["should_monitor_existing"] = should_monitor_existing
            __props__.__dict__["should_search"] = should_search
            __props__.__dict__["tags"] = tags
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["accessToken", "refreshToken"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(SpotifyAlbums, __self__).__init__(
            'lidarr:ImportLists/spotifyAlbums:SpotifyAlbums',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_token: Optional[pulumi.Input[str]] = None,
            enable_automatic_add: Optional[pulumi.Input[bool]] = None,
            expires: Optional[pulumi.Input[str]] = None,
            list_order: Optional[pulumi.Input[int]] = None,
            metadata_profile_id: Optional[pulumi.Input[int]] = None,
            monitor_new_items: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            quality_profile_id: Optional[pulumi.Input[int]] = None,
            refresh_token: Optional[pulumi.Input[str]] = None,
            root_folder_path: Optional[pulumi.Input[str]] = None,
            should_monitor: Optional[pulumi.Input[str]] = None,
            should_monitor_existing: Optional[pulumi.Input[bool]] = None,
            should_search: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'SpotifyAlbums':
        """
        Get an existing SpotifyAlbums resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_token: Access token.
        :param pulumi.Input[bool] enable_automatic_add: Enable automatic add flag.
        :param pulumi.Input[str] expires: Expires.
        :param pulumi.Input[int] list_order: List order.
        :param pulumi.Input[int] metadata_profile_id: Metadata profile ID.
        :param pulumi.Input[str] monitor_new_items: Monitor new items.
        :param pulumi.Input[str] name: Import List name.
        :param pulumi.Input[int] quality_profile_id: Quality profile ID.
        :param pulumi.Input[str] refresh_token: Refresh token.
        :param pulumi.Input[str] root_folder_path: Root folder path.
        :param pulumi.Input[str] should_monitor: Should monitor.
        :param pulumi.Input[bool] should_monitor_existing: Should monitor existing flag.
        :param pulumi.Input[bool] should_search: Should search flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SpotifyAlbumsState.__new__(_SpotifyAlbumsState)

        __props__.__dict__["access_token"] = access_token
        __props__.__dict__["enable_automatic_add"] = enable_automatic_add
        __props__.__dict__["expires"] = expires
        __props__.__dict__["list_order"] = list_order
        __props__.__dict__["metadata_profile_id"] = metadata_profile_id
        __props__.__dict__["monitor_new_items"] = monitor_new_items
        __props__.__dict__["name"] = name
        __props__.__dict__["quality_profile_id"] = quality_profile_id
        __props__.__dict__["refresh_token"] = refresh_token
        __props__.__dict__["root_folder_path"] = root_folder_path
        __props__.__dict__["should_monitor"] = should_monitor
        __props__.__dict__["should_monitor_existing"] = should_monitor_existing
        __props__.__dict__["should_search"] = should_search
        __props__.__dict__["tags"] = tags
        return SpotifyAlbums(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> pulumi.Output[str]:
        """
        Access token.
        """
        return pulumi.get(self, "access_token")

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

