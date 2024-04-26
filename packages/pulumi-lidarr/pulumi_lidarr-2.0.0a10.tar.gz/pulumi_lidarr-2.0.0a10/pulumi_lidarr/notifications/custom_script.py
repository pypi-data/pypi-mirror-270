# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CustomScriptArgs', 'CustomScript']

@pulumi.input_type
class CustomScriptArgs:
    def __init__(__self__, *,
                 path: pulumi.Input[str],
                 arguments: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_album_delete: Optional[pulumi.Input[bool]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_artist_delete: Optional[pulumi.Input[bool]] = None,
                 on_download_failure: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 on_import_failure: Optional[pulumi.Input[bool]] = None,
                 on_release_import: Optional[pulumi.Input[bool]] = None,
                 on_rename: Optional[pulumi.Input[bool]] = None,
                 on_track_retag: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a CustomScript resource.
        :param pulumi.Input[str] path: Path.
        :param pulumi.Input[str] arguments: Arguments.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: NotificationCustomScript name.
        :param pulumi.Input[bool] on_album_delete: On album delete flag.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_artist_delete: On artist delete flag.
        :param pulumi.Input[bool] on_download_failure: On download failure flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[bool] on_import_failure: On import failure flag.
        :param pulumi.Input[bool] on_release_import: On release import flag.
        :param pulumi.Input[bool] on_rename: On rename flag.
        :param pulumi.Input[bool] on_track_retag: On track retag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "path", path)
        if arguments is not None:
            pulumi.set(__self__, "arguments", arguments)
        if include_health_warnings is not None:
            pulumi.set(__self__, "include_health_warnings", include_health_warnings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if on_album_delete is not None:
            pulumi.set(__self__, "on_album_delete", on_album_delete)
        if on_application_update is not None:
            pulumi.set(__self__, "on_application_update", on_application_update)
        if on_artist_delete is not None:
            pulumi.set(__self__, "on_artist_delete", on_artist_delete)
        if on_download_failure is not None:
            pulumi.set(__self__, "on_download_failure", on_download_failure)
        if on_grab is not None:
            pulumi.set(__self__, "on_grab", on_grab)
        if on_health_issue is not None:
            pulumi.set(__self__, "on_health_issue", on_health_issue)
        if on_health_restored is not None:
            pulumi.set(__self__, "on_health_restored", on_health_restored)
        if on_import_failure is not None:
            pulumi.set(__self__, "on_import_failure", on_import_failure)
        if on_release_import is not None:
            pulumi.set(__self__, "on_release_import", on_release_import)
        if on_rename is not None:
            pulumi.set(__self__, "on_rename", on_rename)
        if on_track_retag is not None:
            pulumi.set(__self__, "on_track_retag", on_track_retag)
        if on_upgrade is not None:
            pulumi.set(__self__, "on_upgrade", on_upgrade)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        Path.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[str]]:
        """
        Arguments.
        """
        return pulumi.get(self, "arguments")

    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arguments", value)

    @property
    @pulumi.getter(name="includeHealthWarnings")
    def include_health_warnings(self) -> Optional[pulumi.Input[bool]]:
        """
        Include health warnings.
        """
        return pulumi.get(self, "include_health_warnings")

    @include_health_warnings.setter
    def include_health_warnings(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_health_warnings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        NotificationCustomScript name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="onAlbumDelete")
    def on_album_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On album delete flag.
        """
        return pulumi.get(self, "on_album_delete")

    @on_album_delete.setter
    def on_album_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_album_delete", value)

    @property
    @pulumi.getter(name="onApplicationUpdate")
    def on_application_update(self) -> Optional[pulumi.Input[bool]]:
        """
        On application update flag.
        """
        return pulumi.get(self, "on_application_update")

    @on_application_update.setter
    def on_application_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_application_update", value)

    @property
    @pulumi.getter(name="onArtistDelete")
    def on_artist_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On artist delete flag.
        """
        return pulumi.get(self, "on_artist_delete")

    @on_artist_delete.setter
    def on_artist_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_artist_delete", value)

    @property
    @pulumi.getter(name="onDownloadFailure")
    def on_download_failure(self) -> Optional[pulumi.Input[bool]]:
        """
        On download failure flag.
        """
        return pulumi.get(self, "on_download_failure")

    @on_download_failure.setter
    def on_download_failure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_download_failure", value)

    @property
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> Optional[pulumi.Input[bool]]:
        """
        On grab flag.
        """
        return pulumi.get(self, "on_grab")

    @on_grab.setter
    def on_grab(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_grab", value)

    @property
    @pulumi.getter(name="onHealthIssue")
    def on_health_issue(self) -> Optional[pulumi.Input[bool]]:
        """
        On health issue flag.
        """
        return pulumi.get(self, "on_health_issue")

    @on_health_issue.setter
    def on_health_issue(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_issue", value)

    @property
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> Optional[pulumi.Input[bool]]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @on_health_restored.setter
    def on_health_restored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_restored", value)

    @property
    @pulumi.getter(name="onImportFailure")
    def on_import_failure(self) -> Optional[pulumi.Input[bool]]:
        """
        On import failure flag.
        """
        return pulumi.get(self, "on_import_failure")

    @on_import_failure.setter
    def on_import_failure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_import_failure", value)

    @property
    @pulumi.getter(name="onReleaseImport")
    def on_release_import(self) -> Optional[pulumi.Input[bool]]:
        """
        On release import flag.
        """
        return pulumi.get(self, "on_release_import")

    @on_release_import.setter
    def on_release_import(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_release_import", value)

    @property
    @pulumi.getter(name="onRename")
    def on_rename(self) -> Optional[pulumi.Input[bool]]:
        """
        On rename flag.
        """
        return pulumi.get(self, "on_rename")

    @on_rename.setter
    def on_rename(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_rename", value)

    @property
    @pulumi.getter(name="onTrackRetag")
    def on_track_retag(self) -> Optional[pulumi.Input[bool]]:
        """
        On track retag.
        """
        return pulumi.get(self, "on_track_retag")

    @on_track_retag.setter
    def on_track_retag(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_track_retag", value)

    @property
    @pulumi.getter(name="onUpgrade")
    def on_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        On upgrade flag.
        """
        return pulumi.get(self, "on_upgrade")

    @on_upgrade.setter
    def on_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_upgrade", value)

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
class _CustomScriptState:
    def __init__(__self__, *,
                 arguments: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_album_delete: Optional[pulumi.Input[bool]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_artist_delete: Optional[pulumi.Input[bool]] = None,
                 on_download_failure: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 on_import_failure: Optional[pulumi.Input[bool]] = None,
                 on_release_import: Optional[pulumi.Input[bool]] = None,
                 on_rename: Optional[pulumi.Input[bool]] = None,
                 on_track_retag: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering CustomScript resources.
        :param pulumi.Input[str] arguments: Arguments.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: NotificationCustomScript name.
        :param pulumi.Input[bool] on_album_delete: On album delete flag.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_artist_delete: On artist delete flag.
        :param pulumi.Input[bool] on_download_failure: On download failure flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[bool] on_import_failure: On import failure flag.
        :param pulumi.Input[bool] on_release_import: On release import flag.
        :param pulumi.Input[bool] on_rename: On rename flag.
        :param pulumi.Input[bool] on_track_retag: On track retag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[str] path: Path.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if arguments is not None:
            pulumi.set(__self__, "arguments", arguments)
        if include_health_warnings is not None:
            pulumi.set(__self__, "include_health_warnings", include_health_warnings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if on_album_delete is not None:
            pulumi.set(__self__, "on_album_delete", on_album_delete)
        if on_application_update is not None:
            pulumi.set(__self__, "on_application_update", on_application_update)
        if on_artist_delete is not None:
            pulumi.set(__self__, "on_artist_delete", on_artist_delete)
        if on_download_failure is not None:
            pulumi.set(__self__, "on_download_failure", on_download_failure)
        if on_grab is not None:
            pulumi.set(__self__, "on_grab", on_grab)
        if on_health_issue is not None:
            pulumi.set(__self__, "on_health_issue", on_health_issue)
        if on_health_restored is not None:
            pulumi.set(__self__, "on_health_restored", on_health_restored)
        if on_import_failure is not None:
            pulumi.set(__self__, "on_import_failure", on_import_failure)
        if on_release_import is not None:
            pulumi.set(__self__, "on_release_import", on_release_import)
        if on_rename is not None:
            pulumi.set(__self__, "on_rename", on_rename)
        if on_track_retag is not None:
            pulumi.set(__self__, "on_track_retag", on_track_retag)
        if on_upgrade is not None:
            pulumi.set(__self__, "on_upgrade", on_upgrade)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[str]]:
        """
        Arguments.
        """
        return pulumi.get(self, "arguments")

    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arguments", value)

    @property
    @pulumi.getter(name="includeHealthWarnings")
    def include_health_warnings(self) -> Optional[pulumi.Input[bool]]:
        """
        Include health warnings.
        """
        return pulumi.get(self, "include_health_warnings")

    @include_health_warnings.setter
    def include_health_warnings(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_health_warnings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        NotificationCustomScript name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="onAlbumDelete")
    def on_album_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On album delete flag.
        """
        return pulumi.get(self, "on_album_delete")

    @on_album_delete.setter
    def on_album_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_album_delete", value)

    @property
    @pulumi.getter(name="onApplicationUpdate")
    def on_application_update(self) -> Optional[pulumi.Input[bool]]:
        """
        On application update flag.
        """
        return pulumi.get(self, "on_application_update")

    @on_application_update.setter
    def on_application_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_application_update", value)

    @property
    @pulumi.getter(name="onArtistDelete")
    def on_artist_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On artist delete flag.
        """
        return pulumi.get(self, "on_artist_delete")

    @on_artist_delete.setter
    def on_artist_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_artist_delete", value)

    @property
    @pulumi.getter(name="onDownloadFailure")
    def on_download_failure(self) -> Optional[pulumi.Input[bool]]:
        """
        On download failure flag.
        """
        return pulumi.get(self, "on_download_failure")

    @on_download_failure.setter
    def on_download_failure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_download_failure", value)

    @property
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> Optional[pulumi.Input[bool]]:
        """
        On grab flag.
        """
        return pulumi.get(self, "on_grab")

    @on_grab.setter
    def on_grab(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_grab", value)

    @property
    @pulumi.getter(name="onHealthIssue")
    def on_health_issue(self) -> Optional[pulumi.Input[bool]]:
        """
        On health issue flag.
        """
        return pulumi.get(self, "on_health_issue")

    @on_health_issue.setter
    def on_health_issue(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_issue", value)

    @property
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> Optional[pulumi.Input[bool]]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @on_health_restored.setter
    def on_health_restored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_restored", value)

    @property
    @pulumi.getter(name="onImportFailure")
    def on_import_failure(self) -> Optional[pulumi.Input[bool]]:
        """
        On import failure flag.
        """
        return pulumi.get(self, "on_import_failure")

    @on_import_failure.setter
    def on_import_failure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_import_failure", value)

    @property
    @pulumi.getter(name="onReleaseImport")
    def on_release_import(self) -> Optional[pulumi.Input[bool]]:
        """
        On release import flag.
        """
        return pulumi.get(self, "on_release_import")

    @on_release_import.setter
    def on_release_import(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_release_import", value)

    @property
    @pulumi.getter(name="onRename")
    def on_rename(self) -> Optional[pulumi.Input[bool]]:
        """
        On rename flag.
        """
        return pulumi.get(self, "on_rename")

    @on_rename.setter
    def on_rename(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_rename", value)

    @property
    @pulumi.getter(name="onTrackRetag")
    def on_track_retag(self) -> Optional[pulumi.Input[bool]]:
        """
        On track retag.
        """
        return pulumi.get(self, "on_track_retag")

    @on_track_retag.setter
    def on_track_retag(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_track_retag", value)

    @property
    @pulumi.getter(name="onUpgrade")
    def on_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        On upgrade flag.
        """
        return pulumi.get(self, "on_upgrade")

    @on_upgrade.setter
    def on_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_upgrade", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Path.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

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


class CustomScript(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arguments: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_album_delete: Optional[pulumi.Input[bool]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_artist_delete: Optional[pulumi.Input[bool]] = None,
                 on_download_failure: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 on_import_failure: Optional[pulumi.Input[bool]] = None,
                 on_release_import: Optional[pulumi.Input[bool]] = None,
                 on_rename: Optional[pulumi.Input[bool]] = None,
                 on_track_retag: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Notifications -->Notification Custom Script resource.
        For more information refer to [Notification](https://wiki.servarr.com/lidarr/settings#connect) and [Custom Script](https://wiki.servarr.com/lidarr/supported#customscript).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.notifications.CustomScript("example",
            include_health_warnings=False,
            on_application_update=False,
            on_download_failure=False,
            on_grab=False,
            on_health_issue=False,
            on_import_failure=True,
            on_release_import=False,
            on_rename=False,
            on_upgrade=True,
            path="/scripts/lidarr.sh")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:Notifications/customScript:CustomScript example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arguments: Arguments.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: NotificationCustomScript name.
        :param pulumi.Input[bool] on_album_delete: On album delete flag.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_artist_delete: On artist delete flag.
        :param pulumi.Input[bool] on_download_failure: On download failure flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[bool] on_import_failure: On import failure flag.
        :param pulumi.Input[bool] on_release_import: On release import flag.
        :param pulumi.Input[bool] on_rename: On rename flag.
        :param pulumi.Input[bool] on_track_retag: On track retag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[str] path: Path.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomScriptArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Notifications -->Notification Custom Script resource.
        For more information refer to [Notification](https://wiki.servarr.com/lidarr/settings#connect) and [Custom Script](https://wiki.servarr.com/lidarr/supported#customscript).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_lidarr as lidarr

        example = lidarr.notifications.CustomScript("example",
            include_health_warnings=False,
            on_application_update=False,
            on_download_failure=False,
            on_grab=False,
            on_health_issue=False,
            on_import_failure=True,
            on_release_import=False,
            on_rename=False,
            on_upgrade=True,
            path="/scripts/lidarr.sh")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import lidarr:Notifications/customScript:CustomScript example 1
        ```

        :param str resource_name: The name of the resource.
        :param CustomScriptArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomScriptArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arguments: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_album_delete: Optional[pulumi.Input[bool]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_artist_delete: Optional[pulumi.Input[bool]] = None,
                 on_download_failure: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 on_import_failure: Optional[pulumi.Input[bool]] = None,
                 on_release_import: Optional[pulumi.Input[bool]] = None,
                 on_rename: Optional[pulumi.Input[bool]] = None,
                 on_track_retag: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomScriptArgs.__new__(CustomScriptArgs)

            __props__.__dict__["arguments"] = arguments
            __props__.__dict__["include_health_warnings"] = include_health_warnings
            __props__.__dict__["name"] = name
            __props__.__dict__["on_album_delete"] = on_album_delete
            __props__.__dict__["on_application_update"] = on_application_update
            __props__.__dict__["on_artist_delete"] = on_artist_delete
            __props__.__dict__["on_download_failure"] = on_download_failure
            __props__.__dict__["on_grab"] = on_grab
            __props__.__dict__["on_health_issue"] = on_health_issue
            __props__.__dict__["on_health_restored"] = on_health_restored
            __props__.__dict__["on_import_failure"] = on_import_failure
            __props__.__dict__["on_release_import"] = on_release_import
            __props__.__dict__["on_rename"] = on_rename
            __props__.__dict__["on_track_retag"] = on_track_retag
            __props__.__dict__["on_upgrade"] = on_upgrade
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
            __props__.__dict__["tags"] = tags
        super(CustomScript, __self__).__init__(
            'lidarr:Notifications/customScript:CustomScript',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arguments: Optional[pulumi.Input[str]] = None,
            include_health_warnings: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            on_album_delete: Optional[pulumi.Input[bool]] = None,
            on_application_update: Optional[pulumi.Input[bool]] = None,
            on_artist_delete: Optional[pulumi.Input[bool]] = None,
            on_download_failure: Optional[pulumi.Input[bool]] = None,
            on_grab: Optional[pulumi.Input[bool]] = None,
            on_health_issue: Optional[pulumi.Input[bool]] = None,
            on_health_restored: Optional[pulumi.Input[bool]] = None,
            on_import_failure: Optional[pulumi.Input[bool]] = None,
            on_release_import: Optional[pulumi.Input[bool]] = None,
            on_rename: Optional[pulumi.Input[bool]] = None,
            on_track_retag: Optional[pulumi.Input[bool]] = None,
            on_upgrade: Optional[pulumi.Input[bool]] = None,
            path: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'CustomScript':
        """
        Get an existing CustomScript resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arguments: Arguments.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: NotificationCustomScript name.
        :param pulumi.Input[bool] on_album_delete: On album delete flag.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_artist_delete: On artist delete flag.
        :param pulumi.Input[bool] on_download_failure: On download failure flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[bool] on_import_failure: On import failure flag.
        :param pulumi.Input[bool] on_release_import: On release import flag.
        :param pulumi.Input[bool] on_rename: On rename flag.
        :param pulumi.Input[bool] on_track_retag: On track retag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[str] path: Path.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomScriptState.__new__(_CustomScriptState)

        __props__.__dict__["arguments"] = arguments
        __props__.__dict__["include_health_warnings"] = include_health_warnings
        __props__.__dict__["name"] = name
        __props__.__dict__["on_album_delete"] = on_album_delete
        __props__.__dict__["on_application_update"] = on_application_update
        __props__.__dict__["on_artist_delete"] = on_artist_delete
        __props__.__dict__["on_download_failure"] = on_download_failure
        __props__.__dict__["on_grab"] = on_grab
        __props__.__dict__["on_health_issue"] = on_health_issue
        __props__.__dict__["on_health_restored"] = on_health_restored
        __props__.__dict__["on_import_failure"] = on_import_failure
        __props__.__dict__["on_release_import"] = on_release_import
        __props__.__dict__["on_rename"] = on_rename
        __props__.__dict__["on_track_retag"] = on_track_retag
        __props__.__dict__["on_upgrade"] = on_upgrade
        __props__.__dict__["path"] = path
        __props__.__dict__["tags"] = tags
        return CustomScript(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arguments(self) -> pulumi.Output[str]:
        """
        Arguments.
        """
        return pulumi.get(self, "arguments")

    @property
    @pulumi.getter(name="includeHealthWarnings")
    def include_health_warnings(self) -> pulumi.Output[bool]:
        """
        Include health warnings.
        """
        return pulumi.get(self, "include_health_warnings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        NotificationCustomScript name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="onAlbumDelete")
    def on_album_delete(self) -> pulumi.Output[bool]:
        """
        On album delete flag.
        """
        return pulumi.get(self, "on_album_delete")

    @property
    @pulumi.getter(name="onApplicationUpdate")
    def on_application_update(self) -> pulumi.Output[bool]:
        """
        On application update flag.
        """
        return pulumi.get(self, "on_application_update")

    @property
    @pulumi.getter(name="onArtistDelete")
    def on_artist_delete(self) -> pulumi.Output[bool]:
        """
        On artist delete flag.
        """
        return pulumi.get(self, "on_artist_delete")

    @property
    @pulumi.getter(name="onDownloadFailure")
    def on_download_failure(self) -> pulumi.Output[bool]:
        """
        On download failure flag.
        """
        return pulumi.get(self, "on_download_failure")

    @property
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> pulumi.Output[bool]:
        """
        On grab flag.
        """
        return pulumi.get(self, "on_grab")

    @property
    @pulumi.getter(name="onHealthIssue")
    def on_health_issue(self) -> pulumi.Output[bool]:
        """
        On health issue flag.
        """
        return pulumi.get(self, "on_health_issue")

    @property
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> pulumi.Output[bool]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @property
    @pulumi.getter(name="onImportFailure")
    def on_import_failure(self) -> pulumi.Output[bool]:
        """
        On import failure flag.
        """
        return pulumi.get(self, "on_import_failure")

    @property
    @pulumi.getter(name="onReleaseImport")
    def on_release_import(self) -> pulumi.Output[bool]:
        """
        On release import flag.
        """
        return pulumi.get(self, "on_release_import")

    @property
    @pulumi.getter(name="onRename")
    def on_rename(self) -> pulumi.Output[bool]:
        """
        On rename flag.
        """
        return pulumi.get(self, "on_rename")

    @property
    @pulumi.getter(name="onTrackRetag")
    def on_track_retag(self) -> pulumi.Output[bool]:
        """
        On track retag.
        """
        return pulumi.get(self, "on_track_retag")

    @property
    @pulumi.getter(name="onUpgrade")
    def on_upgrade(self) -> pulumi.Output[bool]:
        """
        On upgrade flag.
        """
        return pulumi.get(self, "on_upgrade")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        Path.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

