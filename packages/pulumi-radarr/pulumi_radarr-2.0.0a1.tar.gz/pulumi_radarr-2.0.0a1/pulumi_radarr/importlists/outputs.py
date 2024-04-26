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
    'GetExclusionsImportListExclusionResult',
    'GetImportListsImportListResult',
]

@pulumi.output_type
class GetExclusionsImportListExclusionResult(dict):
    def __init__(__self__, *,
                 id: int,
                 title: str,
                 tmdb_id: int,
                 year: int):
        """
        :param int id: Import List Exclusion ID.
        :param str title: Movie to be excluded.
        :param int tmdb_id: Movie TMDB ID.
        :param int year: Year.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "tmdb_id", tmdb_id)
        pulumi.set(__self__, "year", year)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Import List Exclusion ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Movie to be excluded.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="tmdbId")
    def tmdb_id(self) -> int:
        """
        Movie TMDB ID.
        """
        return pulumi.get(self, "tmdb_id")

    @property
    @pulumi.getter
    def year(self) -> int:
        """
        Year.
        """
        return pulumi.get(self, "year")


@pulumi.output_type
class GetImportListsImportListResult(dict):
    def __init__(__self__, *,
                 access_token: str,
                 account_id: str,
                 api_key: str,
                 auth_user: str,
                 base_url: str,
                 cast: bool,
                 cast_director: bool,
                 cast_producer: bool,
                 cast_sound: bool,
                 cast_writing: bool,
                 certification: str,
                 company_id: str,
                 config_contract: str,
                 enable_auto: bool,
                 enabled: bool,
                 exclude_genre_ids: str,
                 expires: str,
                 genres: str,
                 id: int,
                 implementation: str,
                 include_genre_ids: str,
                 keyword_id: str,
                 language_code: int,
                 limit: int,
                 link: str,
                 list_id: str,
                 list_order: int,
                 list_type: str,
                 listname: str,
                 min_score: int,
                 min_vote_average: str,
                 min_votes: str,
                 minimum_availability: str,
                 monitor: str,
                 name: str,
                 only_active: bool,
                 person_id: str,
                 port: int,
                 profile_ids: Sequence[int],
                 quality_profile_id: int,
                 rating: str,
                 refresh_token: str,
                 root_folder_path: str,
                 search_on_add: bool,
                 source: int,
                 tag_ids: Sequence[int],
                 tags: Sequence[int],
                 tmdb_certification: str,
                 tmdb_list_type: int,
                 trakt_additional_parameters: str,
                 trakt_list_type: int,
                 url: str,
                 url_base: str,
                 user_list_type: int,
                 username: str,
                 years: str):
        """
        :param str access_token: Access token.
        :param str account_id: Account ID.
        :param str api_key: API key.
        :param str auth_user: Auth user.
        :param str base_url: Base URL.
        :param bool cast: Include cast.
        :param bool cast_director: Include cast director.
        :param bool cast_producer: Include cast producer.
        :param bool cast_sound: Include cast sound.
        :param bool cast_writing: Include cast writing.
        :param str certification: Certification.
        :param str company_id: Company ID.
        :param str config_contract: ImportList configuration template.
        :param bool enable_auto: Enable automatic add flag.
        :param bool enabled: Enabled flag.
        :param str exclude_genre_ids: Exclude genre IDs.
        :param str expires: Expires.
        :param str genres: Genres.
        :param int id: Import List ID.
        :param str implementation: ImportList implementation name.
        :param str include_genre_ids: Include genre IDs.
        :param str keyword_id: Keyword ID.
        :param int language_code: Language code.
        :param int limit: limit.
        :param str link: Link.
        :param str list_id: List ID.
        :param int list_order: List order.
        :param str list_type: List type.
        :param str listname: List name.
        :param int min_score: Min score.
        :param str min_vote_average: Min vote average.
        :param str min_votes: Min votes.
        :param str minimum_availability: Minimum availability.
        :param str monitor: Should monitor.
        :param str name: Import List name.
        :param bool only_active: Only active.
        :param str person_id: Person ID.
        :param int port: Port.
        :param Sequence[int] profile_ids: Profile IDs.
        :param int quality_profile_id: Quality profile ID.
        :param str rating: Rating.
        :param str refresh_token: Refresh token.
        :param str root_folder_path: Root folder path.
        :param bool search_on_add: Search on add flag.
        :param int source: Source.
        :param Sequence[int] tag_ids: Tag IDs.
        :param Sequence[int] tags: List of associated tags.
        :param str tmdb_certification: Certification.
        :param int tmdb_list_type: TMDB list type.
        :param str trakt_additional_parameters: Trakt additional parameters.
        :param int trakt_list_type: Trakt list type.
        :param str url: URL.
        :param str url_base: Base URL.
        :param int user_list_type: User list type.
        :param str username: Username.
        :param str years: Years.
        """
        pulumi.set(__self__, "access_token", access_token)
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "api_key", api_key)
        pulumi.set(__self__, "auth_user", auth_user)
        pulumi.set(__self__, "base_url", base_url)
        pulumi.set(__self__, "cast", cast)
        pulumi.set(__self__, "cast_director", cast_director)
        pulumi.set(__self__, "cast_producer", cast_producer)
        pulumi.set(__self__, "cast_sound", cast_sound)
        pulumi.set(__self__, "cast_writing", cast_writing)
        pulumi.set(__self__, "certification", certification)
        pulumi.set(__self__, "company_id", company_id)
        pulumi.set(__self__, "config_contract", config_contract)
        pulumi.set(__self__, "enable_auto", enable_auto)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "exclude_genre_ids", exclude_genre_ids)
        pulumi.set(__self__, "expires", expires)
        pulumi.set(__self__, "genres", genres)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "implementation", implementation)
        pulumi.set(__self__, "include_genre_ids", include_genre_ids)
        pulumi.set(__self__, "keyword_id", keyword_id)
        pulumi.set(__self__, "language_code", language_code)
        pulumi.set(__self__, "limit", limit)
        pulumi.set(__self__, "link", link)
        pulumi.set(__self__, "list_id", list_id)
        pulumi.set(__self__, "list_order", list_order)
        pulumi.set(__self__, "list_type", list_type)
        pulumi.set(__self__, "listname", listname)
        pulumi.set(__self__, "min_score", min_score)
        pulumi.set(__self__, "min_vote_average", min_vote_average)
        pulumi.set(__self__, "min_votes", min_votes)
        pulumi.set(__self__, "minimum_availability", minimum_availability)
        pulumi.set(__self__, "monitor", monitor)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "only_active", only_active)
        pulumi.set(__self__, "person_id", person_id)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "profile_ids", profile_ids)
        pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        pulumi.set(__self__, "rating", rating)
        pulumi.set(__self__, "refresh_token", refresh_token)
        pulumi.set(__self__, "root_folder_path", root_folder_path)
        pulumi.set(__self__, "search_on_add", search_on_add)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "tag_ids", tag_ids)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "tmdb_certification", tmdb_certification)
        pulumi.set(__self__, "tmdb_list_type", tmdb_list_type)
        pulumi.set(__self__, "trakt_additional_parameters", trakt_additional_parameters)
        pulumi.set(__self__, "trakt_list_type", trakt_list_type)
        pulumi.set(__self__, "url", url)
        pulumi.set(__self__, "url_base", url_base)
        pulumi.set(__self__, "user_list_type", user_list_type)
        pulumi.set(__self__, "username", username)
        pulumi.set(__self__, "years", years)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> str:
        """
        Access token.
        """
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        Account ID.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> str:
        """
        API key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="authUser")
    def auth_user(self) -> str:
        """
        Auth user.
        """
        return pulumi.get(self, "auth_user")

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> str:
        """
        Base URL.
        """
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter
    def cast(self) -> bool:
        """
        Include cast.
        """
        return pulumi.get(self, "cast")

    @property
    @pulumi.getter(name="castDirector")
    def cast_director(self) -> bool:
        """
        Include cast director.
        """
        return pulumi.get(self, "cast_director")

    @property
    @pulumi.getter(name="castProducer")
    def cast_producer(self) -> bool:
        """
        Include cast producer.
        """
        return pulumi.get(self, "cast_producer")

    @property
    @pulumi.getter(name="castSound")
    def cast_sound(self) -> bool:
        """
        Include cast sound.
        """
        return pulumi.get(self, "cast_sound")

    @property
    @pulumi.getter(name="castWriting")
    def cast_writing(self) -> bool:
        """
        Include cast writing.
        """
        return pulumi.get(self, "cast_writing")

    @property
    @pulumi.getter
    def certification(self) -> str:
        """
        Certification.
        """
        return pulumi.get(self, "certification")

    @property
    @pulumi.getter(name="companyId")
    def company_id(self) -> str:
        """
        Company ID.
        """
        return pulumi.get(self, "company_id")

    @property
    @pulumi.getter(name="configContract")
    def config_contract(self) -> str:
        """
        ImportList configuration template.
        """
        return pulumi.get(self, "config_contract")

    @property
    @pulumi.getter(name="enableAuto")
    def enable_auto(self) -> bool:
        """
        Enable automatic add flag.
        """
        return pulumi.get(self, "enable_auto")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Enabled flag.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="excludeGenreIds")
    def exclude_genre_ids(self) -> str:
        """
        Exclude genre IDs.
        """
        return pulumi.get(self, "exclude_genre_ids")

    @property
    @pulumi.getter
    def expires(self) -> str:
        """
        Expires.
        """
        return pulumi.get(self, "expires")

    @property
    @pulumi.getter
    def genres(self) -> str:
        """
        Genres.
        """
        return pulumi.get(self, "genres")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Import List ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def implementation(self) -> str:
        """
        ImportList implementation name.
        """
        return pulumi.get(self, "implementation")

    @property
    @pulumi.getter(name="includeGenreIds")
    def include_genre_ids(self) -> str:
        """
        Include genre IDs.
        """
        return pulumi.get(self, "include_genre_ids")

    @property
    @pulumi.getter(name="keywordId")
    def keyword_id(self) -> str:
        """
        Keyword ID.
        """
        return pulumi.get(self, "keyword_id")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> int:
        """
        Language code.
        """
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def limit(self) -> int:
        """
        limit.
        """
        return pulumi.get(self, "limit")

    @property
    @pulumi.getter
    def link(self) -> str:
        """
        Link.
        """
        return pulumi.get(self, "link")

    @property
    @pulumi.getter(name="listId")
    def list_id(self) -> str:
        """
        List ID.
        """
        return pulumi.get(self, "list_id")

    @property
    @pulumi.getter(name="listOrder")
    def list_order(self) -> int:
        """
        List order.
        """
        return pulumi.get(self, "list_order")

    @property
    @pulumi.getter(name="listType")
    def list_type(self) -> str:
        """
        List type.
        """
        return pulumi.get(self, "list_type")

    @property
    @pulumi.getter
    def listname(self) -> str:
        """
        List name.
        """
        return pulumi.get(self, "listname")

    @property
    @pulumi.getter(name="minScore")
    def min_score(self) -> int:
        """
        Min score.
        """
        return pulumi.get(self, "min_score")

    @property
    @pulumi.getter(name="minVoteAverage")
    def min_vote_average(self) -> str:
        """
        Min vote average.
        """
        return pulumi.get(self, "min_vote_average")

    @property
    @pulumi.getter(name="minVotes")
    def min_votes(self) -> str:
        """
        Min votes.
        """
        return pulumi.get(self, "min_votes")

    @property
    @pulumi.getter(name="minimumAvailability")
    def minimum_availability(self) -> str:
        """
        Minimum availability.
        """
        return pulumi.get(self, "minimum_availability")

    @property
    @pulumi.getter
    def monitor(self) -> str:
        """
        Should monitor.
        """
        return pulumi.get(self, "monitor")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Import List name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="onlyActive")
    def only_active(self) -> bool:
        """
        Only active.
        """
        return pulumi.get(self, "only_active")

    @property
    @pulumi.getter(name="personId")
    def person_id(self) -> str:
        """
        Person ID.
        """
        return pulumi.get(self, "person_id")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        Port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="profileIds")
    def profile_ids(self) -> Sequence[int]:
        """
        Profile IDs.
        """
        return pulumi.get(self, "profile_ids")

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> int:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @property
    @pulumi.getter
    def rating(self) -> str:
        """
        Rating.
        """
        return pulumi.get(self, "rating")

    @property
    @pulumi.getter(name="refreshToken")
    def refresh_token(self) -> str:
        """
        Refresh token.
        """
        return pulumi.get(self, "refresh_token")

    @property
    @pulumi.getter(name="rootFolderPath")
    def root_folder_path(self) -> str:
        """
        Root folder path.
        """
        return pulumi.get(self, "root_folder_path")

    @property
    @pulumi.getter(name="searchOnAdd")
    def search_on_add(self) -> bool:
        """
        Search on add flag.
        """
        return pulumi.get(self, "search_on_add")

    @property
    @pulumi.getter
    def source(self) -> int:
        """
        Source.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="tagIds")
    def tag_ids(self) -> Sequence[int]:
        """
        Tag IDs.
        """
        return pulumi.get(self, "tag_ids")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[int]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tmdbCertification")
    def tmdb_certification(self) -> str:
        """
        Certification.
        """
        return pulumi.get(self, "tmdb_certification")

    @property
    @pulumi.getter(name="tmdbListType")
    def tmdb_list_type(self) -> int:
        """
        TMDB list type.
        """
        return pulumi.get(self, "tmdb_list_type")

    @property
    @pulumi.getter(name="traktAdditionalParameters")
    def trakt_additional_parameters(self) -> str:
        """
        Trakt additional parameters.
        """
        return pulumi.get(self, "trakt_additional_parameters")

    @property
    @pulumi.getter(name="traktListType")
    def trakt_list_type(self) -> int:
        """
        Trakt list type.
        """
        return pulumi.get(self, "trakt_list_type")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        URL.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="urlBase")
    def url_base(self) -> str:
        """
        Base URL.
        """
        return pulumi.get(self, "url_base")

    @property
    @pulumi.getter(name="userListType")
    def user_list_type(self) -> int:
        """
        User list type.
        """
        return pulumi.get(self, "user_list_type")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Username.
        """
        return pulumi.get(self, "username")

    @property
    @pulumi.getter
    def years(self) -> str:
        """
        Years.
        """
        return pulumi.get(self, "years")


