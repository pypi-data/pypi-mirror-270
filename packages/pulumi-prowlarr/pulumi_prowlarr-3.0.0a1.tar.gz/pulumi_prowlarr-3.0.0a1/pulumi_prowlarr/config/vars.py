# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('prowlarr')


class _ExportableConfig(types.ModuleType):
    @property
    def api_key(self) -> Optional[str]:
        """
        API key for Prowlarr authentication. Can be specified via the `PROWLARR_API_KEY` environment variable.
        """
        return __config__.get('apiKey')

    @property
    def authorization(self) -> Optional[str]:
        """
        Token for token-based authentication with Prowlarr. This is an alternative to using an API key. Set this via the
        `PROWLARR_AUTHORIZATION` environment variable. One of `authorization` or `api_key` must be provided, but not both.
        """
        return __config__.get('authorization')

    @property
    def url(self) -> Optional[str]:
        """
        Full Prowlarr URL with protocol and port (e.g. `https://test.prowlarr.com:9696`). You should **NOT** supply any path
        (`/api`), the SDK will use the appropriate paths. Can be specified via the `PROWLARR_URL` environment variable.
        """
        return __config__.get('url')

