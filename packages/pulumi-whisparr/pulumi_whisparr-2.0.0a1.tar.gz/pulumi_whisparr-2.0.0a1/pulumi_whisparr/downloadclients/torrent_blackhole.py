# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TorrentBlackholeArgs', 'TorrentBlackhole']

@pulumi.input_type
class TorrentBlackholeArgs:
    def __init__(__self__, *,
                 torrent_folder: pulumi.Input[str],
                 watch_folder: pulumi.Input[str],
                 enable: Optional[pulumi.Input[bool]] = None,
                 magnet_file_extension: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 save_magnet_files: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
        """
        The set of arguments for constructing a TorrentBlackhole resource.
        :param pulumi.Input[str] torrent_folder: Torrent folder.
        :param pulumi.Input[str] watch_folder: Watch folder flag.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] magnet_file_extension: Magnet file extension.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] read_only: Read only flag.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[bool] save_magnet_files: Save magnet files flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        """
        pulumi.set(__self__, "torrent_folder", torrent_folder)
        pulumi.set(__self__, "watch_folder", watch_folder)
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if magnet_file_extension is not None:
            pulumi.set(__self__, "magnet_file_extension", magnet_file_extension)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)
        if remove_completed_downloads is not None:
            pulumi.set(__self__, "remove_completed_downloads", remove_completed_downloads)
        if remove_failed_downloads is not None:
            pulumi.set(__self__, "remove_failed_downloads", remove_failed_downloads)
        if save_magnet_files is not None:
            pulumi.set(__self__, "save_magnet_files", save_magnet_files)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="torrentFolder")
    def torrent_folder(self) -> pulumi.Input[str]:
        """
        Torrent folder.
        """
        return pulumi.get(self, "torrent_folder")

    @torrent_folder.setter
    def torrent_folder(self, value: pulumi.Input[str]):
        pulumi.set(self, "torrent_folder", value)

    @property
    @pulumi.getter(name="watchFolder")
    def watch_folder(self) -> pulumi.Input[str]:
        """
        Watch folder flag.
        """
        return pulumi.get(self, "watch_folder")

    @watch_folder.setter
    def watch_folder(self, value: pulumi.Input[str]):
        pulumi.set(self, "watch_folder", value)

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
    @pulumi.getter(name="magnetFileExtension")
    def magnet_file_extension(self) -> Optional[pulumi.Input[str]]:
        """
        Magnet file extension.
        """
        return pulumi.get(self, "magnet_file_extension")

    @magnet_file_extension.setter
    def magnet_file_extension(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "magnet_file_extension", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Download Client name.
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
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Read only flag.
        """
        return pulumi.get(self, "read_only")

    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "read_only", value)

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @remove_completed_downloads.setter
    def remove_completed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_completed_downloads", value)

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @remove_failed_downloads.setter
    def remove_failed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_failed_downloads", value)

    @property
    @pulumi.getter(name="saveMagnetFiles")
    def save_magnet_files(self) -> Optional[pulumi.Input[bool]]:
        """
        Save magnet files flag.
        """
        return pulumi.get(self, "save_magnet_files")

    @save_magnet_files.setter
    def save_magnet_files(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "save_magnet_files", value)

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
class _TorrentBlackholeState:
    def __init__(__self__, *,
                 enable: Optional[pulumi.Input[bool]] = None,
                 magnet_file_extension: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 save_magnet_files: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 torrent_folder: Optional[pulumi.Input[str]] = None,
                 watch_folder: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TorrentBlackhole resources.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] magnet_file_extension: Magnet file extension.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] read_only: Read only flag.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[bool] save_magnet_files: Save magnet files flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] torrent_folder: Torrent folder.
        :param pulumi.Input[str] watch_folder: Watch folder flag.
        """
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if magnet_file_extension is not None:
            pulumi.set(__self__, "magnet_file_extension", magnet_file_extension)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)
        if remove_completed_downloads is not None:
            pulumi.set(__self__, "remove_completed_downloads", remove_completed_downloads)
        if remove_failed_downloads is not None:
            pulumi.set(__self__, "remove_failed_downloads", remove_failed_downloads)
        if save_magnet_files is not None:
            pulumi.set(__self__, "save_magnet_files", save_magnet_files)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if torrent_folder is not None:
            pulumi.set(__self__, "torrent_folder", torrent_folder)
        if watch_folder is not None:
            pulumi.set(__self__, "watch_folder", watch_folder)

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
    @pulumi.getter(name="magnetFileExtension")
    def magnet_file_extension(self) -> Optional[pulumi.Input[str]]:
        """
        Magnet file extension.
        """
        return pulumi.get(self, "magnet_file_extension")

    @magnet_file_extension.setter
    def magnet_file_extension(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "magnet_file_extension", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Download Client name.
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
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Read only flag.
        """
        return pulumi.get(self, "read_only")

    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "read_only", value)

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @remove_completed_downloads.setter
    def remove_completed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_completed_downloads", value)

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> Optional[pulumi.Input[bool]]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @remove_failed_downloads.setter
    def remove_failed_downloads(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "remove_failed_downloads", value)

    @property
    @pulumi.getter(name="saveMagnetFiles")
    def save_magnet_files(self) -> Optional[pulumi.Input[bool]]:
        """
        Save magnet files flag.
        """
        return pulumi.get(self, "save_magnet_files")

    @save_magnet_files.setter
    def save_magnet_files(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "save_magnet_files", value)

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
    @pulumi.getter(name="torrentFolder")
    def torrent_folder(self) -> Optional[pulumi.Input[str]]:
        """
        Torrent folder.
        """
        return pulumi.get(self, "torrent_folder")

    @torrent_folder.setter
    def torrent_folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "torrent_folder", value)

    @property
    @pulumi.getter(name="watchFolder")
    def watch_folder(self) -> Optional[pulumi.Input[str]]:
        """
        Watch folder flag.
        """
        return pulumi.get(self, "watch_folder")

    @watch_folder.setter
    def watch_folder(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "watch_folder", value)


class TorrentBlackhole(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 magnet_file_extension: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 save_magnet_files: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 torrent_folder: Optional[pulumi.Input[str]] = None,
                 watch_folder: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- subcategory:Download Clients -->Download Client Torrent Blackhole resource.
        For more information refer to [Download Client](https://wiki.servarr.com/whisparr/settings#download-clients) and [TorrentBlackhole](https://wiki.servarr.com/whisparr/supported#torrentblackhole).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_whisparr as whisparr

        example = whisparr.download_clients.TorrentBlackhole("example",
            enable=True,
            magnet_file_extension=".magnet",
            priority=1,
            torrent_folder="/torrent/",
            watch_folder="/watch/")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import whisparr:DownloadClients/torrentBlackhole:TorrentBlackhole example 1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] magnet_file_extension: Magnet file extension.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] read_only: Read only flag.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[bool] save_magnet_files: Save magnet files flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] torrent_folder: Torrent folder.
        :param pulumi.Input[str] watch_folder: Watch folder flag.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TorrentBlackholeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- subcategory:Download Clients -->Download Client Torrent Blackhole resource.
        For more information refer to [Download Client](https://wiki.servarr.com/whisparr/settings#download-clients) and [TorrentBlackhole](https://wiki.servarr.com/whisparr/supported#torrentblackhole).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_whisparr as whisparr

        example = whisparr.download_clients.TorrentBlackhole("example",
            enable=True,
            magnet_file_extension=".magnet",
            priority=1,
            torrent_folder="/torrent/",
            watch_folder="/watch/")
        ```

        ## Import

        import using the API/UI ID

        ```sh
         $ pulumi import whisparr:DownloadClients/torrentBlackhole:TorrentBlackhole example 1
        ```

        :param str resource_name: The name of the resource.
        :param TorrentBlackholeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TorrentBlackholeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enable: Optional[pulumi.Input[bool]] = None,
                 magnet_file_extension: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
                 remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
                 save_magnet_files: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 torrent_folder: Optional[pulumi.Input[str]] = None,
                 watch_folder: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TorrentBlackholeArgs.__new__(TorrentBlackholeArgs)

            __props__.__dict__["enable"] = enable
            __props__.__dict__["magnet_file_extension"] = magnet_file_extension
            __props__.__dict__["name"] = name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["read_only"] = read_only
            __props__.__dict__["remove_completed_downloads"] = remove_completed_downloads
            __props__.__dict__["remove_failed_downloads"] = remove_failed_downloads
            __props__.__dict__["save_magnet_files"] = save_magnet_files
            __props__.__dict__["tags"] = tags
            if torrent_folder is None and not opts.urn:
                raise TypeError("Missing required property 'torrent_folder'")
            __props__.__dict__["torrent_folder"] = torrent_folder
            if watch_folder is None and not opts.urn:
                raise TypeError("Missing required property 'watch_folder'")
            __props__.__dict__["watch_folder"] = watch_folder
        super(TorrentBlackhole, __self__).__init__(
            'whisparr:DownloadClients/torrentBlackhole:TorrentBlackhole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            enable: Optional[pulumi.Input[bool]] = None,
            magnet_file_extension: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            read_only: Optional[pulumi.Input[bool]] = None,
            remove_completed_downloads: Optional[pulumi.Input[bool]] = None,
            remove_failed_downloads: Optional[pulumi.Input[bool]] = None,
            save_magnet_files: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            torrent_folder: Optional[pulumi.Input[str]] = None,
            watch_folder: Optional[pulumi.Input[str]] = None) -> 'TorrentBlackhole':
        """
        Get an existing TorrentBlackhole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enable: Enable flag.
        :param pulumi.Input[str] magnet_file_extension: Magnet file extension.
        :param pulumi.Input[str] name: Download Client name.
        :param pulumi.Input[int] priority: Priority.
        :param pulumi.Input[bool] read_only: Read only flag.
        :param pulumi.Input[bool] remove_completed_downloads: Remove completed downloads flag.
        :param pulumi.Input[bool] remove_failed_downloads: Remove failed downloads flag.
        :param pulumi.Input[bool] save_magnet_files: Save magnet files flag.
        :param pulumi.Input[Sequence[pulumi.Input[int]]] tags: List of associated tags.
        :param pulumi.Input[str] torrent_folder: Torrent folder.
        :param pulumi.Input[str] watch_folder: Watch folder flag.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TorrentBlackholeState.__new__(_TorrentBlackholeState)

        __props__.__dict__["enable"] = enable
        __props__.__dict__["magnet_file_extension"] = magnet_file_extension
        __props__.__dict__["name"] = name
        __props__.__dict__["priority"] = priority
        __props__.__dict__["read_only"] = read_only
        __props__.__dict__["remove_completed_downloads"] = remove_completed_downloads
        __props__.__dict__["remove_failed_downloads"] = remove_failed_downloads
        __props__.__dict__["save_magnet_files"] = save_magnet_files
        __props__.__dict__["tags"] = tags
        __props__.__dict__["torrent_folder"] = torrent_folder
        __props__.__dict__["watch_folder"] = watch_folder
        return TorrentBlackhole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enable(self) -> pulumi.Output[bool]:
        """
        Enable flag.
        """
        return pulumi.get(self, "enable")

    @property
    @pulumi.getter(name="magnetFileExtension")
    def magnet_file_extension(self) -> pulumi.Output[str]:
        """
        Magnet file extension.
        """
        return pulumi.get(self, "magnet_file_extension")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Download Client name.
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
    @pulumi.getter(name="readOnly")
    def read_only(self) -> pulumi.Output[bool]:
        """
        Read only flag.
        """
        return pulumi.get(self, "read_only")

    @property
    @pulumi.getter(name="removeCompletedDownloads")
    def remove_completed_downloads(self) -> pulumi.Output[bool]:
        """
        Remove completed downloads flag.
        """
        return pulumi.get(self, "remove_completed_downloads")

    @property
    @pulumi.getter(name="removeFailedDownloads")
    def remove_failed_downloads(self) -> pulumi.Output[bool]:
        """
        Remove failed downloads flag.
        """
        return pulumi.get(self, "remove_failed_downloads")

    @property
    @pulumi.getter(name="saveMagnetFiles")
    def save_magnet_files(self) -> pulumi.Output[bool]:
        """
        Save magnet files flag.
        """
        return pulumi.get(self, "save_magnet_files")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[int]]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="torrentFolder")
    def torrent_folder(self) -> pulumi.Output[str]:
        """
        Torrent folder.
        """
        return pulumi.get(self, "torrent_folder")

    @property
    @pulumi.getter(name="watchFolder")
    def watch_folder(self) -> pulumi.Output[str]:
        """
        Watch folder flag.
        """
        return pulumi.get(self, "watch_folder")

