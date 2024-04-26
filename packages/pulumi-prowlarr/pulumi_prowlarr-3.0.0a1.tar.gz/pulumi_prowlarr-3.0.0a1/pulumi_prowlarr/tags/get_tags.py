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
    'GetTagsResult',
    'AwaitableGetTagsResult',
    'get_tags',
    'get_tags_output',
]

@pulumi.output_type
class GetTagsResult:
    """
    A collection of values returned by getTags.
    """
    def __init__(__self__, id=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Sequence['outputs.GetTagsTagResult']:
        """
        Tag list.
        """
        return pulumi.get(self, "tags")


class AwaitableGetTagsResult(GetTagsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagsResult(
            id=self.id,
            tags=self.tags)


def get_tags(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagsResult:
    """
    <!-- subcategory:Tags -->List all available Tags.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    example = prowlarr.Tags.get_tags()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prowlarr:Tags/getTags:getTags', __args__, opts=opts, typ=GetTagsResult).value

    return AwaitableGetTagsResult(
        id=pulumi.get(__ret__, 'id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_tags)
def get_tags_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagsResult]:
    """
    <!-- subcategory:Tags -->List all available Tags.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    example = prowlarr.Tags.get_tags()
    ```
    """
    ...
