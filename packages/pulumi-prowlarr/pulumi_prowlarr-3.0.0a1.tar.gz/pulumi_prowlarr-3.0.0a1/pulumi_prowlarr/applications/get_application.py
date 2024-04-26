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
    'GetApplicationResult',
    'AwaitableGetApplicationResult',
    'get_application',
    'get_application_output',
]

@pulumi.output_type
class GetApplicationResult:
    """
    A collection of values returned by getApplication.
    """
    def __init__(__self__, anime_sync_categories=None, api_key=None, base_url=None, config_contract=None, id=None, implementation=None, name=None, prowlarr_url=None, sync_categories=None, sync_level=None, tags=None):
        if anime_sync_categories and not isinstance(anime_sync_categories, list):
            raise TypeError("Expected argument 'anime_sync_categories' to be a list")
        pulumi.set(__self__, "anime_sync_categories", anime_sync_categories)
        if api_key and not isinstance(api_key, str):
            raise TypeError("Expected argument 'api_key' to be a str")
        pulumi.set(__self__, "api_key", api_key)
        if base_url and not isinstance(base_url, str):
            raise TypeError("Expected argument 'base_url' to be a str")
        pulumi.set(__self__, "base_url", base_url)
        if config_contract and not isinstance(config_contract, str):
            raise TypeError("Expected argument 'config_contract' to be a str")
        pulumi.set(__self__, "config_contract", config_contract)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if implementation and not isinstance(implementation, str):
            raise TypeError("Expected argument 'implementation' to be a str")
        pulumi.set(__self__, "implementation", implementation)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if prowlarr_url and not isinstance(prowlarr_url, str):
            raise TypeError("Expected argument 'prowlarr_url' to be a str")
        pulumi.set(__self__, "prowlarr_url", prowlarr_url)
        if sync_categories and not isinstance(sync_categories, list):
            raise TypeError("Expected argument 'sync_categories' to be a list")
        pulumi.set(__self__, "sync_categories", sync_categories)
        if sync_level and not isinstance(sync_level, str):
            raise TypeError("Expected argument 'sync_level' to be a str")
        pulumi.set(__self__, "sync_level", sync_level)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="animeSyncCategories")
    def anime_sync_categories(self) -> Sequence[int]:
        """
        Anime sync categories.
        """
        return pulumi.get(self, "anime_sync_categories")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> str:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> str:
        """
        Base URL.
        """
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> str:
        """
        Application configuration template.
        """
        return pulumi.get(self, "config_contract")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Application ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def implementation(self) -> str:
        """
        Application implementation name.
        """
        return pulumi.get(self, "implementation")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Application name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="prowlarrUrl")
    def prowlarr_url(self) -> str:
        """
        Prowlarr URL.
        """
        return pulumi.get(self, "prowlarr_url")

    @property
    @pulumi.getter(name="syncCategories")
    def sync_categories(self) -> Sequence[int]:
        """
        Sync categories.
        """
        return pulumi.get(self, "sync_categories")

    @property
    @pulumi.getter(name="syncLevel")
    def sync_level(self) -> str:
        """
        Sync level.
        """
        return pulumi.get(self, "sync_level")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[int]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")


class AwaitableGetApplicationResult(GetApplicationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationResult(
            anime_sync_categories=self.anime_sync_categories,
            api_key=self.api_key,
            base_url=self.base_url,
            config_contract=self.config_contract,
            id=self.id,
            implementation=self.implementation,
            name=self.name,
            prowlarr_url=self.prowlarr_url,
            sync_categories=self.sync_categories,
            sync_level=self.sync_level,
            tags=self.tags)


def get_application(name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationResult:
    """
    <!-- subcategory:Applications -->Single Application.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    example = prowlarr.Applications.get_application(name="Example")
    ```


    :param str name: Application name.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prowlarr:Applications/getApplication:getApplication', __args__, opts=opts, typ=GetApplicationResult).value

    return AwaitableGetApplicationResult(
        anime_sync_categories=pulumi.get(__ret__, 'anime_sync_categories'),
        api_key=pulumi.get(__ret__, 'api_key'),
        base_url=pulumi.get(__ret__, 'base_url'),
        config_contract=pulumi.get(__ret__, 'config_contract'),
        id=pulumi.get(__ret__, 'id'),
        implementation=pulumi.get(__ret__, 'implementation'),
        name=pulumi.get(__ret__, 'name'),
        prowlarr_url=pulumi.get(__ret__, 'prowlarr_url'),
        sync_categories=pulumi.get(__ret__, 'sync_categories'),
        sync_level=pulumi.get(__ret__, 'sync_level'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_application)
def get_application_output(name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationResult]:
    """
    <!-- subcategory:Applications -->Single Application.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    example = prowlarr.Applications.get_application(name="Example")
    ```


    :param str name: Application name.
    """
    ...
