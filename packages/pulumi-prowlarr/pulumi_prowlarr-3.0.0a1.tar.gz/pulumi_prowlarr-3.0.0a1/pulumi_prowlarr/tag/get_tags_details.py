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
    'GetTagsDetailsResult',
    'AwaitableGetTagsDetailsResult',
    'get_tags_details',
    'get_tags_details_output',
]

@pulumi.output_type
class GetTagsDetailsResult:
    """
    A collection of values returned by getTagsDetails.
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
    def tags(self) -> Sequence['outputs.GetTagsDetailsTagResult']:
        """
        Tag list.
        """
        return pulumi.get(self, "tags")


class AwaitableGetTagsDetailsResult(GetTagsDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTagsDetailsResult(
            id=self.id,
            tags=self.tags)


def get_tags_details(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTagsDetailsResult:
    """
    <!-- subcategory:Tag -->Tag list with their associated resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    example = prowlarr.Tag.get_tags_details()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('prowlarr:Tag/getTagsDetails:getTagsDetails', __args__, opts=opts, typ=GetTagsDetailsResult).value

    return AwaitableGetTagsDetailsResult(
        id=pulumi.get(__ret__, 'id'),
        tags=pulumi.get(__ret__, 'tags'))


@_utilities.lift_output_func(get_tags_details)
def get_tags_details_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTagsDetailsResult]:
    """
    <!-- subcategory:Tag -->Tag list with their associated resources.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_prowlarr as prowlarr

    example = prowlarr.Tag.get_tags_details()
    ```
    """
    ...
