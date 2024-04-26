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

__all__ = ['ProfileArgs', 'Profile']

@pulumi.input_type
class ProfileArgs:
    def __init__(__self__, *,
                 language: pulumi.Input['ProfileLanguageArgs'],
                 quality_groups: pulumi.Input[Sequence[pulumi.Input['ProfileQualityGroupArgs']]],
                 cutoff: Optional[pulumi.Input[int]] = None,
                 cutoff_format_score: Optional[pulumi.Input[int]] = None,
                 format_items: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileFormatItemArgs']]]] = None,
                 min_format_score: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 upgrade_allowed: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Profile resource.
        :param pulumi.Input['ProfileLanguageArgs'] language: Language.
        :param pulumi.Input[Sequence[pulumi.Input['ProfileQualityGroupArgs']]] quality_groups: Quality groups.
        :param pulumi.Input[int] cutoff: Quality ID to which cutoff.
        :param pulumi.Input[int] cutoff_format_score: Cutoff format score.
        :param pulumi.Input[Sequence[pulumi.Input['ProfileFormatItemArgs']]] format_items: Format items.
        :param pulumi.Input[int] min_format_score: Min format score.
        :param pulumi.Input[str] name: Name.
        :param pulumi.Input[bool] upgrade_allowed: Upgrade allowed flag.
        """
        pulumi.set(__self__, "language", language)
        pulumi.set(__self__, "quality_groups", quality_groups)
        if cutoff is not None:
            pulumi.set(__self__, "cutoff", cutoff)
        if cutoff_format_score is not None:
            pulumi.set(__self__, "cutoff_format_score", cutoff_format_score)
        if format_items is not None:
            pulumi.set(__self__, "format_items", format_items)
        if min_format_score is not None:
            pulumi.set(__self__, "min_format_score", min_format_score)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if upgrade_allowed is not None:
            pulumi.set(__self__, "upgrade_allowed", upgrade_allowed)

    @property
    @pulumi.getter
    def language(self) -> pulumi.Input['ProfileLanguageArgs']:
        """
        Language.
        """
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: pulumi.Input['ProfileLanguageArgs']):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter(name="qualityGroups")
    def quality_groups(self) -> pulumi.Input[Sequence[pulumi.Input['ProfileQualityGroupArgs']]]:
        """
        Quality groups.
        """
        return pulumi.get(self, "quality_groups")

    @quality_groups.setter
    def quality_groups(self, value: pulumi.Input[Sequence[pulumi.Input['ProfileQualityGroupArgs']]]):
        pulumi.set(self, "quality_groups", value)

    @property
    @pulumi.getter
    def cutoff(self) -> Optional[pulumi.Input[int]]:
        """
        Quality ID to which cutoff.
        """
        return pulumi.get(self, "cutoff")

    @cutoff.setter
    def cutoff(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cutoff", value)

    @property
    @pulumi.getter(name="cutoffFormatScore")
    def cutoff_format_score(self) -> Optional[pulumi.Input[int]]:
        """
        Cutoff format score.
        """
        return pulumi.get(self, "cutoff_format_score")

    @cutoff_format_score.setter
    def cutoff_format_score(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cutoff_format_score", value)

    @property
    @pulumi.getter(name="formatItems")
    def format_items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProfileFormatItemArgs']]]]:
        """
        Format items.
        """
        return pulumi.get(self, "format_items")

    @format_items.setter
    def format_items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileFormatItemArgs']]]]):
        pulumi.set(self, "format_items", value)

    @property
    @pulumi.getter(name="minFormatScore")
    def min_format_score(self) -> Optional[pulumi.Input[int]]:
        """
        Min format score.
        """
        return pulumi.get(self, "min_format_score")

    @min_format_score.setter
    def min_format_score(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_format_score", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="upgradeAllowed")
    def upgrade_allowed(self) -> Optional[pulumi.Input[bool]]:
        """
        Upgrade allowed flag.
        """
        return pulumi.get(self, "upgrade_allowed")

    @upgrade_allowed.setter
    def upgrade_allowed(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "upgrade_allowed", value)


@pulumi.input_type
class _ProfileState:
    def __init__(__self__, *,
                 cutoff: Optional[pulumi.Input[int]] = None,
                 cutoff_format_score: Optional[pulumi.Input[int]] = None,
                 format_items: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileFormatItemArgs']]]] = None,
                 language: Optional[pulumi.Input['ProfileLanguageArgs']] = None,
                 min_format_score: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_groups: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileQualityGroupArgs']]]] = None,
                 upgrade_allowed: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Profile resources.
        :param pulumi.Input[int] cutoff: Quality ID to which cutoff.
        :param pulumi.Input[int] cutoff_format_score: Cutoff format score.
        :param pulumi.Input[Sequence[pulumi.Input['ProfileFormatItemArgs']]] format_items: Format items.
        :param pulumi.Input['ProfileLanguageArgs'] language: Language.
        :param pulumi.Input[int] min_format_score: Min format score.
        :param pulumi.Input[str] name: Name.
        :param pulumi.Input[Sequence[pulumi.Input['ProfileQualityGroupArgs']]] quality_groups: Quality groups.
        :param pulumi.Input[bool] upgrade_allowed: Upgrade allowed flag.
        """
        if cutoff is not None:
            pulumi.set(__self__, "cutoff", cutoff)
        if cutoff_format_score is not None:
            pulumi.set(__self__, "cutoff_format_score", cutoff_format_score)
        if format_items is not None:
            pulumi.set(__self__, "format_items", format_items)
        if language is not None:
            pulumi.set(__self__, "language", language)
        if min_format_score is not None:
            pulumi.set(__self__, "min_format_score", min_format_score)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if quality_groups is not None:
            pulumi.set(__self__, "quality_groups", quality_groups)
        if upgrade_allowed is not None:
            pulumi.set(__self__, "upgrade_allowed", upgrade_allowed)

    @property
    @pulumi.getter
    def cutoff(self) -> Optional[pulumi.Input[int]]:
        """
        Quality ID to which cutoff.
        """
        return pulumi.get(self, "cutoff")

    @cutoff.setter
    def cutoff(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cutoff", value)

    @property
    @pulumi.getter(name="cutoffFormatScore")
    def cutoff_format_score(self) -> Optional[pulumi.Input[int]]:
        """
        Cutoff format score.
        """
        return pulumi.get(self, "cutoff_format_score")

    @cutoff_format_score.setter
    def cutoff_format_score(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cutoff_format_score", value)

    @property
    @pulumi.getter(name="formatItems")
    def format_items(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProfileFormatItemArgs']]]]:
        """
        Format items.
        """
        return pulumi.get(self, "format_items")

    @format_items.setter
    def format_items(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileFormatItemArgs']]]]):
        pulumi.set(self, "format_items", value)

    @property
    @pulumi.getter
    def language(self) -> Optional[pulumi.Input['ProfileLanguageArgs']]:
        """
        Language.
        """
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: Optional[pulumi.Input['ProfileLanguageArgs']]):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter(name="minFormatScore")
    def min_format_score(self) -> Optional[pulumi.Input[int]]:
        """
        Min format score.
        """
        return pulumi.get(self, "min_format_score")

    @min_format_score.setter
    def min_format_score(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_format_score", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="qualityGroups")
    def quality_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProfileQualityGroupArgs']]]]:
        """
        Quality groups.
        """
        return pulumi.get(self, "quality_groups")

    @quality_groups.setter
    def quality_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProfileQualityGroupArgs']]]]):
        pulumi.set(self, "quality_groups", value)

    @property
    @pulumi.getter(name="upgradeAllowed")
    def upgrade_allowed(self) -> Optional[pulumi.Input[bool]]:
        """
        Upgrade allowed flag.
        """
        return pulumi.get(self, "upgrade_allowed")

    @upgrade_allowed.setter
    def upgrade_allowed(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "upgrade_allowed", value)


class Profile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cutoff: Optional[pulumi.Input[int]] = None,
                 cutoff_format_score: Optional[pulumi.Input[int]] = None,
                 format_items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileFormatItemArgs']]]]] = None,
                 language: Optional[pulumi.Input[pulumi.InputType['ProfileLanguageArgs']]] = None,
                 min_format_score: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileQualityGroupArgs']]]]] = None,
                 upgrade_allowed: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        <!-- subcategory:Profiles -->Quality Profile resource.
        For more information refer to [Quality Profile](https://wiki.servarr.com/whisparr/settings#quality-profiles) documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_whisparr as whisparr

        example = whisparr.profiles.Profile("example",
            cutoff=1100,
            language=whisparr.profiles.ProfileLanguageArgs(
                id=1,
                name="English",
            ),
            quality_groups=[whisparr.profiles.ProfileQualityGroupArgs(
                id=1100,
                name="4k",
                qualities=[
                    whisparr.profiles.ProfileQualityGroupQualityArgs(
                        id=18,
                        name="WEBDL-2160p",
                        resolution=2160,
                        source="web",
                    ),
                    whisparr.profiles.ProfileQualityGroupQualityArgs(
                        id=19,
                        name="Bluray-2160p",
                        resolution=2160,
                        source="bluray",
                    ),
                ],
            )],
            upgrade_allowed=True)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import whisparr:Profiles/profile:Profile example 10
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cutoff: Quality ID to which cutoff.
        :param pulumi.Input[int] cutoff_format_score: Cutoff format score.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileFormatItemArgs']]]] format_items: Format items.
        :param pulumi.Input[pulumi.InputType['ProfileLanguageArgs']] language: Language.
        :param pulumi.Input[int] min_format_score: Min format score.
        :param pulumi.Input[str] name: Name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileQualityGroupArgs']]]] quality_groups: Quality groups.
        :param pulumi.Input[bool] upgrade_allowed: Upgrade allowed flag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Profiles -->Quality Profile resource.
        For more information refer to [Quality Profile](https://wiki.servarr.com/whisparr/settings#quality-profiles) documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_whisparr as whisparr

        example = whisparr.profiles.Profile("example",
            cutoff=1100,
            language=whisparr.profiles.ProfileLanguageArgs(
                id=1,
                name="English",
            ),
            quality_groups=[whisparr.profiles.ProfileQualityGroupArgs(
                id=1100,
                name="4k",
                qualities=[
                    whisparr.profiles.ProfileQualityGroupQualityArgs(
                        id=18,
                        name="WEBDL-2160p",
                        resolution=2160,
                        source="web",
                    ),
                    whisparr.profiles.ProfileQualityGroupQualityArgs(
                        id=19,
                        name="Bluray-2160p",
                        resolution=2160,
                        source="bluray",
                    ),
                ],
            )],
            upgrade_allowed=True)
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import whisparr:Profiles/profile:Profile example 10
        ```

        :param str resource_name: The name of the resource.
        :param ProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cutoff: Optional[pulumi.Input[int]] = None,
                 cutoff_format_score: Optional[pulumi.Input[int]] = None,
                 format_items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileFormatItemArgs']]]]] = None,
                 language: Optional[pulumi.Input[pulumi.InputType['ProfileLanguageArgs']]] = None,
                 min_format_score: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 quality_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileQualityGroupArgs']]]]] = None,
                 upgrade_allowed: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProfileArgs.__new__(ProfileArgs)

            __props__.__dict__["cutoff"] = cutoff
            __props__.__dict__["cutoff_format_score"] = cutoff_format_score
            __props__.__dict__["format_items"] = format_items
            if language is None and not opts.urn:
                raise TypeError("Missing required property 'language'")
            __props__.__dict__["language"] = language
            __props__.__dict__["min_format_score"] = min_format_score
            __props__.__dict__["name"] = name
            if quality_groups is None and not opts.urn:
                raise TypeError("Missing required property 'quality_groups'")
            __props__.__dict__["quality_groups"] = quality_groups
            __props__.__dict__["upgrade_allowed"] = upgrade_allowed
        super(Profile, __self__).__init__(
            'whisparr:Profiles/profile:Profile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cutoff: Optional[pulumi.Input[int]] = None,
            cutoff_format_score: Optional[pulumi.Input[int]] = None,
            format_items: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileFormatItemArgs']]]]] = None,
            language: Optional[pulumi.Input[pulumi.InputType['ProfileLanguageArgs']]] = None,
            min_format_score: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            quality_groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileQualityGroupArgs']]]]] = None,
            upgrade_allowed: Optional[pulumi.Input[bool]] = None) -> 'Profile':
        """
        Get an existing Profile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cutoff: Quality ID to which cutoff.
        :param pulumi.Input[int] cutoff_format_score: Cutoff format score.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileFormatItemArgs']]]] format_items: Format items.
        :param pulumi.Input[pulumi.InputType['ProfileLanguageArgs']] language: Language.
        :param pulumi.Input[int] min_format_score: Min format score.
        :param pulumi.Input[str] name: Name.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProfileQualityGroupArgs']]]] quality_groups: Quality groups.
        :param pulumi.Input[bool] upgrade_allowed: Upgrade allowed flag.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProfileState.__new__(_ProfileState)

        __props__.__dict__["cutoff"] = cutoff
        __props__.__dict__["cutoff_format_score"] = cutoff_format_score
        __props__.__dict__["format_items"] = format_items
        __props__.__dict__["language"] = language
        __props__.__dict__["min_format_score"] = min_format_score
        __props__.__dict__["name"] = name
        __props__.__dict__["quality_groups"] = quality_groups
        __props__.__dict__["upgrade_allowed"] = upgrade_allowed
        return Profile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cutoff(self) -> pulumi.Output[int]:
        """
        Quality ID to which cutoff.
        """
        return pulumi.get(self, "cutoff")

    @property
    @pulumi.getter(name="cutoffFormatScore")
    def cutoff_format_score(self) -> pulumi.Output[int]:
        """
        Cutoff format score.
        """
        return pulumi.get(self, "cutoff_format_score")

    @property
    @pulumi.getter(name="formatItems")
    def format_items(self) -> pulumi.Output[Sequence['outputs.ProfileFormatItem']]:
        """
        Format items.
        """
        return pulumi.get(self, "format_items")

    @property
    @pulumi.getter
    def language(self) -> pulumi.Output['outputs.ProfileLanguage']:
        """
        Language.
        """
        return pulumi.get(self, "language")

    @property
    @pulumi.getter(name="minFormatScore")
    def min_format_score(self) -> pulumi.Output[int]:
        """
        Min format score.
        """
        return pulumi.get(self, "min_format_score")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="qualityGroups")
    def quality_groups(self) -> pulumi.Output[Sequence['outputs.ProfileQualityGroup']]:
        """
        Quality groups.
        """
        return pulumi.get(self, "quality_groups")

    @property
    @pulumi.getter(name="upgradeAllowed")
    def upgrade_allowed(self) -> pulumi.Output[bool]:
        """
        Upgrade allowed flag.
        """
        return pulumi.get(self, "upgrade_allowed")

