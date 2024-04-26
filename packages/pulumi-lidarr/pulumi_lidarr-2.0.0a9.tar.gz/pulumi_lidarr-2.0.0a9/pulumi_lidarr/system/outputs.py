# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'HostAuthentication',
    'HostBackup',
    'HostLogging',
    'HostProxy',
    'HostSsl',
    'HostUpdate',
    'GetHostAuthenticationResult',
    'GetHostBackupResult',
    'GetHostLoggingResult',
    'GetHostProxyResult',
    'GetHostSslResult',
    'GetHostUpdateResult',
]

@pulumi.output_type
class HostAuthentication(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encryptedPassword":
            suggest = "encrypted_password"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostAuthentication. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostAuthentication.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostAuthentication.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 method: str,
                 encrypted_password: Optional[str] = None,
                 password: Optional[str] = None,
                 username: Optional[str] = None):
        """
        :param str method: Authentication method.
        :param str encrypted_password: Needed for validation.
        :param str password: Password.
        :param str username: Username.
        """
        pulumi.set(__self__, "method", method)
        if encrypted_password is not None:
            pulumi.set(__self__, "encrypted_password", encrypted_password)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def method(self) -> str:
        """
        Authentication method.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter(name="encryptedPassword")
    def encrypted_password(self) -> Optional[str]:
        """
        Needed for validation.
        """
        return pulumi.get(self, "encrypted_password")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        Password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        """
        Username.
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class HostBackup(dict):
    def __init__(__self__, *,
                 folder: str,
                 interval: int,
                 retention: int):
        """
        :param str folder: Backup folder.
        :param int interval: Backup interval.
        :param int retention: Backup retention.
        """
        pulumi.set(__self__, "folder", folder)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "retention", retention)

    @property
    @pulumi.getter
    def folder(self) -> str:
        """
        Backup folder.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        Backup interval.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter
    def retention(self) -> int:
        """
        Backup retention.
        """
        return pulumi.get(self, "retention")


@pulumi.output_type
class HostLogging(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "logLevel":
            suggest = "log_level"
        elif key == "analyticsEnabled":
            suggest = "analytics_enabled"
        elif key == "consoleLogLevel":
            suggest = "console_log_level"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostLogging. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostLogging.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostLogging.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 log_level: str,
                 analytics_enabled: Optional[bool] = None,
                 console_log_level: Optional[str] = None):
        """
        :param str log_level: Log level.
        :param bool analytics_enabled: Enable analytics flag.
        :param str console_log_level: Console log level.
        """
        pulumi.set(__self__, "log_level", log_level)
        if analytics_enabled is not None:
            pulumi.set(__self__, "analytics_enabled", analytics_enabled)
        if console_log_level is not None:
            pulumi.set(__self__, "console_log_level", console_log_level)

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> str:
        """
        Log level.
        """
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter(name="analyticsEnabled")
    def analytics_enabled(self) -> Optional[bool]:
        """
        Enable analytics flag.
        """
        return pulumi.get(self, "analytics_enabled")

    @property
    @pulumi.getter(name="consoleLogLevel")
    def console_log_level(self) -> Optional[str]:
        """
        Console log level.
        """
        return pulumi.get(self, "console_log_level")


@pulumi.output_type
class HostProxy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "bypassFilter":
            suggest = "bypass_filter"
        elif key == "bypassLocalAddresses":
            suggest = "bypass_local_addresses"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostProxy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostProxy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostProxy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: bool,
                 bypass_filter: Optional[str] = None,
                 bypass_local_addresses: Optional[bool] = None,
                 hostname: Optional[str] = None,
                 password: Optional[str] = None,
                 port: Optional[int] = None,
                 type: Optional[str] = None,
                 username: Optional[str] = None):
        """
        :param bool enabled: Enabled.
        :param str bypass_filter: Bypass filder.
        :param bool bypass_local_addresses: Bypass for local addresses flag.
        :param str hostname: Proxy hostname.
        :param str password: Proxy password.
        :param int port: Proxy port.
        :param str type: Proxy type.
        :param str username: Proxy username.
        """
        pulumi.set(__self__, "enabled", enabled)
        if bypass_filter is not None:
            pulumi.set(__self__, "bypass_filter", bypass_filter)
        if bypass_local_addresses is not None:
            pulumi.set(__self__, "bypass_local_addresses", bypass_local_addresses)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="bypassFilter")
    def bypass_filter(self) -> Optional[str]:
        """
        Bypass filder.
        """
        return pulumi.get(self, "bypass_filter")

    @property
    @pulumi.getter(name="bypassLocalAddresses")
    def bypass_local_addresses(self) -> Optional[bool]:
        """
        Bypass for local addresses flag.
        """
        return pulumi.get(self, "bypass_local_addresses")

    @property
    @pulumi.getter
    def hostname(self) -> Optional[str]:
        """
        Proxy hostname.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        Proxy password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        Proxy port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Proxy type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> Optional[str]:
        """
        Proxy username.
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class HostSsl(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "certificateValidation":
            suggest = "certificate_validation"
        elif key == "certPassword":
            suggest = "cert_password"
        elif key == "certPath":
            suggest = "cert_path"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostSsl. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostSsl.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostSsl.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 certificate_validation: str,
                 enabled: bool,
                 cert_password: Optional[str] = None,
                 cert_path: Optional[str] = None,
                 port: Optional[int] = None):
        """
        :param str certificate_validation: Certificate validation.
        :param bool enabled: Enabled.
        :param str cert_password: Certificate Password.
        :param str cert_path: Certificate path.
        :param int port: SSL port.
        """
        pulumi.set(__self__, "certificate_validation", certificate_validation)
        pulumi.set(__self__, "enabled", enabled)
        if cert_password is not None:
            pulumi.set(__self__, "cert_password", cert_password)
        if cert_path is not None:
            pulumi.set(__self__, "cert_path", cert_path)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter(name="certificateValidation")
    def certificate_validation(self) -> str:
        """
        Certificate validation.
        """
        return pulumi.get(self, "certificate_validation")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="certPassword")
    def cert_password(self) -> Optional[str]:
        """
        Certificate Password.
        """
        return pulumi.get(self, "cert_password")

    @property
    @pulumi.getter(name="certPath")
    def cert_path(self) -> Optional[str]:
        """
        Certificate path.
        """
        return pulumi.get(self, "cert_path")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        SSL port.
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class HostUpdate(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "scriptPath":
            suggest = "script_path"
        elif key == "updateAutomatically":
            suggest = "update_automatically"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostUpdate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostUpdate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostUpdate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 branch: str,
                 mechanism: str,
                 script_path: Optional[str] = None,
                 update_automatically: Optional[bool] = None):
        """
        :param str branch: Branch reference.
        :param str mechanism: Update mechanism.
        :param str script_path: Script path.
        :param bool update_automatically: Update automatically flag.
        """
        pulumi.set(__self__, "branch", branch)
        pulumi.set(__self__, "mechanism", mechanism)
        if script_path is not None:
            pulumi.set(__self__, "script_path", script_path)
        if update_automatically is not None:
            pulumi.set(__self__, "update_automatically", update_automatically)

    @property
    @pulumi.getter
    def branch(self) -> str:
        """
        Branch reference.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter
    def mechanism(self) -> str:
        """
        Update mechanism.
        """
        return pulumi.get(self, "mechanism")

    @property
    @pulumi.getter(name="scriptPath")
    def script_path(self) -> Optional[str]:
        """
        Script path.
        """
        return pulumi.get(self, "script_path")

    @property
    @pulumi.getter(name="updateAutomatically")
    def update_automatically(self) -> Optional[bool]:
        """
        Update automatically flag.
        """
        return pulumi.get(self, "update_automatically")


@pulumi.output_type
class GetHostAuthenticationResult(dict):
    def __init__(__self__, *,
                 encrypted_password: str,
                 method: str,
                 password: str,
                 username: str):
        """
        :param str encrypted_password: Needed for validation.
        :param str method: Authentication method.
        :param str password: Password.
        :param str username: Username.
        """
        pulumi.set(__self__, "encrypted_password", encrypted_password)
        pulumi.set(__self__, "method", method)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="encryptedPassword")
    def encrypted_password(self) -> str:
        """
        Needed for validation.
        """
        return pulumi.get(self, "encrypted_password")

    @property
    @pulumi.getter
    def method(self) -> str:
        """
        Authentication method.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Username.
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class GetHostBackupResult(dict):
    def __init__(__self__, *,
                 folder: str,
                 interval: int,
                 retention: int):
        """
        :param str folder: Backup folder.
        :param int interval: Backup interval.
        :param int retention: Backup retention.
        """
        pulumi.set(__self__, "folder", folder)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "retention", retention)

    @property
    @pulumi.getter
    def folder(self) -> str:
        """
        Backup folder.
        """
        return pulumi.get(self, "folder")

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        Backup interval.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter
    def retention(self) -> int:
        """
        Backup retention.
        """
        return pulumi.get(self, "retention")


@pulumi.output_type
class GetHostLoggingResult(dict):
    def __init__(__self__, *,
                 analytics_enabled: bool,
                 console_log_level: str,
                 log_level: str):
        """
        :param bool analytics_enabled: Enable analytics flag.
        :param str console_log_level: Console log level.
        :param str log_level: Log level.
        """
        pulumi.set(__self__, "analytics_enabled", analytics_enabled)
        pulumi.set(__self__, "console_log_level", console_log_level)
        pulumi.set(__self__, "log_level", log_level)

    @property
    @pulumi.getter(name="analyticsEnabled")
    def analytics_enabled(self) -> bool:
        """
        Enable analytics flag.
        """
        return pulumi.get(self, "analytics_enabled")

    @property
    @pulumi.getter(name="consoleLogLevel")
    def console_log_level(self) -> str:
        """
        Console log level.
        """
        return pulumi.get(self, "console_log_level")

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> str:
        """
        Log level.
        """
        return pulumi.get(self, "log_level")


@pulumi.output_type
class GetHostProxyResult(dict):
    def __init__(__self__, *,
                 bypass_filter: str,
                 bypass_local_addresses: bool,
                 enabled: bool,
                 hostname: str,
                 password: str,
                 port: int,
                 type: str,
                 username: str):
        """
        :param str bypass_filter: Bypass filder.
        :param bool bypass_local_addresses: Bypass for local addresses flag.
        :param bool enabled: Enabled.
        :param str hostname: Proxy hostname.
        :param str password: Proxy password.
        :param int port: Proxy port.
        :param str type: Proxy type.
        :param str username: Proxy username.
        """
        pulumi.set(__self__, "bypass_filter", bypass_filter)
        pulumi.set(__self__, "bypass_local_addresses", bypass_local_addresses)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "type", type)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="bypassFilter")
    def bypass_filter(self) -> str:
        """
        Bypass filder.
        """
        return pulumi.get(self, "bypass_filter")

    @property
    @pulumi.getter(name="bypassLocalAddresses")
    def bypass_local_addresses(self) -> bool:
        """
        Bypass for local addresses flag.
        """
        return pulumi.get(self, "bypass_local_addresses")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        Proxy hostname.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Proxy password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        Proxy port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Proxy type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Proxy username.
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class GetHostSslResult(dict):
    def __init__(__self__, *,
                 cert_password: str,
                 cert_path: str,
                 certificate_validation: str,
                 enabled: bool,
                 port: int):
        """
        :param str cert_password: Certificate Password.
        :param str cert_path: Certificate path.
        :param str certificate_validation: Certificate validation.
        :param bool enabled: Enabled.
        :param int port: SSL port.
        """
        pulumi.set(__self__, "cert_password", cert_password)
        pulumi.set(__self__, "cert_path", cert_path)
        pulumi.set(__self__, "certificate_validation", certificate_validation)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter(name="certPassword")
    def cert_password(self) -> str:
        """
        Certificate Password.
        """
        return pulumi.get(self, "cert_password")

    @property
    @pulumi.getter(name="certPath")
    def cert_path(self) -> str:
        """
        Certificate path.
        """
        return pulumi.get(self, "cert_path")

    @property
    @pulumi.getter(name="certificateValidation")
    def certificate_validation(self) -> str:
        """
        Certificate validation.
        """
        return pulumi.get(self, "certificate_validation")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        SSL port.
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class GetHostUpdateResult(dict):
    def __init__(__self__, *,
                 branch: str,
                 mechanism: str,
                 script_path: str,
                 update_automatically: bool):
        """
        :param str branch: Branch reference.
        :param str mechanism: Update mechanism.
        :param str script_path: Script path.
        :param bool update_automatically: Update automatically flag.
        """
        pulumi.set(__self__, "branch", branch)
        pulumi.set(__self__, "mechanism", mechanism)
        pulumi.set(__self__, "script_path", script_path)
        pulumi.set(__self__, "update_automatically", update_automatically)

    @property
    @pulumi.getter
    def branch(self) -> str:
        """
        Branch reference.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter
    def mechanism(self) -> str:
        """
        Update mechanism.
        """
        return pulumi.get(self, "mechanism")

    @property
    @pulumi.getter(name="scriptPath")
    def script_path(self) -> str:
        """
        Script path.
        """
        return pulumi.get(self, "script_path")

    @property
    @pulumi.getter(name="updateAutomatically")
    def update_automatically(self) -> bool:
        """
        Update automatically flag.
        """
        return pulumi.get(self, "update_automatically")


