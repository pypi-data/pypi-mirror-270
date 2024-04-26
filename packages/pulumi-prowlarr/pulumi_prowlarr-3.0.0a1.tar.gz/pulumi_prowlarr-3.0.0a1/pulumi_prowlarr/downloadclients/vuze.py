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

__all__ = ['VuzeArgs', 'Vuze']

@pulumi.input_type
class VuzeArgs:
    def __init__(__self__, *,
                 add_paused: Optional[pulumi.Input[bool]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 directory: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 item_priority: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 url_base: Optional[pulumi.Input[str]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Vuze resource.
        :param pulumi.Input[bool] add_paused: Add paused flag.
        :param pulumi.Input[str] category: Category.
        :param pulumi.Input[str] directory: Directory.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[int] item_priority: Older Movie priority. `0` Last, `1` First.
        :param pulumi.Input[str] name: Name of client category.
        :param pulumi.Input[str] password: Password.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] url_base: Base URL.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        :param pulumi.Input[str] username: Username.
        """
        if add_paused is not None:
            pulumi.set(__self__, "add_paused", add_paused)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if directory is not None:
            pulumi.set(__self__, "directory", directory)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if item_priority is not None:
            pulumi.set(__self__, "item_priority", item_priority)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if url_base is not None:
            pulumi.set(__self__, "url_base", url_base)
        if use_ssl is not None:
            pulumi.set(__self__, "use_ssl", use_ssl)
        if username is not None:
            pulumi.set(__self__, "username", username)

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
        Category.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def directory(self) -> Optional[pulumi.Input[str]]:
        """
        Directory.
        """
        return pulumi.get(self, "directory")

    @directory.setter
    def directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory", value)

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
        Older Movie priority. `0` Last, `1` First.
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
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

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
    @pulumi.getter(name="urlBase")
    def url_base(self) -> Optional[pulumi.Input[str]]:
        """
        Base URL.
        """
        return pulumi.get(self, "url_base")

    @url_base.setter
    def url_base(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url_base", value)

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

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class _VuzeState:
    def __init__(__self__, *,
                 add_paused: Optional[pulumi.Input[bool]] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input['VuzeCategoryArgs']]]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 directory: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 item_priority: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 url_base: Optional[pulumi.Input[str]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Vuze resources.
        :param pulumi.Input[bool] add_paused: Add paused flag.
        :param pulumi.Input[Sequence[pulumi.Input['VuzeCategoryArgs']]] categories: List of categories.
        :param pulumi.Input[str] category: Category.
        :param pulumi.Input[str] directory: Directory.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[int] item_priority: Older Movie priority. `0` Last, `1` First.
        :param pulumi.Input[str] name: Name of client category.
        :param pulumi.Input[str] password: Password.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] url_base: Base URL.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        :param pulumi.Input[str] username: Username.
        """
        if add_paused is not None:
            pulumi.set(__self__, "add_paused", add_paused)
        if categories is not None:
            pulumi.set(__self__, "categories", categories)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if directory is not None:
            pulumi.set(__self__, "directory", directory)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if item_priority is not None:
            pulumi.set(__self__, "item_priority", item_priority)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if url_base is not None:
            pulumi.set(__self__, "url_base", url_base)
        if use_ssl is not None:
            pulumi.set(__self__, "use_ssl", use_ssl)
        if username is not None:
            pulumi.set(__self__, "username", username)

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
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VuzeCategoryArgs']]]]:
        """
        List of categories.
        """
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VuzeCategoryArgs']]]]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        Category.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def directory(self) -> Optional[pulumi.Input[str]]:
        """
        Directory.
        """
        return pulumi.get(self, "directory")

    @directory.setter
    def directory(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory", value)

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
        Older Movie priority. `0` Last, `1` First.
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
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

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
    @pulumi.getter(name="urlBase")
    def url_base(self) -> Optional[pulumi.Input[str]]:
        """
        Base URL.
        """
        return pulumi.get(self, "url_base")

    @url_base.setter
    def url_base(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url_base", value)

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

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Username.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class Vuze(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_paused: Optional[pulumi.Input[bool]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 directory: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 item_priority: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 url_base: Optional[pulumi.Input[str]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- subcategory:Download Clients -->Download Client Vuze resource.
        For more information refer to [Download Client](https://wiki.servarr.com/prowlarr/settings#download-clients) and [Vuze](https://wiki.servarr.com/prowlarr/supported#vuze).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_prowlarr as prowlarr

        example = prowlarr.download_clients.Vuze("example",
            enable=True,
            host="vuze",
            port=9091,
            priority=1,
            url_base="/vuze/")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:DownloadClients/vuze:Vuze example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] add_paused: Add paused flag.
        :param pulumi.Input[str] category: Category.
        :param pulumi.Input[str] directory: Directory.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[int] item_priority: Older Movie priority. `0` Last, `1` First.
        :param pulumi.Input[str] name: Name of client category.
        :param pulumi.Input[str] password: Password.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] url_base: Base URL.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        :param pulumi.Input[str] username: Username.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[VuzeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Download Clients -->Download Client Vuze resource.
        For more information refer to [Download Client](https://wiki.servarr.com/prowlarr/settings#download-clients) and [Vuze](https://wiki.servarr.com/prowlarr/supported#vuze).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_prowlarr as prowlarr

        example = prowlarr.download_clients.Vuze("example",
            enable=True,
            host="vuze",
            port=9091,
            priority=1,
            url_base="/vuze/")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:DownloadClients/vuze:Vuze example 1
        ```

        :param str resource_name: The name of the resource.
        :param VuzeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VuzeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 add_paused: Optional[pulumi.Input[bool]] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 directory: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 item_priority: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 url_base: Optional[pulumi.Input[str]] = None,
                 use_ssl: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VuzeArgs.__new__(VuzeArgs)

            __props__.__dict__["add_paused"] = add_paused
            __props__.__dict__["category"] = category
            __props__.__dict__["directory"] = directory
            __props__.__dict__["enable"] = enable
            __props__.__dict__["host"] = host
            __props__.__dict__["item_priority"] = item_priority
            __props__.__dict__["name"] = name
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            __props__.__dict__["port"] = port
            __props__.__dict__["priority"] = priority
            __props__.__dict__["tags"] = tags
            __props__.__dict__["url_base"] = url_base
            __props__.__dict__["use_ssl"] = use_ssl
            __props__.__dict__["username"] = username
            __props__.__dict__["categories"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Vuze, __self__).__init__(
            'prowlarr:DownloadClients/vuze:Vuze',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            add_paused: Optional[pulumi.Input[bool]] = None,
            categories: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VuzeCategoryArgs']]]]] = None,
            category: Optional[pulumi.Input[str]] = None,
            directory: Optional[pulumi.Input[str]] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            host: Optional[pulumi.Input[str]] = None,
            item_priority: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            url_base: Optional[pulumi.Input[str]] = None,
            use_ssl: Optional[pulumi.Input[bool]] = None,
            username: Optional[pulumi.Input[str]] = None) -> 'Vuze':
        """
        Get an existing Vuze resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] add_paused: Add paused flag.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VuzeCategoryArgs']]]] categories: List of categories.
        :param pulumi.Input[str] category: Category.
        :param pulumi.Input[str] directory: Directory.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] host: host.
        :param pulumi.Input[int] item_priority: Older Movie priority. `0` Last, `1` First.
        :param pulumi.Input[str] name: Name of client category.
        :param pulumi.Input[str] password: Password.
        :param pulumi.Input[int] port: Port.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] url_base: Base URL.
        :param pulumi.Input[bool] use_ssl: Use SSL flag.
        :param pulumi.Input[str] username: Username.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VuzeState.__new__(_VuzeState)

        __props__.__dict__["add_paused"] = add_paused
        __props__.__dict__["categories"] = categories
        __props__.__dict__["category"] = category
        __props__.__dict__["directory"] = directory
        __props__.__dict__["enable"] = enable
        __props__.__dict__["host"] = host
        __props__.__dict__["item_priority"] = item_priority
        __props__.__dict__["name"] = name
        __props__.__dict__["password"] = password
        __props__.__dict__["port"] = port
        __props__.__dict__["priority"] = priority
        __props__.__dict__["tags"] = tags
        __props__.__dict__["url_base"] = url_base
        __props__.__dict__["use_ssl"] = use_ssl
        __props__.__dict__["username"] = username
        return Vuze(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addPaused")
    def add_paused(self) -> pulumi.Output[bool]:
        """
        Add paused flag.
        """
        return pulumi.get(self, "add_paused")

    @property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Sequence['outputs.VuzeCategory']]:
        """
        List of categories.
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        """
        Category.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def directory(self) -> pulumi.Output[str]:
        """
        Directory.
        """
        return pulumi.get(self, "directory")

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
        Older Movie priority. `0` Last, `1` First.
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
    def password(self) -> pulumi.Output[str]:
        """
        Password.
        """
        return pulumi.get(self, "password")

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
    @pulumi.getter(name="urlBase")
    def url_base(self) -> pulumi.Output[str]:
        """
        Base URL.
        """
        return pulumi.get(self, "url_base")

    @property
    @pulumi.getter(name="useSsl")
    def use_ssl(self) -> pulumi.Output[bool]:
        """
        Use SSL flag.
        """
        return pulumi.get(self, "use_ssl")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        Username.
        """
        return pulumi.get(self, "username")

