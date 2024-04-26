# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['NotifiarrArgs', 'Notifiarr']

@pulumi.input_type
class NotifiarrArgs:
    def __init__(__self__, *,
                 api_key: pulumi.Input[str],
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 include_manual_grabs: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Notifiarr resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[bool] include_manual_grabs: Include manual grab flag.
        :param pulumi.Input[str] name: NotificationNotifiarr name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_grab: On release grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "api_key", api_key)
        if include_health_warnings is not None:
            pulumi.set(__self__, "include_health_warnings", include_health_warnings)
        if include_manual_grabs is not None:
            pulumi.set(__self__, "include_manual_grabs", include_manual_grabs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if on_application_update is not None:
            pulumi.set(__self__, "on_application_update", on_application_update)
        if on_grab is not None:
            pulumi.set(__self__, "on_grab", on_grab)
        if on_health_issue is not None:
            pulumi.set(__self__, "on_health_issue", on_health_issue)
        if on_health_restored is not None:
            pulumi.set(__self__, "on_health_restored", on_health_restored)
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
    @pulumi.getter(name="includeManualGrabs")
    def include_manual_grabs(self) -> Optional[pulumi.Input[bool]]:
        """
        Include manual grab flag.
        """
        return pulumi.get(self, "include_manual_grabs")

    @include_manual_grabs.setter
    def include_manual_grabs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_manual_grabs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        NotificationNotifiarr name.
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
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> Optional[pulumi.Input[bool]]:
        """
        On release grab flag.
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
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> Optional[pulumi.Input[bool]]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @on_health_restored.setter
    def on_health_restored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_restored", value)

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
class _NotifiarrState:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 include_manual_grabs: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Notifiarr resources.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[bool] include_manual_grabs: Include manual grab flag.
        :param pulumi.Input[str] name: NotificationNotifiarr name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_grab: On release grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if include_health_warnings is not None:
            pulumi.set(__self__, "include_health_warnings", include_health_warnings)
        if include_manual_grabs is not None:
            pulumi.set(__self__, "include_manual_grabs", include_manual_grabs)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if on_application_update is not None:
            pulumi.set(__self__, "on_application_update", on_application_update)
        if on_grab is not None:
            pulumi.set(__self__, "on_grab", on_grab)
        if on_health_issue is not None:
            pulumi.set(__self__, "on_health_issue", on_health_issue)
        if on_health_restored is not None:
            pulumi.set(__self__, "on_health_restored", on_health_restored)
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
    @pulumi.getter(name="includeManualGrabs")
    def include_manual_grabs(self) -> Optional[pulumi.Input[bool]]:
        """
        Include manual grab flag.
        """
        return pulumi.get(self, "include_manual_grabs")

    @include_manual_grabs.setter
    def include_manual_grabs(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_manual_grabs", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        NotificationNotifiarr name.
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
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> Optional[pulumi.Input[bool]]:
        """
        On release grab flag.
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
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> Optional[pulumi.Input[bool]]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @on_health_restored.setter
    def on_health_restored(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "on_health_restored", value)

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


class Notifiarr(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 include_manual_grabs: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Notifications -->Notification Notifiarr resource.
        For more information refer to [Notification](https://wiki.servarr.com/prowlarr/settings#connect) and [Notifiarr](https://wiki.servarr.com/prowlarr/supported#notifiarr).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_prowlarr as prowlarr

        example = prowlarr.notifications.Notifiarr("example",
            api_key="Token",
            include_health_warnings=False,
            on_application_update=False,
            on_health_issue=False)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:Notifications/notifiarr:Notifiarr example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[bool] include_manual_grabs: Include manual grab flag.
        :param pulumi.Input[str] name: NotificationNotifiarr name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_grab: On release grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NotifiarrArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Notifications -->Notification Notifiarr resource.
        For more information refer to [Notification](https://wiki.servarr.com/prowlarr/settings#connect) and [Notifiarr](https://wiki.servarr.com/prowlarr/supported#notifiarr).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_prowlarr as prowlarr

        example = prowlarr.notifications.Notifiarr("example",
            api_key="Token",
            include_health_warnings=False,
            on_application_update=False,
            on_health_issue=False)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:Notifications/notifiarr:Notifiarr example 1
        ```

        :param str resource_name: The name of the resource.
        :param NotifiarrArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NotifiarrArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 include_health_warnings: Optional[pulumi.Input[bool]] = None,
                 include_manual_grabs: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 on_application_update: Optional[pulumi.Input[bool]] = None,
                 on_grab: Optional[pulumi.Input[bool]] = None,
                 on_health_issue: Optional[pulumi.Input[bool]] = None,
                 on_health_restored: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NotifiarrArgs.__new__(NotifiarrArgs)

            if api_key is None and not opts.urn:
                raise TypeError("Missing required property 'api_key'")
            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["include_health_warnings"] = include_health_warnings
            __props__.__dict__["include_manual_grabs"] = include_manual_grabs
            __props__.__dict__["name"] = name
            __props__.__dict__["on_application_update"] = on_application_update
            __props__.__dict__["on_grab"] = on_grab
            __props__.__dict__["on_health_issue"] = on_health_issue
            __props__.__dict__["on_health_restored"] = on_health_restored
            __props__.__dict__["tags"] = tags
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Notifiarr, __self__).__init__(
            'prowlarr:Notifications/notifiarr:Notifiarr',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            include_health_warnings: Optional[pulumi.Input[bool]] = None,
            include_manual_grabs: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            on_application_update: Optional[pulumi.Input[bool]] = None,
            on_grab: Optional[pulumi.Input[bool]] = None,
            on_health_issue: Optional[pulumi.Input[bool]] = None,
            on_health_restored: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Notifiarr':
        """
        Get an existing Notifiarr resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: API key.
        :param pulumi.Input[bool] include_health_warnings: Include health warnings.
        :param pulumi.Input[bool] include_manual_grabs: Include manual grab flag.
        :param pulumi.Input[str] name: NotificationNotifiarr name.
        :param pulumi.Input[bool] on_application_update: On application update flag.
        :param pulumi.Input[bool] on_grab: On release grab flag.
        :param pulumi.Input[bool] on_health_issue: On health issue flag.
        :param pulumi.Input[bool] on_health_restored: On health restored flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NotifiarrState.__new__(_NotifiarrState)

        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["include_health_warnings"] = include_health_warnings
        __props__.__dict__["include_manual_grabs"] = include_manual_grabs
        __props__.__dict__["name"] = name
        __props__.__dict__["on_application_update"] = on_application_update
        __props__.__dict__["on_grab"] = on_grab
        __props__.__dict__["on_health_issue"] = on_health_issue
        __props__.__dict__["on_health_restored"] = on_health_restored
        __props__.__dict__["tags"] = tags
        return Notifiarr(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[str]:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="includeHealthWarnings")
    def include_health_warnings(self) -> pulumi.Output[bool]:
        """
        Include health warnings.
        """
        return pulumi.get(self, "include_health_warnings")

    @property
    @pulumi.getter(name="includeManualGrabs")
    def include_manual_grabs(self) -> pulumi.Output[bool]:
        """
        Include manual grab flag.
        """
        return pulumi.get(self, "include_manual_grabs")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        NotificationNotifiarr name.
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
    @pulumi.getter(name="onGrab")
    def on_grab(self) -> pulumi.Output[bool]:
        """
        On release grab flag.
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
    @pulumi.getter(name="onHealthRestored")
    def on_health_restored(self) -> pulumi.Output[bool]:
        """
        On health restored flag.
        """
        return pulumi.get(self, "on_health_restored")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

