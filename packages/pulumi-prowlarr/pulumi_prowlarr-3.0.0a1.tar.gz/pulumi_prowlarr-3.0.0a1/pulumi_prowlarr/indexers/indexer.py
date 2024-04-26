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

__all__ = ['IndexerArgs', 'Indexer']

@pulumi.input_type
class IndexerArgs:
    def __init__(__self__, *,
                 app_profile_id: pulumi.Input[int],
                 config_contract: pulumi.Input[str],
                 fields: pulumi.Input[Sequence[pulumi.Input['IndexerFieldArgs']]],
                 implementation: pulumi.Input[str],
                 protocol: pulumi.Input[str],
                 enable: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a Indexer resource.
        :param pulumi.Input[int] app_profile_id: Application profile ID.
        :param pulumi.Input[str] config_contract: Indexer configuration template.
        :param pulumi.Input[Sequence[pulumi.Input['IndexerFieldArgs']]] fields: Set of configuration fields. All non-empty fields must be specified.
        :param pulumi.Input[str] implementation: Indexer implementation name.
        :param pulumi.Input[str] protocol: Protocol. Valid values are 'usenet' and 'torrent'.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] name: Field name.
               It must contain the whole field name comprehensive of its prefix (e.g. `baseSettings.`).
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "app_profile_id", app_profile_id)
        pulumi.set(__self__, "config_contract", config_contract)
        pulumi.set(__self__, "fields", fields)
        pulumi.set(__self__, "implementation", implementation)
        pulumi.set(__self__, "protocol", protocol)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appProfileId")
    def app_profile_id(self) -> pulumi.Input[int]:
        """
        Application profile ID.
        """
        return pulumi.get(self, "app_profile_id")

    @app_profile_id.setter
    def app_profile_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "app_profile_id", value)

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> pulumi.Input[str]:
        """
        Indexer configuration template.
        """
        return pulumi.get(self, "config_contract")

    @config_contract.setter
    def config_contract(self, value: pulumi.Input[str]):
        pulumi.set(self, "config_contract", value)

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Input[Sequence[pulumi.Input['IndexerFieldArgs']]]:
        """
        Set of configuration fields. All non-empty fields must be specified.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: pulumi.Input[Sequence[pulumi.Input['IndexerFieldArgs']]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def implementation(self) -> pulumi.Input[str]:
        """
        Indexer implementation name.
        """
        return pulumi.get(self, "implementation")

    @implementation.setter
    def implementation(self, value: pulumi.Input[str]):
        pulumi.set(self, "implementation", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        Protocol. Valid values are 'usenet' and 'torrent'.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

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
        Field name.
        It must contain the whole field name comprehensive of its prefix (e.g. `baseSettings.`).
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


@pulumi.input_type
class _IndexerState:
    def __init__(__self__, *,
                 app_profile_id: Optional[pulumi.Input[int]] = None,
                 config_contract: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input['IndexerFieldArgs']]]] = None,
                 implementation: Optional[pulumi.Input[str]] = None,
                 language: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 privacy: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        Input properties used for looking up and filtering Indexer resources.
        :param pulumi.Input[int] app_profile_id: Application profile ID.
        :param pulumi.Input[str] config_contract: Indexer configuration template.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[Sequence[pulumi.Input['IndexerFieldArgs']]] fields: Set of configuration fields. All non-empty fields must be specified.
        :param pulumi.Input[str] implementation: Indexer implementation name.
        :param pulumi.Input[str] language: Language.
        :param pulumi.Input[str] name: Field name.
               It must contain the whole field name comprehensive of its prefix (e.g. `baseSettings.`).
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[str] privacy: Privacy.
        :param pulumi.Input[str] protocol: Protocol. Valid values are 'usenet' and 'torrent'.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        if app_profile_id is not None:
            pulumi.set(__self__, "app_profile_id", app_profile_id)
        if config_contract is not None:
            pulumi.set(__self__, "config_contract", config_contract)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if fields is not None:
            pulumi.set(__self__, "fields", fields)
        if implementation is not None:
            pulumi.set(__self__, "implementation", implementation)
        if language is not None:
            pulumi.set(__self__, "language", language)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if privacy is not None:
            pulumi.set(__self__, "privacy", privacy)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appProfileId")
    def app_profile_id(self) -> Optional[pulumi.Input[int]]:
        """
        Application profile ID.
        """
        return pulumi.get(self, "app_profile_id")

    @app_profile_id.setter
    def app_profile_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "app_profile_id", value)

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> Optional[pulumi.Input[str]]:
        """
        Indexer configuration template.
        """
        return pulumi.get(self, "config_contract")

    @config_contract.setter
    def config_contract(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_contract", value)

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
    def fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IndexerFieldArgs']]]]:
        """
        Set of configuration fields. All non-empty fields must be specified.
        """
        return pulumi.get(self, "fields")

    @fields.setter
    def fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IndexerFieldArgs']]]]):
        pulumi.set(self, "fields", value)

    @property
    @pulumi.getter
    def implementation(self) -> Optional[pulumi.Input[str]]:
        """
        Indexer implementation name.
        """
        return pulumi.get(self, "implementation")

    @implementation.setter
    def implementation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "implementation", value)

    @property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input[str]]:
        """
        Language.
        """
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Field name.
        It must contain the whole field name comprehensive of its prefix (e.g. `baseSettings.`).
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
    def privacy(self) -> Optional[pulumi.Input[str]]:
        """
        Privacy.
        """
        return pulumi.get(self, "privacy")

    @privacy.setter
    def privacy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "privacy", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Protocol. Valid values are 'usenet' and 'torrent'.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)

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


class Indexer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_profile_id: Optional[pulumi.Input[int]] = None,
                 config_contract: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexerFieldArgs']]]]] = None,
                 implementation: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        """
        <!-- subcategory:Indexers -->Generic Indexer resource.
        For more information refer to [Indexer](https://wiki.servarr.com/prowlarr/indexers) documentation.

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:Indexers/indexer:Indexer example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] app_profile_id: Application profile ID.
        :param pulumi.Input[str] config_contract: Indexer configuration template.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexerFieldArgs']]]] fields: Set of configuration fields. All non-empty fields must be specified.
        :param pulumi.Input[str] implementation: Indexer implementation name.
        :param pulumi.Input[str] name: Field name.
               It must contain the whole field name comprehensive of its prefix (e.g. `baseSettings.`).
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[str] protocol: Protocol. Valid values are 'usenet' and 'torrent'.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IndexerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Indexers -->Generic Indexer resource.
        For more information refer to [Indexer](https://wiki.servarr.com/prowlarr/indexers) documentation.

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import prowlarr:Indexers/indexer:Indexer example 1
        ```

        :param str resource_name: The name of the resource.
        :param IndexerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IndexerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_profile_id: Optional[pulumi.Input[int]] = None,
                 config_contract: Optional[pulumi.Input[str]] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexerFieldArgs']]]]] = None,
                 implementation: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IndexerArgs.__new__(IndexerArgs)

            if app_profile_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_profile_id'")
            __props__.__dict__["app_profile_id"] = app_profile_id
            if config_contract is None and not opts.urn:
                raise TypeError("Missing required property 'config_contract'")
            __props__.__dict__["config_contract"] = config_contract
            __props__.__dict__["enable"] = enable
            if fields is None and not opts.urn:
                raise TypeError("Missing required property 'fields'")
            __props__.__dict__["fields"] = fields
            if implementation is None and not opts.urn:
                raise TypeError("Missing required property 'implementation'")
            __props__.__dict__["implementation"] = implementation
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__.__dict__["protocol"] = protocol
            __props__.__dict__["tags"] = tags
            __props__.__dict__["language"] = None
            __props__.__dict__["privacy"] = None
        super(Indexer, __self__).__init__(
            'prowlarr:Indexers/indexer:Indexer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_profile_id: Optional[pulumi.Input[int]] = None,
            config_contract: Optional[pulumi.Input[str]] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            fields: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexerFieldArgs']]]]] = None,
            implementation: Optional[pulumi.Input[str]] = None,
            language: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            privacy: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None) -> 'Indexer':
        """
        Get an existing Indexer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] app_profile_id: Application profile ID.
        :param pulumi.Input[str] config_contract: Indexer configuration template.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IndexerFieldArgs']]]] fields: Set of configuration fields. All non-empty fields must be specified.
        :param pulumi.Input[str] implementation: Indexer implementation name.
        :param pulumi.Input[str] language: Language.
        :param pulumi.Input[str] name: Field name.
               It must contain the whole field name comprehensive of its prefix (e.g. `baseSettings.`).
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[str] privacy: Privacy.
        :param pulumi.Input[str] protocol: Protocol. Valid values are 'usenet' and 'torrent'.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IndexerState.__new__(_IndexerState)

        __props__.__dict__["app_profile_id"] = app_profile_id
        __props__.__dict__["config_contract"] = config_contract
        __props__.__dict__["enable"] = enable
        __props__.__dict__["fields"] = fields
        __props__.__dict__["implementation"] = implementation
        __props__.__dict__["language"] = language
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["privacy"] = privacy
        __props__.__dict__["protocol"] = protocol
        __props__.__dict__["tags"] = tags
        return Indexer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appProfileId")
    def app_profile_id(self) -> pulumi.Output[int]:
        """
        Application profile ID.
        """
        return pulumi.get(self, "app_profile_id")

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> pulumi.Output[str]:
        """
        Indexer configuration template.
        """
        return pulumi.get(self, "config_contract")

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter
    def fields(self) -> pulumi.Output[Sequence['outputs.IndexerField']]:
        """
        Set of configuration fields. All non-empty fields must be specified.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def implementation(self) -> pulumi.Output[str]:
        """
        Indexer implementation name.
        """
        return pulumi.get(self, "implementation")

    @property
    @pulumi.getter
    def language(self) -> pulumi.Output[str]:
        """
        Language.
        """
        return pulumi.get(self, "language")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Field name.
        It must contain the whole field name comprehensive of its prefix (e.g. `baseSettings.`).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def privacy(self) -> pulumi.Output[str]:
        """
        Privacy.
        """
        return pulumi.get(self, "privacy")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        Protocol. Valid values are 'usenet' and 'torrent'.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

