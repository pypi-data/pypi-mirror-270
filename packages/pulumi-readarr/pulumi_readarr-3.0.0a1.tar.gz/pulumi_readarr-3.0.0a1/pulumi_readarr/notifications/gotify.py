# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GotifyArgs', 'Gotify']

@pulumi.input_type
class GotifyArgs:
    def __init__(__self__, *,
                 app_token: pulumi.Input[str],
                 priority: pulumi.Input[int],
                 server: pulumi.Input[str],
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_author_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_file_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
                 on_download_failure: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_import_failure: Optional[pulumi.Input[bool]] = None,
                 on_release_import: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Gotify resource.
        :param pulumi.Input[str] app_token: App token.
        :param pulumi.Input[int] priority: Priority. `0` Min, `2` Low, `5` Normal, `8` High.
        :param pulumi.Input[str] server: Server.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: Notification name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_author_delete: On author deleted flag.
        :param pulumi.Input[bool] on_book_delete: On book delete flag.
        :param pulumi.Input[bool] on_book_file_delete: On book file delete flag.
        :param pulumi.Input[bool] on_book_file_delete_for_upgrade: On book file delete for upgrade flag.
        :param pulumi.Input[bool] on_download_failure: On download failure flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_import_failure: On import failure flag.
        :param pulumi.Input[bool] on_release_import: On release import flag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "app_token", app_token)
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "server", server)
        if include_health_warnings is not None:
            pulumi.set(__self__, "include_health_warnings", include_health_warnings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if on_application_update is not None:
            pulumi.set(__self__, "on_application_update", on_application_update)
        if on_author_delete is not None:
            pulumi.set(__self__, "on_author_delete", on_author_delete)
        if on_book_delete is not None:
            pulumi.set(__self__, "on_book_delete", on_book_delete)
        if on_book_file_delete is not None:
            pulumi.set(__self__, "on_book_file_delete", on_book_file_delete)
        if on_book_file_delete_for_upgrade is not None:
            pulumi.set(__self__, "on_book_file_delete_for_upgrade", on_book_file_delete_for_upgrade)
        if on_download_failure is not None:
            pulumi.set(__self__, "on_download_failure", on_download_failure)
        if on_grab is not None:
            pulumi.set(__self__, "on_grab", on_grab)
        if on_health_issue is not None:
            pulumi.set(__self__, "on_health_issue", on_health_issue)
        if on_import_failure is not None:
            pulumi.set(__self__, "on_import_failure", on_import_failure)
        if on_release_import is not None:
            pulumi.set(__self__, "on_release_import", on_release_import)
        if on_upgrade is not None:
            pulumi.set(__self__, "on_upgrade", on_upgrade)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appToken")
    def app_token(self) -> pulumi.Input[str]:
        """
        App token.
        """
        return pulumi.get(self, "app_token")

    @app_token.setter
    def app_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_token", value)

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Input[int]:
        """
        Priority. `0` Min, `2` Low, `5` Normal, `8` High.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: pulumi.Input[int]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def server(self) -> pulumi.Input[str]:
        """
        Server.
        """
        return pulumi.get(self, "server")

    @server.setter
    def server(self, value: pulumi.Input[str]):
        pulumi.set(self, "server", value)

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
        Notification name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="onAuthorDelete")
    def on_author_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On author deleted flag.
        """
        return pulumi.get(self, "on_author_delete")

    @on_author_delete.setter
    def on_author_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_author_delete", value)

    @property
    @pulumi.getter(name="onBookDelete")
    def on_book_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On book delete flag.
        """
        return pulumi.get(self, "on_book_delete")

    @on_book_delete.setter
    def on_book_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_book_delete", value)

    @property
    @pulumi.getter(name="onBookFileDelete")
    def on_book_file_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On book file delete flag.
        """
        return pulumi.get(self, "on_book_file_delete")

    @on_book_file_delete.setter
    def on_book_file_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_book_file_delete", value)

    @property
    @pulumi.getter(name="onBookFileDeleteForUpgrade")
    def on_book_file_delete_for_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        On book file delete for upgrade flag.
        """
        return pulumi.get(self, "on_book_file_delete_for_upgrade")

    @on_book_file_delete_for_upgrade.setter
    def on_book_file_delete_for_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_book_file_delete_for_upgrade", value)

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
class _GotifyState:
    def __init__(__self__, *,
                 app_token: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_author_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_file_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
                 on_download_failure: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_import_failure: Optional[pulumi.Input[bool]] = None,
                 on_release_import: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Gotify resources.
        :param pulumi.Input[str] app_token: App token.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: Notification name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_author_delete: On author deleted flag.
        :param pulumi.Input[bool] on_book_delete: On book delete flag.
        :param pulumi.Input[bool] on_book_file_delete: On book file delete flag.
        :param pulumi.Input[bool] on_book_file_delete_for_upgrade: On book file delete for upgrade flag.
        :param pulumi.Input[bool] on_download_failure: On download failure flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_import_failure: On import failure flag.
        :param pulumi.Input[bool] on_release_import: On release import flag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[int] priority: Priority. `0` Min, `2` Low, `5` Normal, `8` High.
        :param pulumi.Input[str] server: Server.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if app_token is not None:
            pulumi.set(__self__, "app_token", app_token)
        if include_health_warnings is not None:
            pulumi.set(__self__, "include_health_warnings", include_health_warnings)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if on_application_update is not None:
            pulumi.set(__self__, "on_application_update", on_application_update)
        if on_author_delete is not None:
            pulumi.set(__self__, "on_author_delete", on_author_delete)
        if on_book_delete is not None:
            pulumi.set(__self__, "on_book_delete", on_book_delete)
        if on_book_file_delete is not None:
            pulumi.set(__self__, "on_book_file_delete", on_book_file_delete)
        if on_book_file_delete_for_upgrade is not None:
            pulumi.set(__self__, "on_book_file_delete_for_upgrade", on_book_file_delete_for_upgrade)
        if on_download_failure is not None:
            pulumi.set(__self__, "on_download_failure", on_download_failure)
        if on_grab is not None:
            pulumi.set(__self__, "on_grab", on_grab)
        if on_health_issue is not None:
            pulumi.set(__self__, "on_health_issue", on_health_issue)
        if on_import_failure is not None:
            pulumi.set(__self__, "on_import_failure", on_import_failure)
        if on_release_import is not None:
            pulumi.set(__self__, "on_release_import", on_release_import)
        if on_upgrade is not None:
            pulumi.set(__self__, "on_upgrade", on_upgrade)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if server is not None:
            pulumi.set(__self__, "server", server)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appToken")
    def app_token(self) -> Optional[pulumi.Input[str]]:
        """
        App token.
        """
        return pulumi.get(self, "app_token")

    @app_token.setter
    def app_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_token", value)

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
        Notification name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="onAuthorDelete")
    def on_author_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On author deleted flag.
        """
        return pulumi.get(self, "on_author_delete")

    @on_author_delete.setter
    def on_author_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_author_delete", value)

    @property
    @pulumi.getter(name="onBookDelete")
    def on_book_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On book delete flag.
        """
        return pulumi.get(self, "on_book_delete")

    @on_book_delete.setter
    def on_book_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_book_delete", value)

    @property
    @pulumi.getter(name="onBookFileDelete")
    def on_book_file_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        On book file delete flag.
        """
        return pulumi.get(self, "on_book_file_delete")

    @on_book_file_delete.setter
    def on_book_file_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_book_file_delete", value)

    @property
    @pulumi.getter(name="onBookFileDeleteForUpgrade")
    def on_book_file_delete_for_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        On book file delete for upgrade flag.
        """
        return pulumi.get(self, "on_book_file_delete_for_upgrade")

    @on_book_file_delete_for_upgrade.setter
    def on_book_file_delete_for_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_book_file_delete_for_upgrade", value)

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
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority. `0` Min, `2` Low, `5` Normal, `8` High.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[str]]:
        """
        Server.
        """
        return pulumi.get(self, "server")

    @server.setter
    def server(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server", value)

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


class Gotify(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_token: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_author_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_file_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
                 on_download_failure: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_import_failure: Optional[pulumi.Input[bool]] = None,
                 on_release_import: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Notifications -->Notification Gotify resource.
        For more information refer to [Notification](https://wiki.servarr.com/readarr/settings#connect) and [Gotify](https://wiki.servarr.com/readarr/supported#gotify).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_readarr as readarr

        example = readarr.notifications.Gotify("example",
            app_token="Token",
            include_health_warnings=False,
            on_author_delete=False,
            on_book_delete=False,
            on_book_file_delete=False,
            on_book_file_delete_for_upgrade=False,
            on_download_failure=False,
            on_grab=False,
            on_health_issue=False,
            on_import_failure=False,
            on_release_import=False,
            on_upgrade=False,
            priority=5,
            server="http://gotify-server.net")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import readarr:Notifications/gotify:Gotify example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_token: App token.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: Notification name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_author_delete: On author deleted flag.
        :param pulumi.Input[bool] on_book_delete: On book delete flag.
        :param pulumi.Input[bool] on_book_file_delete: On book file delete flag.
        :param pulumi.Input[bool] on_book_file_delete_for_upgrade: On book file delete for upgrade flag.
        :param pulumi.Input[bool] on_download_failure: On download failure flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_import_failure: On import failure flag.
        :param pulumi.Input[bool] on_release_import: On release import flag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[int] priority: Priority. `0` Min, `2` Low, `5` Normal, `8` High.
        :param pulumi.Input[str] server: Server.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GotifyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Notifications -->Notification Gotify resource.
        For more information refer to [Notification](https://wiki.servarr.com/readarr/settings#connect) and [Gotify](https://wiki.servarr.com/readarr/supported#gotify).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_readarr as readarr

        example = readarr.notifications.Gotify("example",
            app_token="Token",
            include_health_warnings=False,
            on_author_delete=False,
            on_book_delete=False,
            on_book_file_delete=False,
            on_book_file_delete_for_upgrade=False,
            on_download_failure=False,
            on_grab=False,
            on_health_issue=False,
            on_import_failure=False,
            on_release_import=False,
            on_upgrade=False,
            priority=5,
            server="http://gotify-server.net")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import readarr:Notifications/gotify:Gotify example 1
        ```

        :param str resource_name: The name of the resource.
        :param GotifyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GotifyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_token: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_author_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_file_delete: Optional[pulumi.Input[bool]] = None,
                 on_book_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
                 on_download_failure: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_import_failure: Optional[pulumi.Input[bool]] = None,
                 on_release_import: Optional[pulumi.Input[bool]] = None,
                 on_upgrade: Optional[pulumi.Input[bool]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GotifyArgs.__new__(GotifyArgs)

            if app_token is None and not opts.urn:
                raise TypeError("Missing required property 'app_token'")
            __props__.__dict__["app_token"] = None if app_token is None else pulumi.Output.secret(app_token)
            __props__.__dict__["include_health_warnings"] = include_health_warnings
            __props__.__dict__["name"] = name
            __props__.__dict__["on_application_update"] = on_application_update
            __props__.__dict__["on_author_delete"] = on_author_delete
            __props__.__dict__["on_book_delete"] = on_book_delete
            __props__.__dict__["on_book_file_delete"] = on_book_file_delete
            __props__.__dict__["on_book_file_delete_for_upgrade"] = on_book_file_delete_for_upgrade
            __props__.__dict__["on_download_failure"] = on_download_failure
            __props__.__dict__["on_grab"] = on_grab
            __props__.__dict__["on_health_issue"] = on_health_issue
            __props__.__dict__["on_import_failure"] = on_import_failure
            __props__.__dict__["on_release_import"] = on_release_import
            __props__.__dict__["on_upgrade"] = on_upgrade
            if priority is None and not opts.urn:
                raise TypeError("Missing required property 'priority'")
            __props__.__dict__["priority"] = priority
            if server is None and not opts.urn:
                raise TypeError("Missing required property 'server'")
            __props__.__dict__["server"] = server
            __props__.__dict__["tags"] = tags
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["appToken"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Gotify, __self__).__init__(
            'readarr:Notifications/gotify:Gotify',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_token: Optional[pulumi.Input[str]] = None,
            include_health_warnings: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            on_application_update: Optional[pulumi.Input[bool]] = None,
            on_author_delete: Optional[pulumi.Input[bool]] = None,
            on_book_delete: Optional[pulumi.Input[bool]] = None,
            on_book_file_delete: Optional[pulumi.Input[bool]] = None,
            on_book_file_delete_for_upgrade: Optional[pulumi.Input[bool]] = None,
            on_download_failure: Optional[pulumi.Input[bool]] = None,
            on_grab: Optional[pulumi.Input[bool]] = None,
            on_health_issue: Optional[pulumi.Input[bool]] = None,
            on_import_failure: Optional[pulumi.Input[bool]] = None,
            on_release_import: Optional[pulumi.Input[bool]] = None,
            on_upgrade: Optional[pulumi.Input[bool]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            server: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Gotify':
        """
        Get an existing Gotify resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_token: App token.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[str] name: Notification name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_author_delete: On author deleted flag.
        :param pulumi.Input[bool] on_book_delete: On book delete flag.
        :param pulumi.Input[bool] on_book_file_delete: On book file delete flag.
        :param pulumi.Input[bool] on_book_file_delete_for_upgrade: On book file delete for upgrade flag.
        :param pulumi.Input[bool] on_download_failure: On download failure flag.
        :param pulumi.Input[bool] on_grab: On grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_import_failure: On import failure flag.
        :param pulumi.Input[bool] on_release_import: On release import flag.
        :param pulumi.Input[bool] on_upgrade: On upgrade flag.
        :param pulumi.Input[int] priority: Priority. `0` Min, `2` Low, `5` Normal, `8` High.
        :param pulumi.Input[str] server: Server.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GotifyState.__new__(_GotifyState)

        __props__.__dict__["app_token"] = app_token
        __props__.__dict__["include_health_warnings"] = include_health_warnings
        __props__.__dict__["name"] = name
        __props__.__dict__["on_application_update"] = on_application_update
        __props__.__dict__["on_author_delete"] = on_author_delete
        __props__.__dict__["on_book_delete"] = on_book_delete
        __props__.__dict__["on_book_file_delete"] = on_book_file_delete
        __props__.__dict__["on_book_file_delete_for_upgrade"] = on_book_file_delete_for_upgrade
        __props__.__dict__["on_download_failure"] = on_download_failure
        __props__.__dict__["on_grab"] = on_grab
        __props__.__dict__["on_health_issue"] = on_health_issue
        __props__.__dict__["on_import_failure"] = on_import_failure
        __props__.__dict__["on_release_import"] = on_release_import
        __props__.__dict__["on_upgrade"] = on_upgrade
        __props__.__dict__["priority"] = priority
        __props__.__dict__["server"] = server
        __props__.__dict__["tags"] = tags
        return Gotify(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appToken")
    def app_token(self) -> pulumi.Output[str]:
        """
        App token.
        """
        return pulumi.get(self, "app_token")

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
        Notification name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="onApplicationUpdate")
    def on_application_update(self) -> pulumi.Output[bool]:
        """
        On application update flag.
        """
        return pulumi.get(self, "on_application_update")

    @property
    @pulumi.getter(name="onAuthorDelete")
    def on_author_delete(self) -> pulumi.Output[bool]:
        """
        On author deleted flag.
        """
        return pulumi.get(self, "on_author_delete")

    @property
    @pulumi.getter(name="onBookDelete")
    def on_book_delete(self) -> pulumi.Output[bool]:
        """
        On book delete flag.
        """
        return pulumi.get(self, "on_book_delete")

    @property
    @pulumi.getter(name="onBookFileDelete")
    def on_book_file_delete(self) -> pulumi.Output[bool]:
        """
        On book file delete flag.
        """
        return pulumi.get(self, "on_book_file_delete")

    @property
    @pulumi.getter(name="onBookFileDeleteForUpgrade")
    def on_book_file_delete_for_upgrade(self) -> pulumi.Output[bool]:
        """
        On book file delete for upgrade flag.
        """
        return pulumi.get(self, "on_book_file_delete_for_upgrade")

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
    @pulumi.getter(name="onUpgrade")
    def on_upgrade(self) -> pulumi.Output[bool]:
        """
        On upgrade flag.
        """
        return pulumi.get(self, "on_upgrade")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Priority. `0` Min, `2` Low, `5` Normal, `8` High.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def server(self) -> pulumi.Output[str]:
        """
        Server.
        """
        return pulumi.get(self, "server")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

