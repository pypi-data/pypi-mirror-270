# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetDownloadClientsResult',
    'AwaitableGetDownloadClientsResult',
    'get_download_clients',
    'get_download_clients_output',
]

@pulumi.output_type
class GetDownloadClientsResult:
    """
    A collection of values returned by getDownloadClients.
    """
    def __init__(__self__, download_clients=None, id=None):
        if download_clients and not isinstance(download_clients, list):
            raise TypeError("Expected argument 'download_clients' to be a list")
        pulumi.set(__self__, "download_clients", download_clients)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="downloadClients")
    def download_clients(self) -> Sequence['outputs.GetDownloadClientsDownloadClientResult']:
        """
        Download Client list..
        """
        return pulumi.get(self, "download_clients")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetDownloadClientsResult(GetDownloadClientsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDownloadClientsResult(
            download_clients=self.download_clients,
            id=self.id)


def get_download_clients(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDownloadClientsResult:
    """
    <!-- subcategory:Download Clients -->List all available DownloadClients.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_readarr as readarr

    example = readarr.DownloadClients.get_download_clients()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('readarr:DownloadClients/getDownloadClients:getDownloadClients', __args__, opts=opts, typ=GetDownloadClientsResult).value

    return AwaitableGetDownloadClientsResult(
        download_clients=pulumi.get(__ret__, 'download_clients'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_download_clients)
def get_download_clients_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDownloadClientsResult]:
    """
    <!-- subcategory:Download Clients -->List all available DownloadClients.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_readarr as readarr

    example = readarr.DownloadClients.get_download_clients()
    ```
    """
    ...
