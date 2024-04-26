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
    'GetSyncProfilesResult',
    'AwaitableGetSyncProfilesResult',
    'get_sync_profiles',
    'get_sync_profiles_output',
]

@pulumi.output_type
class GetSyncProfilesResult:
    """
    A collection of values returned by getSyncProfiles.
    """
    def __init__(__self__, id=None, sync_profiles=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if sync_profiles and not isinstance(sync_profiles, list):
            raise TypeError("Expected argument 'sync_profiles' to be a list")
        pulumi.set(__self__, "sync_profiles", sync_profiles)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="syncProfiles")
    def sync_profiles(self) -> Sequence['outputs.GetSyncProfilesSyncProfileResult']:
        """
        Sync Profile list.
        """
        return pulumi.get(self, "sync_profiles")


class AwaitableGetSyncProfilesResult(GetSyncProfilesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSyncProfilesResult(
            id=self.id,
            sync_profiles=self.sync_profiles)


def get_sync_profiles(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSyncProfilesResult:
    """
    <!-- subcategory:Applications -->List all available Sync Profiles.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    example = prowlarr.Applications.get_sync_profiles()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prowlarr:Applications/getSyncProfiles:getSyncProfiles', __args__, opts=opts, typ=GetSyncProfilesResult).value

    return AwaitableGetSyncProfilesResult(
        id=pulumi.get(__ret__, 'id'),
        sync_profiles=pulumi.get(__ret__, 'sync_profiles'))


@_utilities.lift_output_func(get_sync_profiles)
def get_sync_profiles_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSyncProfilesResult]:
    """
    <!-- subcategory:Applications -->List all available Sync Profiles.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    example = prowlarr.Applications.get_sync_profiles()
    ```
    """
    ...
