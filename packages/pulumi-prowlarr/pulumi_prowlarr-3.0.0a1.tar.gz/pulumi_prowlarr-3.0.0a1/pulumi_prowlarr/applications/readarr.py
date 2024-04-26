# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ReadarrArgs', 'Readarr']

@pulumi.input_type
class ReadarrArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str],
                 base_url: pulumi.Input[str],
                 prowlarr_url: pulumi.Input[str],
                 sync_level: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 sync_categories: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Readarr resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[str] prowlarr_url: Prowlarr URL.
        :param pulumi.Input[str] sync_level: Sync level.
        :param pulumi.Input[str] name: Application name.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] sync_categories: Sync categories.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "api_key", api_key)
        pulumi.set(__self__, "base_url", base_url)
        pulumi.set(__self__, "prowlarr_url", prowlarr_url)
        pulumi.set(__self__, "sync_level", sync_level)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sync_categories is not None:
            pulumi.set(__self__, "sync_categories", sync_categories)
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
    @pulumi.getter(name="prowlarrUrl")
    def prowlarr_url(self) -> pulumi.Input[str]:
        """
        Prowlarr URL.
        """
        return pulumi.get(self, "prowlarr_url")

    @prowlarr_url.setter
    def prowlarr_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "prowlarr_url", value)

    @property
    @pulumi.getter(name="syncLevel")
    def sync_level(self) -> pulumi.Input[str]:
        """
        Sync level.
        """
        return pulumi.get(self, "sync_level")

    @sync_level.setter
    def sync_level(self, value: pulumi.Input[str]):
        pulumi.set(self, "sync_level", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Application name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="syncCategories")
    def sync_categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Sync categories.
        """
        return pulumi.get(self, "sync_categories")

    @sync_categories.setter
    def sync_categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "sync_categories", value)

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
class _ReadarrState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prowlarr_url: Optional[pulumi.Input[str]] = None,
                 sync_categories: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 sync_level: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Readarr resources.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[str] name: Application name.
        :param pulumi.Input[str] prowlarr_url: Prowlarr URL.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] sync_categories: Sync categories.
        :param pulumi.Input[str] sync_level: Sync level.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if base_url is not None:
            pulumi.set(__self__, "base_url", base_url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if prowlarr_url is not None:
            pulumi.set(__self__, "prowlarr_url", prowlarr_url)
        if sync_categories is not None:
            pulumi.set(__self__, "sync_categories", sync_categories)
        if sync_level is not None:
            pulumi.set(__self__, "sync_level", sync_level)
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
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Application name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="prowlarrUrl")
    def prowlarr_url(self) -> Optional[pulumi.Input[str]]:
        """
        Prowlarr URL.
        """
        return pulumi.get(self, "prowlarr_url")

    @prowlarr_url.setter
    def prowlarr_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prowlarr_url", value)

    @property
    @pulumi.getter(name="syncCategories")
    def sync_categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        Sync categories.
        """
        return pulumi.get(self, "sync_categories")

    @sync_categories.setter
    def sync_categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "sync_categories", value)

    @property
    @pulumi.getter(name="syncLevel")
    def sync_level(self) -> Optional[pulumi.Input[str]]:
        """
        Sync level.
        """
        return pulumi.get(self, "sync_level")

    @sync_level.setter
    def sync_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_level", value)

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


class Readarr(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prowlarr_url: Optional[pulumi.Input[str]] = None,
                 sync_categories: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 sync_level: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Applications -->Application Readarr resource.
        For more information refer to [Application](https://wiki.servarr.com/prowlarr/settings#applications) and [Readarr](https://wiki.servarr.com/prowlarr/supported#readarr).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_prowlarr as prowlarr

        example = prowlarr.applications.Readarr("example",
            api_key="APIKey",
            base_url="http://localhost:8787",
            prowlarr_url="http://localhost:9696",
            sync_categories=[
                7000,
                7010,
                7030,
            ],
            sync_level="addOnly")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:Applications/readarr:Readarr example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[str] name: Application name.
        :param pulumi.Input[str] prowlarr_url: Prowlarr URL.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] sync_categories: Sync categories.
        :param pulumi.Input[str] sync_level: Sync level.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReadarrArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Applications -->Application Readarr resource.
        For more information refer to [Application](https://wiki.servarr.com/prowlarr/settings#applications) and [Readarr](https://wiki.servarr.com/prowlarr/supported#readarr).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_prowlarr as prowlarr

        example = prowlarr.applications.Readarr("example",
            api_key="APIKey",
            base_url="http://localhost:8787",
            prowlarr_url="http://localhost:9696",
            sync_categories=[
                7000,
                7010,
                7030,
            ],
            sync_level="addOnly")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:Applications/readarr:Readarr example 1
        ```

        :param str resource_name: The name of the resource.
        :param ReadarrArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReadarrArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 prowlarr_url: Optional[pulumi.Input[str]] = None,
                 sync_categories: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 sync_level: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReadarrArgs.__new__(ReadarrArgs)

            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            if base_url is None and not opts.urn:
                raise TypeError("Missing required property 'base_url'")
            __props__.__dict__["base_url"] = base_url
            __props__.__dict__["name"] = name
            if prowlarr_url is None and not opts.urn:
                raise TypeError("Missing required property 'prowlarr_url'")
            __props__.__dict__["prowlarr_url"] = prowlarr_url
            __props__.__dict__["sync_categories"] = sync_categories
            if sync_level is None and not opts.urn:
                raise TypeError("Missing required property 'sync_level'")
            __props__.__dict__["sync_level"] = sync_level
            __props__.__dict__["tags"] = tags
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Readarr, __self__).__init__(
            'prowlarr:Applications/readarr:Readarr',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            base_url: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            prowlarr_url: Optional[pulumi.Input[str]] = None,
            sync_categories: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            sync_level: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Readarr':
        """
        Get an existing Readarr resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[str] base_url: Base URL.
        :param pulumi.Input[str] name: Application name.
        :param pulumi.Input[str] prowlarr_url: Prowlarr URL.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] sync_categories: Sync categories.
        :param pulumi.Input[str] sync_level: Sync level.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ReadarrState.__new__(_ReadarrState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["base_url"] = base_url
        __props__.__dict__["name"] = name
        __props__.__dict__["prowlarr_url"] = prowlarr_url
        __props__.__dict__["sync_categories"] = sync_categories
        __props__.__dict__["sync_level"] = sync_level
        __props__.__dict__["tags"] = tags
        return Readarr(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Application name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="prowlarrUrl")
    def prowlarr_url(self) -> pulumi.Output[str]:
        """
        Prowlarr URL.
        """
        return pulumi.get(self, "prowlarr_url")

    @property
    @pulumi.getter(name="syncCategories")
    def sync_categories(self) -> pulumi.Output[Sequence[int]]:
        """
        Sync categories.
        """
        return pulumi.get(self, "sync_categories")

    @property
    @pulumi.getter(name="syncLevel")
    def sync_level(self) -> pulumi.Output[str]:
        """
        Sync level.
        """
        return pulumi.get(self, "sync_level")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

