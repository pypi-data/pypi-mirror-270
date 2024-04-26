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
from ._inputs import *

__all__ = ['FreeboxArgs', 'Freebox']

@pulumi.input_type
class FreeboxArgs:
    def __init__(__self__, *,
                 api_url: pulumi.Input[str],
                 app_id: pulumi.Input[str],
                 app_token: pulumi.Input[str],
                 host: pulumi.Input[str],
                 port: pulumi.Input[int],
                 add_paused: Optional[pulumi.Input[bool]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 destination_directory: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 item_priority: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Freebox resource.
        :param pulumi.Input[str] api_url: API URL.
        :param pulumi.Input[str] app_id: App ID.
        :param pulumi.Input[str] app_token: App Token.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[bool] add_paused: Add paused flag.
        :param pulumi.Input[str] category: category.
        :param pulumi.Input[str] destination_directory: Movie directory.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[int] item_priority: Recent Movie priority. `0` Last, `1` First.
        :param pulumi.Input[str] name: Name of client category.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        """
        pulumi.set(__self__, "api_url", api_url)
        pulumi.set(__self__, "app_id", app_id)
        pulumi.set(__self__, "app_token", app_token)
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "port", port)
        if add_paused is not None:
            pulumi.set(__self__, "add_paused", add_paused)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if destination_directory is not None:
            pulumi.set(__self__, "destination_directory", destination_directory)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if item_priority is not None:
            pulumi.set(__self__, "item_priority", item_priority)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if use_ssl is not None:
            pulumi.set(__self__, "use_ssl", use_ssl)

    @property
    @pulumi.getter(name="apiUrl")
    def api_url(self) -> pulumi.Input[str]:
        """
        API URL.
        """
        return pulumi.get(self, "api_url")

    @api_url.setter
    def api_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_url", value)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        """
        App ID.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="appToken")
    def app_token(self) -> pulumi.Input[str]:
        """
        App Token.
        """
        return pulumi.get(self, "app_token")

    @app_token.setter
    def app_token(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_token", value)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        """
        host.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="addPaused")
    def add_paused(self) -> Optional[pulumi.Input[bool]]:
        """
        Add paused flag.
        """
        return pulumi.get(self, "add_paused")

    @add_paused.setter
    def add_paused(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "add_paused", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        category.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="destinationDirectory")
    def destination_directory(self) -> Optional[pulumi.Input[str]]:
        """
        Movie directory.
        """
        return pulumi.get(self, "destination_directory")

    @destination_directory.setter
    def destination_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_directory", value)

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
    @pulumi.getter(name="itemPriority")
    def item_priority(self) -> Optional[pulumi.Input[int]]:
        """
        Recent Movie priority. `0` Last, `1` First.
        """
        return pulumi.get(self, "item_priority")

    @item_priority.setter
    def item_priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "item_priority", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of client category.
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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[pulumi.Input[bool]]:
        """
        Use SSL flag.
        """
        return pulumi.get(self, "use_ssl")

    @use_ssl.setter
    def use_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_ssl", value)


@pulumi.input_type
class _FreeboxState:
    def __init__(__self__, *,
                 add_paused: Optional[pulumi.Input[bool]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 app_token: Optional[pulumi.Input[str]] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input['FreeboxCategoryArgs']]]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 destination_directory: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 item_priority: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Freebox resources.
        :param pulumi.Input[bool] add_paused: Add paused flag.
        :param pulumi.Input[str] api_url: API URL.
        :param pulumi.Input[str] app_id: App ID.
        :param pulumi.Input[str] app_token: App Token.
        :param pulumi.Input[Sequence[pulumi.Input['FreeboxCategoryArgs']]] categories: List of categories.
        :param pulumi.Input[str] category: category.
        :param pulumi.Input[str] destination_directory: Movie directory.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[int] item_priority: Recent Movie priority. `0` Last, `1` First.
        :param pulumi.Input[str] name: Name of client category.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        """
        if add_paused is not None:
            pulumi.set(__self__, "add_paused", add_paused)
        if api_url is not None:
            pulumi.set(__self__, "api_url", api_url)
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if app_token is not None:
            pulumi.set(__self__, "app_token", app_token)
        if categories is not None:
            pulumi.set(__self__, "categories", categories)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if destination_directory is not None:
            pulumi.set(__self__, "destination_directory", destination_directory)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if item_priority is not None:
            pulumi.set(__self__, "item_priority", item_priority)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if use_ssl is not None:
            pulumi.set(__self__, "use_ssl", use_ssl)

    @property
    @pulumi.getter(name="addPaused")
    def add_paused(self) -> Optional[pulumi.Input[bool]]:
        """
        Add paused flag.
        """
        return pulumi.get(self, "add_paused")

    @add_paused.setter
    def add_paused(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "add_paused", value)

    @property
    @pulumi.getter(name="apiUrl")
    def api_url(self) -> Optional[pulumi.Input[str]]:
        """
        API URL.
        """
        return pulumi.get(self, "api_url")

    @api_url.setter
    def api_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_url", value)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        App ID.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="appToken")
    def app_token(self) -> Optional[pulumi.Input[str]]:
        """
        App Token.
        """
        return pulumi.get(self, "app_token")

    @app_token.setter
    def app_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_token", value)

    @property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FreeboxCategoryArgs']]]]:
        """
        List of categories.
        """
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FreeboxCategoryArgs']]]]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        category.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="destinationDirectory")
    def destination_directory(self) -> Optional[pulumi.Input[str]]:
        """
        Movie directory.
        """
        return pulumi.get(self, "destination_directory")

    @destination_directory.setter
    def destination_directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_directory", value)

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
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        host.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter(name="itemPriority")
    def item_priority(self) -> Optional[pulumi.Input[int]]:
        """
        Recent Movie priority. `0` Last, `1` First.
        """
        return pulumi.get(self, "item_priority")

    @item_priority.setter
    def item_priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "item_priority", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of client category.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> Optional[pulumi.Input[bool]]:
        """
        Use SSL flag.
        """
        return pulumi.get(self, "use_ssl")

    @use_ssl.setter
    def use_ssl(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_ssl", value)


class Freebox(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_paused: Optional[pulumi.Input[bool]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 app_token: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 destination_directory: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 item_priority: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        <!-- subcategory:Download Clients -->Download Client Freebox resource.
        For more information refer to [Download Client](https://wiki.servarr.com/prowlarr/settings#download-clients) and [Freebox](https://wiki.servarr.com/prowlarr/supported#torrentfreeboxdownload).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_prowlarr as prowlarr

        example = prowlarr.download_clients.Freebox("example",
            api_url="/api/v1/",
            app_id="freebox",
            app_token="Token123",
            enable=True,
            host="mafreebox.freebox.fr",
            port=443,
            priority=1)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:DownloadClients/freebox:Freebox example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] add_paused: Add paused flag.
        :param pulumi.Input[str] api_url: API URL.
        :param pulumi.Input[str] app_id: App ID.
        :param pulumi.Input[str] app_token: App Token.
        :param pulumi.Input[str] category: category.
        :param pulumi.Input[str] destination_directory: Movie directory.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[int] item_priority: Recent Movie priority. `0` Last, `1` First.
        :param pulumi.Input[str] name: Name of client category.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FreeboxArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Download Clients -->Download Client Freebox resource.
        For more information refer to [Download Client](https://wiki.servarr.com/prowlarr/settings#download-clients) and [Freebox](https://wiki.servarr.com/prowlarr/supported#torrentfreeboxdownload).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_prowlarr as prowlarr

        example = prowlarr.download_clients.Freebox("example",
            api_url="/api/v1/",
            app_id="freebox",
            app_token="Token123",
            enable=True,
            host="mafreebox.freebox.fr",
            port=443,
            priority=1)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:DownloadClients/freebox:Freebox example 1
        ```

        :param str resource_name: The name of the resource.
        :param FreeboxArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FreeboxArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_paused: Optional[pulumi.Input[bool]] = None,
                 api_url: Optional[pulumi.Input[str]] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 app_token: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 destination_directory: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 item_priority: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FreeboxArgs.__new__(FreeboxArgs)

            __props__.__dict__["add_paused"] = add_paused
            if api_url is None and not opts.urn:
                raise TypeError("Missing required property 'api_url'")
            __props__.__dict__["api_url"] = api_url
            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            if app_token is None and not opts.urn:
                raise TypeError("Missing required property 'app_token'")
            __props__.__dict__["app_token"] = None if app_token is None else pulumi.Output.secret(app_token)
            __props__.__dict__["category"] = category
            __props__.__dict__["destination_directory"] = destination_directory
            __props__.__dict__["enable"] = enable
            if host is None and not opts.urn:
                raise TypeError("Missing required property 'host'")
            __props__.__dict__["host"] = host
            __props__.__dict__["item_priority"] = item_priority
            __props__.__dict__["name"] = name
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            __props__.__dict__["priority"] = priority
            __props__.__dict__["tags"] = tags
            __props__.__dict__["use_ssl"] = use_ssl
            __props__.__dict__["categories"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["appToken"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Freebox, __self__).__init__(
            'prowlarr:DownloadClients/freebox:Freebox',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            add_paused: Optional[pulumi.Input[bool]] = None,
            api_url: Optional[pulumi.Input[str]] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            app_token: Optional[pulumi.Input[str]] = None,
            categories: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FreeboxCategoryArgs']]]]] = None,
            category: Optional[pulumi.Input[str]] = None,
            destination_directory: Optional[pulumi.Input[str]] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            host: Optional[pulumi.Input[str]] = None,
            item_priority: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            use_ssl: Optional[pulumi.Input[bool]] = None) -> 'Freebox':
        """
        Get an existing Freebox resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] add_paused: Add paused flag.
        :param pulumi.Input[str] api_url: API URL.
        :param pulumi.Input[str] app_id: App ID.
        :param pulumi.Input[str] app_token: App Token.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FreeboxCategoryArgs']]]] categories: List of categories.
        :param pulumi.Input[str] category: category.
        :param pulumi.Input[str] destination_directory: Movie directory.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[int] item_priority: Recent Movie priority. `0` Last, `1` First.
        :param pulumi.Input[str] name: Name of client category.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FreeboxState.__new__(_FreeboxState)

        __props__.__dict__["add_paused"] = add_paused
        __props__.__dict__["api_url"] = api_url
        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["app_token"] = app_token
        __props__.__dict__["categories"] = categories
        __props__.__dict__["category"] = category
        __props__.__dict__["destination_directory"] = destination_directory
        __props__.__dict__["enable"] = enable
        __props__.__dict__["host"] = host
        __props__.__dict__["item_priority"] = item_priority
        __props__.__dict__["name"] = name
        __props__.__dict__["port"] = port
        __props__.__dict__["priority"] = priority
        __props__.__dict__["tags"] = tags
        __props__.__dict__["use_ssl"] = use_ssl
        return Freebox(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addPaused")
    def add_paused(self) -> pulumi.Output[bool]:
        """
        Add paused flag.
        """
        return pulumi.get(self, "add_paused")

    @property
    @pulumi.getter(name="apiUrl")
    def api_url(self) -> pulumi.Output[str]:
        """
        API URL.
        """
        return pulumi.get(self, "api_url")

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        App ID.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="appToken")
    def app_token(self) -> pulumi.Output[str]:
        """
        App Token.
        """
        return pulumi.get(self, "app_token")

    @property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Sequence['outputs.FreeboxCategory']]:
        """
        List of categories.
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        """
        category.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="destinationDirectory")
    def destination_directory(self) -> pulumi.Output[str]:
        """
        Movie directory.
        """
        return pulumi.get(self, "destination_directory")

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        host.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="itemPriority")
    def item_priority(self) -> pulumi.Output[int]:
        """
        Recent Movie priority. `0` Last, `1` First.
        """
        return pulumi.get(self, "item_priority")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of client category.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> pulumi.Output[bool]:
        """
        Use SSL flag.
        """
        return pulumi.get(self, "use_ssl")

