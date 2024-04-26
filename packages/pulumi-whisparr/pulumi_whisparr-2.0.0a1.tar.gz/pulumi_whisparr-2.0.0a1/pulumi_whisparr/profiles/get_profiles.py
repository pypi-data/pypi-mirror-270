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
    'GetProfilesResult',
    'AwaitableGetProfilesResult',
    'get_profiles',
    'get_profiles_output',
]

@pulumi.output_type
class GetProfilesResult:
    """
    A collection of values returned by getProfiles.
    """
    def __init__(__self__, id=None, quality_profiles=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if quality_profiles and not isinstance(quality_profiles, list):
            raise TypeError("Expected argument 'quality_profiles' to be a list")
        pulumi.set(__self__, "quality_profiles", quality_profiles)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="qualityProfiles")
    def quality_profiles(self) -> Sequence['outputs.GetProfilesQualityProfileResult']:
        """
        Quality Profile list.
        """
        return pulumi.get(self, "quality_profiles")


class AwaitableGetProfilesResult(GetProfilesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProfilesResult(
            id=self.id,
            quality_profiles=self.quality_profiles)


def get_profiles(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProfilesResult:
    """
    <!-- subcategory:Profiles -->List all available Quality Profiles.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_whisparr as whisparr

    example = whisparr.Profiles.get_profiles()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('whisparr:Profiles/getProfiles:getProfiles', __args__, opts=opts, typ=GetProfilesResult).value

    return AwaitableGetProfilesResult(
        id=pulumi.get(__ret__, 'id'),
        quality_profiles=pulumi.get(__ret__, 'quality_profiles'))


@_utilities.lift_output_func(get_profiles)
def get_profiles_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProfilesResult]:
    """
    <!-- subcategory:Profiles -->List all available Quality Profiles.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_whisparr as whisparr

    example = whisparr.Profiles.get_profiles()
    ```
    """
    ...
