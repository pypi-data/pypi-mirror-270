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
    'GetSchemaResult',
    'AwaitableGetSchemaResult',
    'get_schema',
    'get_schema_output',
]

@pulumi.output_type
class GetSchemaResult:
    """
    A collection of values returned by getSchema.
    """
    def __init__(__self__, config_contract=None, description=None, encoding=None, fields=None, id=None, implementation=None, indexer_urls=None, language=None, legacy_urls=None, name=None, privacy=None, protocol=None):
        if config_contract and not isinstance(config_contract, str):
            raise TypeError("Expected argument 'config_contract' to be a str")
        pulumi.set(__self__, "config_contract", config_contract)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encoding and not isinstance(encoding, str):
            raise TypeError("Expected argument 'encoding' to be a str")
        pulumi.set(__self__, "encoding", encoding)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if implementation and not isinstance(implementation, str):
            raise TypeError("Expected argument 'implementation' to be a str")
        pulumi.set(__self__, "implementation", implementation)
        if indexer_urls and not isinstance(indexer_urls, list):
            raise TypeError("Expected argument 'indexer_urls' to be a list")
        pulumi.set(__self__, "indexer_urls", indexer_urls)
        if language and not isinstance(language, str):
            raise TypeError("Expected argument 'language' to be a str")
        pulumi.set(__self__, "language", language)
        if legacy_urls and not isinstance(legacy_urls, list):
            raise TypeError("Expected argument 'legacy_urls' to be a list")
        pulumi.set(__self__, "legacy_urls", legacy_urls)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if privacy and not isinstance(privacy, str):
            raise TypeError("Expected argument 'privacy' to be a str")
        pulumi.set(__self__, "privacy", privacy)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> str:
        """
        Indexer configuration template.
        """
        return pulumi.get(self, "config_contract")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Indexer description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encoding(self) -> str:
        """
        Indexer encoding.
        """
        return pulumi.get(self, "encoding")

    @property
    @pulumi.getter
    def fields(self) -> Sequence['outputs.GetSchemaFieldResult']:
        """
        Set of configuration fields.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Schema ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def implementation(self) -> str:
        """
        Indexer implementation name.
        """
        return pulumi.get(self, "implementation")

    @property
    @pulumi.getter(name="indexerUrls")
    def indexer_urls(self) -> Sequence[str]:
        """
        List of available URLs.
        """
        return pulumi.get(self, "indexer_urls")

    @property
    @pulumi.getter
    def language(self) -> str:
        """
        Language.
        """
        return pulumi.get(self, "language")

    @property
    @pulumi.getter(name="legacyUrls")
    def legacy_urls(self) -> Sequence[str]:
        """
        List of legacy URLs.
        """
        return pulumi.get(self, "legacy_urls")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Indexer name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def privacy(self) -> str:
        """
        Privacy.
        """
        return pulumi.get(self, "privacy")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Protocol. Valid values are 'usenet' and 'torrent'.
        """
        return pulumi.get(self, "protocol")


class AwaitableGetSchemaResult(GetSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchemaResult(
            config_contract=self.config_contract,
            description=self.description,
            encoding=self.encoding,
            fields=self.fields,
            id=self.id,
            implementation=self.implementation,
            indexer_urls=self.indexer_urls,
            language=self.language,
            legacy_urls=self.legacy_urls,
            name=self.name,
            privacy=self.privacy,
            protocol=self.protocol)


def get_schema(name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchemaResult:
    """
    <!-- subcategory:Indexers -->Indexer schema definition.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    test = prowlarr.Indexers.get_schema(name="AlphaRatio")
    ```


    :param str name: Field name.
    """
    __args__ = dict()
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prowlarr:Indexers/getSchema:getSchema', __args__, opts=opts, typ=GetSchemaResult).value

    return AwaitableGetSchemaResult(
        config_contract=pulumi.get(__ret__, 'config_contract'),
        description=pulumi.get(__ret__, 'description'),
        encoding=pulumi.get(__ret__, 'encoding'),
        fields=pulumi.get(__ret__, 'fields'),
        id=pulumi.get(__ret__, 'id'),
        implementation=pulumi.get(__ret__, 'implementation'),
        indexer_urls=pulumi.get(__ret__, 'indexer_urls'),
        language=pulumi.get(__ret__, 'language'),
        legacy_urls=pulumi.get(__ret__, 'legacy_urls'),
        name=pulumi.get(__ret__, 'name'),
        privacy=pulumi.get(__ret__, 'privacy'),
        protocol=pulumi.get(__ret__, 'protocol'))


@_utilities.lift_output_func(get_schema)
def get_schema_output(name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSchemaResult]:
    """
    <!-- subcategory:Indexers -->Indexer schema definition.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    test = prowlarr.Indexers.get_schema(name="AlphaRatio")
    ```


    :param str name: Field name.
    """
    ...
