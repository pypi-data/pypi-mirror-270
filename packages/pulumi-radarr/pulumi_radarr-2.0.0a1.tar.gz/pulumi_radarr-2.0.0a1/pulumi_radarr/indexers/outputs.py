# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetIndexersIndexerResult',
]

@pulumi.output_type
class GetIndexersIndexerResult(dict):
    def __init__(__self__, *,
                 additional_parameters: str,
                 allow_zero_size: bool,
                 api_key: str,
                 api_path: str,
                 api_user: str,
                 base_url: str,
                 captcha_token: str,
                 categories: Sequence[int],
                 codecs: Sequence[int],
                 config_contract: str,
                 cookie: str,
                 delay: int,
                 download_client_id: int,
                 enable_automatic_search: bool,
                 enable_interactive_search: bool,
                 enable_rss: bool,
                 id: int,
                 implementation: str,
                 mediums: Sequence[int],
                 minimum_seeders: int,
                 multi_languages: Sequence[int],
                 name: str,
                 passkey: str,
                 priority: int,
                 protocol: str,
                 ranked_only: bool,
                 remove_year: bool,
                 required_flags: Sequence[int],
                 seed_ratio: float,
                 seed_time: int,
                 tags: Sequence[int],
                 user: str,
                 username: str):
        """
        :param str additional_parameters: Additional parameters.
        :param bool allow_zero_size: Allow zero size files.
        :param str api_key: API key.
        :param str api_path: API path.
        :param str api_user: API User.
        :param str base_url: Base URL.
        :param str captcha_token: Captcha token.
        :param Sequence[int] categories: Series list.
        :param Sequence[int] codecs: Codecs.
        :param str config_contract: Indexer configuration template.
        :param str cookie: Cookie.
        :param int delay: Delay before grabbing.
        :param int download_client_id: Download client ID.
        :param bool enable_automatic_search: Enable automatic search flag.
        :param bool enable_interactive_search: Enable interactive search flag.
        :param bool enable_rss: Enable RSS flag.
        :param int id: Indexer ID.
        :param str implementation: Indexer implementation name.
        :param Sequence[int] mediums: Mediumd.
        :param int minimum_seeders: Minimum seeders.
        :param Sequence[int] multi_languages: Language list.
        :param str name: Indexer name.
        :param str passkey: Passkey.
        :param int priority: Priority.
        :param str protocol: Protocol. Valid values are 'usenet' and 'torrent'.
        :param bool ranked_only: Allow ranked only.
        :param bool remove_year: Remove year.
        :param Sequence[int] required_flags: Computed flags.
        :param float seed_ratio: Seed ratio.
        :param int seed_time: Seed time.
        :param Sequence[int] tags: List of associated tags.
        :param str user: Username.
        :param str username: Username.
        """
        pulumi.set(__self__, "additional_parameters", additional_parameters)
        pulumi.set(__self__, "allow_zero_size", allow_zero_size)
        pulumi.set(__self__, "api_key", api_key)
        pulumi.set(__self__, "api_path", api_path)
        pulumi.set(__self__, "api_user", api_user)
        pulumi.set(__self__, "base_url", base_url)
        pulumi.set(__self__, "captcha_token", captcha_token)
        pulumi.set(__self__, "categories", categories)
        pulumi.set(__self__, "codecs", codecs)
        pulumi.set(__self__, "config_contract", config_contract)
        pulumi.set(__self__, "cookie", cookie)
        pulumi.set(__self__, "delay", delay)
        pulumi.set(__self__, "download_client_id", download_client_id)
        pulumi.set(__self__, "enable_automatic_search", enable_automatic_search)
        pulumi.set(__self__, "enable_interactive_search", enable_interactive_search)
        pulumi.set(__self__, "enable_rss", enable_rss)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "implementation", implementation)
        pulumi.set(__self__, "mediums", mediums)
        pulumi.set(__self__, "minimum_seeders", minimum_seeders)
        pulumi.set(__self__, "multi_languages", multi_languages)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "passkey", passkey)
        pulumi.set(__self__, "priority", priority)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "ranked_only", ranked_only)
        pulumi.set(__self__, "remove_year", remove_year)
        pulumi.set(__self__, "required_flags", required_flags)
        pulumi.set(__self__, "seed_ratio", seed_ratio)
        pulumi.set(__self__, "seed_time", seed_time)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "user", user)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="additionalParameters")
    def additional_parameters(self) -> str:
        """
        Additional parameters.
        """
        return pulumi.get(self, "additional_parameters")

    @property
    @pulumi.getter(name="allowZeroSize")
    def allow_zero_size(self) -> bool:
        """
        Allow zero size files.
        """
        return pulumi.get(self, "allow_zero_size")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> str:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="apiPath")
    def api_path(self) -> str:
        """
        API path.
        """
        return pulumi.get(self, "api_path")

    @property
    @pulumi.getter(name="apiUser")
    def api_user(self) -> str:
        """
        API User.
        """
        return pulumi.get(self, "api_user")

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> str:
        """
        Base URL.
        """
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter(name="captchaToken")
    def captcha_token(self) -> str:
        """
        Captcha token.
        """
        return pulumi.get(self, "captcha_token")

    @property
    @pulumi.getter
    def categories(self) -> Sequence[int]:
        """
        Series list.
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter
    def codecs(self) -> Sequence[int]:
        """
        Codecs.
        """
        return pulumi.get(self, "codecs")

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> str:
        """
        Indexer configuration template.
        """
        return pulumi.get(self, "config_contract")

    @property
    @pulumi.getter
    def cookie(self) -> str:
        """
        Cookie.
        """
        return pulumi.get(self, "cookie")

    @property
    @pulumi.getter
    def delay(self) -> int:
        """
        Delay before grabbing.
        """
        return pulumi.get(self, "delay")

    @property
    @pulumi.getter(name="downloadClientId")
    def download_client_id(self) -> int:
        """
        Download client ID.
        """
        return pulumi.get(self, "download_client_id")

    @property
    @pulumi.getter(name="enableAutomaticSearch")
    def enable_automatic_search(self) -> bool:
        """
        Enable automatic search flag.
        """
        return pulumi.get(self, "enable_automatic_search")

    @property
    @pulumi.getter(name="enableInteractiveSearch")
    def enable_interactive_search(self) -> bool:
        """
        Enable interactive search flag.
        """
        return pulumi.get(self, "enable_interactive_search")

    @property
    @pulumi.getter(name="enableRss")
    def enable_rss(self) -> bool:
        """
        Enable RSS flag.
        """
        return pulumi.get(self, "enable_rss")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Indexer ID.
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
    @pulumi.getter
    def mediums(self) -> Sequence[int]:
        """
        Mediumd.
        """
        return pulumi.get(self, "mediums")

    @property
    @pulumi.getter(name="minimumSeeders")
    def minimum_seeders(self) -> int:
        """
        Minimum seeders.
        """
        return pulumi.get(self, "minimum_seeders")

    @property
    @pulumi.getter(name="multiLanguages")
    def multi_languages(self) -> Sequence[int]:
        """
        Language list.
        """
        return pulumi.get(self, "multi_languages")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Indexer name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def passkey(self) -> str:
        """
        Passkey.
        """
        return pulumi.get(self, "passkey")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        Priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Protocol. Valid values are 'usenet' and 'torrent'.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="rankedOnly")
    def ranked_only(self) -> bool:
        """
        Allow ranked only.
        """
        return pulumi.get(self, "ranked_only")

    @property
    @pulumi.getter(name="removeYear")
    def remove_year(self) -> bool:
        """
        Remove year.
        """
        return pulumi.get(self, "remove_year")

    @property
    @pulumi.getter(name="requiredFlags")
    def required_flags(self) -> Sequence[int]:
        """
        Computed flags.
        """
        return pulumi.get(self, "required_flags")

    @property
    @pulumi.getter(name="seedRatio")
    def seed_ratio(self) -> float:
        """
        Seed ratio.
        """
        return pulumi.get(self, "seed_ratio")

    @property
    @pulumi.getter(name="seedTime")
    def seed_time(self) -> int:
        """
        Seed time.
        """
        return pulumi.get(self, "seed_time")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[int]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def user(self) -> str:
        """
        Username.
        """
        return pulumi.get(self, "user")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Username.
        """
        return pulumi.get(self, "username")


