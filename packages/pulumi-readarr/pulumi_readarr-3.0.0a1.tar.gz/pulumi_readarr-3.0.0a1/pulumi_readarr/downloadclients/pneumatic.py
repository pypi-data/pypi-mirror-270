# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PneumaticArgs', 'Pneumatic']

@pulumi.input_type
class PneumaticArgs:
    def __init__(__self__, *,
                 nzb_folder: pulumi.Input[str],
                 strm_folder: pulumi.Input[str],
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Pneumatic resource.
        :param pulumi.Input[str] nzb_folder: NZB folder.
        :param pulumi.Input[str] strm_folder: STRM folder.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "nzb_folder", nzb_folder)
        pulumi.set(__self__, "strm_folder", strm_folder)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if remove_completed_downloads is not None:
            pulumi.set(__self__, "remove_completed_downloads", remove_completed_downloads)
        if remove_failed_downloads is not None:
            pulumi.set(__self__, "remove_failed_downloads", remove_failed_downloads)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="nzbFolder")
    def nzb_folder(self) -> pulumi.Input[str]:
        """
        NZB folder.
        """
        return pulumi.get(self, "nzb_folder")

    @nzb_folder.setter
    def nzb_folder(self, value: pulumi.Input[str]):
        pulumi.set(self, "nzb_folder", value)

    @property
    @pulumi.getter(name="strmFolder")
    def strm_folder(self) -> pulumi.Input[str]:
        """
        STRM folder.
        """
        return pulumi.get(self, "strm_folder")

    @strm_folder.setter
    def strm_folder(self, value: pulumi.Input[str]):
        pulumi.set(self, "strm_folder", value)

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
        Download Client name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @remove_completed_downloads.setter
    def remove_completed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_completed_downloads", value)

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @remove_failed_downloads.setter
    def remove_failed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_failed_downloads", value)

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
class _PneumaticState:
    def __init__(__self__, *,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nzb_folder: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 strm_folder: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Pneumatic resources.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[str] nzb_folder: NZB folder.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[str] strm_folder: STRM folder.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nzb_folder is not None:
            pulumi.set(__self__, "nzb_folder", nzb_folder)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if remove_completed_downloads is not None:
            pulumi.set(__self__, "remove_completed_downloads", remove_completed_downloads)
        if remove_failed_downloads is not None:
            pulumi.set(__self__, "remove_failed_downloads", remove_failed_downloads)
        if strm_folder is not None:
            pulumi.set(__self__, "strm_folder", strm_folder)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
        Download Client name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nzbFolder")
    def nzb_folder(self) -> Optional[pulumi.Input[str]]:
        """
        NZB folder.
        """
        return pulumi.get(self, "nzb_folder")

    @nzb_folder.setter
    def nzb_folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nzb_folder", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @remove_completed_downloads.setter
    def remove_completed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_completed_downloads", value)

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @remove_failed_downloads.setter
    def remove_failed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_failed_downloads", value)

    @property
    @pulumi.getter(name="strmFolder")
    def strm_folder(self) -> Optional[pulumi.Input[str]]:
        """
        STRM folder.
        """
        return pulumi.get(self, "strm_folder")

    @strm_folder.setter
    def strm_folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strm_folder", value)

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


class Pneumatic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nzb_folder: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 strm_folder: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Download Clients -->Download Client Pneumatic resource.
        For more information refer to [Download Client](https://wiki.servarr.com/readarr/settings#download-clients) and [Pneumatic](https://wiki.servarr.com/readarr/supported#pneumatic).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_readarr as readarr

        example = readarr.download_clients.Pneumatic("example",
            enable=True,
            nzb_folder="/nzb/",
            priority=1,
            strm_folder="/strm/")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import readarr:DownloadClients/pneumatic:Pneumatic example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[str] nzb_folder: NZB folder.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[str] strm_folder: STRM folder.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PneumaticArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Download Clients -->Download Client Pneumatic resource.
        For more information refer to [Download Client](https://wiki.servarr.com/readarr/settings#download-clients) and [Pneumatic](https://wiki.servarr.com/readarr/supported#pneumatic).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_readarr as readarr

        example = readarr.download_clients.Pneumatic("example",
            enable=True,
            nzb_folder="/nzb/",
            priority=1,
            strm_folder="/strm/")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import readarr:DownloadClients/pneumatic:Pneumatic example 1
        ```

        :param str resource_name: The name of the resource.
        :param PneumaticArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PneumaticArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nzb_folder: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 strm_folder: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PneumaticArgs.__new__(PneumaticArgs)

            __props__.__dict__["enable"] = enable
            __props__.__dict__["name"] = name
            if nzb_folder is None and not opts.urn:
                raise TypeError("Missing required property 'nzb_folder'")
            __props__.__dict__["nzb_folder"] = nzb_folder
            __props__.__dict__["priority"] = priority
            __props__.__dict__["remove_completed_downloads"] = remove_completed_downloads
            __props__.__dict__["remove_failed_downloads"] = remove_failed_downloads
            if strm_folder is None and not opts.urn:
                raise TypeError("Missing required property 'strm_folder'")
            __props__.__dict__["strm_folder"] = strm_folder
            __props__.__dict__["tags"] = tags
        super(Pneumatic, __self__).__init__(
            'readarr:DownloadClients/pneumatic:Pneumatic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nzb_folder: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
            remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
            strm_folder: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Pneumatic':
        """
        Get an existing Pneumatic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[str] nzb_folder: NZB folder.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[str] strm_folder: STRM folder.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PneumaticState.__new__(_PneumaticState)

        __props__.__dict__["enable"] = enable
        __props__.__dict__["name"] = name
        __props__.__dict__["nzb_folder"] = nzb_folder
        __props__.__dict__["priority"] = priority
        __props__.__dict__["remove_completed_downloads"] = remove_completed_downloads
        __props__.__dict__["remove_failed_downloads"] = remove_failed_downloads
        __props__.__dict__["strm_folder"] = strm_folder
        __props__.__dict__["tags"] = tags
        return Pneumatic(resource_name, opts=opts, __props__=__props__)

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
        Download Client name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nzbFolder")
    def nzb_folder(self) -> pulumi.Output[str]:
        """
        NZB folder.
        """
        return pulumi.get(self, "nzb_folder")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> pulumi.Output[bool]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> pulumi.Output[bool]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @property
    @pulumi.getter(name="strmFolder")
    def strm_folder(self) -> pulumi.Output[str]:
        """
        STRM folder.
        """
        return pulumi.get(self, "strm_folder")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

