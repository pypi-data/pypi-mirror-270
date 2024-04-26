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
    'GetStatusResult',
    'AwaitableGetStatusResult',
    'get_status',
    'get_status_output',
]

@pulumi.output_type
class GetStatusResult:
    """
    A collection of values returned by getStatus.
    """
    def __init__(__self__, app_data=None, app_name=None, authentication=None, branch=None, build_time=None, database_type=None, database_version=None, id=None, instance_name=None, is_admin=None, is_debug=None, is_docker=None, is_linux=None, is_net_core=None, is_osx=None, is_production=None, is_user_interactive=None, is_windows=None, migration_version=None, mode=None, os_name=None, os_version=None, package_author=None, package_update_mechanism=None, package_update_mechanism_message=None, package_version=None, runtime_name=None, runtime_version=None, start_time=None, startup_path=None, url_base=None, version=None):
        if app_data and not isinstance(app_data, str):
            raise TypeError("Expected argument 'app_data' to be a str")
        pulumi.set(__self__, "app_data", app_data)
        if app_name and not isinstance(app_name, str):
            raise TypeError("Expected argument 'app_name' to be a str")
        pulumi.set(__self__, "app_name", app_name)
        if authentication and not isinstance(authentication, str):
            raise TypeError("Expected argument 'authentication' to be a str")
        pulumi.set(__self__, "authentication", authentication)
        if branch and not isinstance(branch, str):
            raise TypeError("Expected argument 'branch' to be a str")
        pulumi.set(__self__, "branch", branch)
        if build_time and not isinstance(build_time, str):
            raise TypeError("Expected argument 'build_time' to be a str")
        pulumi.set(__self__, "build_time", build_time)
        if database_type and not isinstance(database_type, str):
            raise TypeError("Expected argument 'database_type' to be a str")
        pulumi.set(__self__, "database_type", database_type)
        if database_version and not isinstance(database_version, str):
            raise TypeError("Expected argument 'database_version' to be a str")
        pulumi.set(__self__, "database_version", database_version)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if instance_name and not isinstance(instance_name, str):
            raise TypeError("Expected argument 'instance_name' to be a str")
        pulumi.set(__self__, "instance_name", instance_name)
        if is_admin and not isinstance(is_admin, bool):
            raise TypeError("Expected argument 'is_admin' to be a bool")
        pulumi.set(__self__, "is_admin", is_admin)
        if is_debug and not isinstance(is_debug, bool):
            raise TypeError("Expected argument 'is_debug' to be a bool")
        pulumi.set(__self__, "is_debug", is_debug)
        if is_docker and not isinstance(is_docker, bool):
            raise TypeError("Expected argument 'is_docker' to be a bool")
        pulumi.set(__self__, "is_docker", is_docker)
        if is_linux and not isinstance(is_linux, bool):
            raise TypeError("Expected argument 'is_linux' to be a bool")
        pulumi.set(__self__, "is_linux", is_linux)
        if is_net_core and not isinstance(is_net_core, bool):
            raise TypeError("Expected argument 'is_net_core' to be a bool")
        pulumi.set(__self__, "is_net_core", is_net_core)
        if is_osx and not isinstance(is_osx, bool):
            raise TypeError("Expected argument 'is_osx' to be a bool")
        pulumi.set(__self__, "is_osx", is_osx)
        if is_production and not isinstance(is_production, bool):
            raise TypeError("Expected argument 'is_production' to be a bool")
        pulumi.set(__self__, "is_production", is_production)
        if is_user_interactive and not isinstance(is_user_interactive, bool):
            raise TypeError("Expected argument 'is_user_interactive' to be a bool")
        pulumi.set(__self__, "is_user_interactive", is_user_interactive)
        if is_windows and not isinstance(is_windows, bool):
            raise TypeError("Expected argument 'is_windows' to be a bool")
        pulumi.set(__self__, "is_windows", is_windows)
        if migration_version and not isinstance(migration_version, int):
            raise TypeError("Expected argument 'migration_version' to be a int")
        pulumi.set(__self__, "migration_version", migration_version)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if os_name and not isinstance(os_name, str):
            raise TypeError("Expected argument 'os_name' to be a str")
        pulumi.set(__self__, "os_name", os_name)
        if os_version and not isinstance(os_version, str):
            raise TypeError("Expected argument 'os_version' to be a str")
        pulumi.set(__self__, "os_version", os_version)
        if package_author and not isinstance(package_author, str):
            raise TypeError("Expected argument 'package_author' to be a str")
        pulumi.set(__self__, "package_author", package_author)
        if package_update_mechanism and not isinstance(package_update_mechanism, str):
            raise TypeError("Expected argument 'package_update_mechanism' to be a str")
        pulumi.set(__self__, "package_update_mechanism", package_update_mechanism)
        if package_update_mechanism_message and not isinstance(package_update_mechanism_message, str):
            raise TypeError("Expected argument 'package_update_mechanism_message' to be a str")
        pulumi.set(__self__, "package_update_mechanism_message", package_update_mechanism_message)
        if package_version and not isinstance(package_version, str):
            raise TypeError("Expected argument 'package_version' to be a str")
        pulumi.set(__self__, "package_version", package_version)
        if runtime_name and not isinstance(runtime_name, str):
            raise TypeError("Expected argument 'runtime_name' to be a str")
        pulumi.set(__self__, "runtime_name", runtime_name)
        if runtime_version and not isinstance(runtime_version, str):
            raise TypeError("Expected argument 'runtime_version' to be a str")
        pulumi.set(__self__, "runtime_version", runtime_version)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if startup_path and not isinstance(startup_path, str):
            raise TypeError("Expected argument 'startup_path' to be a str")
        pulumi.set(__self__, "startup_path", startup_path)
        if url_base and not isinstance(url_base, str):
            raise TypeError("Expected argument 'url_base' to be a str")
        pulumi.set(__self__, "url_base", url_base)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="appData")
    def app_data(self) -> str:
        """
        App data folder.
        """
        return pulumi.get(self, "app_data")

    @property
    @pulumi.getter(name="appName")
    def app_name(self) -> str:
        """
        App name.
        """
        return pulumi.get(self, "app_name")

    @property
    @pulumi.getter
    def authentication(self) -> str:
        """
        Authentication.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter
    def branch(self) -> str:
        """
        Branch.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="buildTime")
    def build_time(self) -> str:
        """
        Build time.
        """
        return pulumi.get(self, "build_time")

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> str:
        """
        Database type.
        """
        return pulumi.get(self, "database_type")

    @property
    @pulumi.getter(name="databaseVersion")
    def database_version(self) -> str:
        """
        Database version.
        """
        return pulumi.get(self, "database_version")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Delay Profile ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> str:
        """
        Instance name.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="isAdmin")
    def is_admin(self) -> bool:
        """
        Is admin flag.
        """
        return pulumi.get(self, "is_admin")

    @property
    @pulumi.getter(name="isDebug")
    def is_debug(self) -> bool:
        """
        Is debug flag.
        """
        return pulumi.get(self, "is_debug")

    @property
    @pulumi.getter(name="isDocker")
    def is_docker(self) -> bool:
        """
        Is docker flag.
        """
        return pulumi.get(self, "is_docker")

    @property
    @pulumi.getter(name="isLinux")
    def is_linux(self) -> bool:
        """
        Is linux flag.
        """
        return pulumi.get(self, "is_linux")

    @property
    @pulumi.getter(name="isNetCore")
    def is_net_core(self) -> bool:
        """
        Is net core flag.
        """
        return pulumi.get(self, "is_net_core")

    @property
    @pulumi.getter(name="isOsx")
    def is_osx(self) -> bool:
        """
        Is osx flag.
        """
        return pulumi.get(self, "is_osx")

    @property
    @pulumi.getter(name="isProduction")
    def is_production(self) -> bool:
        """
        Is production flag.
        """
        return pulumi.get(self, "is_production")

    @property
    @pulumi.getter(name="isUserInteractive")
    def is_user_interactive(self) -> bool:
        """
        Is user interactive flag.
        """
        return pulumi.get(self, "is_user_interactive")

    @property
    @pulumi.getter(name="isWindows")
    def is_windows(self) -> bool:
        """
        Is windows flag.
        """
        return pulumi.get(self, "is_windows")

    @property
    @pulumi.getter(name="migrationVersion")
    def migration_version(self) -> int:
        """
        Migration version.
        """
        return pulumi.get(self, "migration_version")

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        Mode.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="osName")
    def os_name(self) -> str:
        """
        OS name.
        """
        return pulumi.get(self, "os_name")

    @property
    @pulumi.getter(name="osVersion")
    def os_version(self) -> str:
        """
        OS version.
        """
        return pulumi.get(self, "os_version")

    @property
    @pulumi.getter(name="packageAuthor")
    def package_author(self) -> str:
        """
        Package author.
        """
        return pulumi.get(self, "package_author")

    @property
    @pulumi.getter(name="packageUpdateMechanism")
    def package_update_mechanism(self) -> str:
        """
        Package update mechanism.
        """
        return pulumi.get(self, "package_update_mechanism")

    @property
    @pulumi.getter(name="packageUpdateMechanismMessage")
    def package_update_mechanism_message(self) -> str:
        """
        Package update mechanism message.
        """
        return pulumi.get(self, "package_update_mechanism_message")

    @property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> str:
        """
        Package version.
        """
        return pulumi.get(self, "package_version")

    @property
    @pulumi.getter(name="runtimeName")
    def runtime_name(self) -> str:
        """
        Runtime name.
        """
        return pulumi.get(self, "runtime_name")

    @property
    @pulumi.getter(name="runtimeVersion")
    def runtime_version(self) -> str:
        """
        Runtime version.
        """
        return pulumi.get(self, "runtime_version")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Start time.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="startupPath")
    def startup_path(self) -> str:
        """
        Startup path.
        """
        return pulumi.get(self, "startup_path")

    @property
    @pulumi.getter(name="urlBase")
    def url_base(self) -> str:
        """
        Base URL.
        """
        return pulumi.get(self, "url_base")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version.
        """
        return pulumi.get(self, "version")


class AwaitableGetStatusResult(GetStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStatusResult(
            app_data=self.app_data,
            app_name=self.app_name,
            authentication=self.authentication,
            branch=self.branch,
            build_time=self.build_time,
            database_type=self.database_type,
            database_version=self.database_version,
            id=self.id,
            instance_name=self.instance_name,
            is_admin=self.is_admin,
            is_debug=self.is_debug,
            is_docker=self.is_docker,
            is_linux=self.is_linux,
            is_net_core=self.is_net_core,
            is_osx=self.is_osx,
            is_production=self.is_production,
            is_user_interactive=self.is_user_interactive,
            is_windows=self.is_windows,
            migration_version=self.migration_version,
            mode=self.mode,
            os_name=self.os_name,
            os_version=self.os_version,
            package_author=self.package_author,
            package_update_mechanism=self.package_update_mechanism,
            package_update_mechanism_message=self.package_update_mechanism_message,
            package_version=self.package_version,
            runtime_name=self.runtime_name,
            runtime_version=self.runtime_version,
            start_time=self.start_time,
            startup_path=self.startup_path,
            url_base=self.url_base,
            version=self.version)


def get_status(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStatusResult:
    """
    <!-- subcategory:System -->System Status resource. User must have rights to read `config.xml`.
    For more information refer to [System Status](https://wiki.servarr.com/readarr/system#status) documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_readarr as readarr

    example = readarr.System.get_status()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('readarr:System/getStatus:getStatus', __args__, opts=opts, typ=GetStatusResult).value

    return AwaitableGetStatusResult(
        app_data=pulumi.get(__ret__, 'app_data'),
        app_name=pulumi.get(__ret__, 'app_name'),
        authentication=pulumi.get(__ret__, 'authentication'),
        branch=pulumi.get(__ret__, 'branch'),
        build_time=pulumi.get(__ret__, 'build_time'),
        database_type=pulumi.get(__ret__, 'database_type'),
        database_version=pulumi.get(__ret__, 'database_version'),
        id=pulumi.get(__ret__, 'id'),
        instance_name=pulumi.get(__ret__, 'instance_name'),
        is_admin=pulumi.get(__ret__, 'is_admin'),
        is_debug=pulumi.get(__ret__, 'is_debug'),
        is_docker=pulumi.get(__ret__, 'is_docker'),
        is_linux=pulumi.get(__ret__, 'is_linux'),
        is_net_core=pulumi.get(__ret__, 'is_net_core'),
        is_osx=pulumi.get(__ret__, 'is_osx'),
        is_production=pulumi.get(__ret__, 'is_production'),
        is_user_interactive=pulumi.get(__ret__, 'is_user_interactive'),
        is_windows=pulumi.get(__ret__, 'is_windows'),
        migration_version=pulumi.get(__ret__, 'migration_version'),
        mode=pulumi.get(__ret__, 'mode'),
        os_name=pulumi.get(__ret__, 'os_name'),
        os_version=pulumi.get(__ret__, 'os_version'),
        package_author=pulumi.get(__ret__, 'package_author'),
        package_update_mechanism=pulumi.get(__ret__, 'package_update_mechanism'),
        package_update_mechanism_message=pulumi.get(__ret__, 'package_update_mechanism_message'),
        package_version=pulumi.get(__ret__, 'package_version'),
        runtime_name=pulumi.get(__ret__, 'runtime_name'),
        runtime_version=pulumi.get(__ret__, 'runtime_version'),
        start_time=pulumi.get(__ret__, 'start_time'),
        startup_path=pulumi.get(__ret__, 'startup_path'),
        url_base=pulumi.get(__ret__, 'url_base'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_status)
def get_status_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStatusResult]:
    """
    <!-- subcategory:System -->System Status resource. User must have rights to read `config.xml`.
    For more information refer to [System Status](https://wiki.servarr.com/readarr/system#status) documentation.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_readarr as readarr

    example = readarr.System.get_status()
    ```
    """
    ...
