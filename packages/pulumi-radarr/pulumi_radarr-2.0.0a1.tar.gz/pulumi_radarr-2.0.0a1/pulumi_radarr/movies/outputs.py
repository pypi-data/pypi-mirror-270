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
    'MovieOriginalLanguage',
    'GetMovieOriginalLanguageResult',
    'GetMoviesMovieResult',
    'GetMoviesMovieOriginalLanguageResult',
]

@pulumi.output_type
class MovieOriginalLanguage(dict):
    def __init__(__self__, *,
                 id: int,
                 name: Optional[str] = None):
        """
        :param int id: ID.
        :param str name: Name.
        """
        pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetMovieOriginalLanguageResult(dict):
    def __init__(__self__, *,
                 id: int,
                 name: str):
        """
        :param int id: ID.
        :param str name: Name.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetMoviesMovieResult(dict):
    def __init__(__self__, *,
                 genres: Sequence[str],
                 id: int,
                 imdb_id: str,
                 is_available: bool,
                 minimum_availability: str,
                 monitored: bool,
                 original_language: 'outputs.GetMoviesMovieOriginalLanguageResult',
                 original_title: str,
                 overview: str,
                 path: str,
                 quality_profile_id: int,
                 status: str,
                 tags: Sequence[int],
                 title: str,
                 tmdb_id: int,
                 website: str,
                 year: int,
                 youtube_trailer_id: str):
        """
        :param Sequence[str] genres: List genres.
        :param int id: Movie ID.
        :param str imdb_id: IMDB ID.
        :param bool is_available: Availability flag.
        :param str minimum_availability: Minimum availability.
               Allowed values: 'tba', 'announced', 'inCinemas', 'released', 'deleted'.
        :param bool monitored: Monitored flag.
        :param 'GetMoviesMovieOriginalLanguageArgs' original_language: Origina language.
        :param str original_title: Movie original title.
        :param str overview: Overview.
        :param str path: Full movie path.
        :param int quality_profile_id: Quality profile ID.
        :param str status: Movie status.
        :param Sequence[int] tags: List of associated tags.
        :param str title: Movie title.
        :param int tmdb_id: TMDB ID.
        :param str website: Website.
        :param int year: Year.
        :param str youtube_trailer_id: Youtube trailer ID.
        """
        pulumi.set(__self__, "genres", genres)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "imdb_id", imdb_id)
        pulumi.set(__self__, "is_available", is_available)
        pulumi.set(__self__, "minimum_availability", minimum_availability)
        pulumi.set(__self__, "monitored", monitored)
        pulumi.set(__self__, "original_language", original_language)
        pulumi.set(__self__, "original_title", original_title)
        pulumi.set(__self__, "overview", overview)
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "quality_profile_id", quality_profile_id)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "tags", tags)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "tmdb_id", tmdb_id)
        pulumi.set(__self__, "website", website)
        pulumi.set(__self__, "year", year)
        pulumi.set(__self__, "youtube_trailer_id", youtube_trailer_id)

    @property
    @pulumi.getter
    def genres(self) -> Sequence[str]:
        """
        List genres.
        """
        return pulumi.get(self, "genres")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Movie ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imdbId")
    def imdb_id(self) -> str:
        """
        IMDB ID.
        """
        return pulumi.get(self, "imdb_id")

    @property
    @pulumi.getter(name="isAvailable")
    def is_available(self) -> bool:
        """
        Availability flag.
        """
        return pulumi.get(self, "is_available")

    @property
    @pulumi.getter(name="minimumAvailability")
    def minimum_availability(self) -> str:
        """
        Minimum availability.
        Allowed values: 'tba', 'announced', 'inCinemas', 'released', 'deleted'.
        """
        return pulumi.get(self, "minimum_availability")

    @property
    @pulumi.getter
    def monitored(self) -> bool:
        """
        Monitored flag.
        """
        return pulumi.get(self, "monitored")

    @property
    @pulumi.getter(name="originalLanguage")
    def original_language(self) -> 'outputs.GetMoviesMovieOriginalLanguageResult':
        """
        Origina language.
        """
        return pulumi.get(self, "original_language")

    @property
    @pulumi.getter(name="originalTitle")
    def original_title(self) -> str:
        """
        Movie original title.
        """
        return pulumi.get(self, "original_title")

    @property
    @pulumi.getter
    def overview(self) -> str:
        """
        Overview.
        """
        return pulumi.get(self, "overview")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Full movie path.
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="qualityProfileId")
    def quality_profile_id(self) -> int:
        """
        Quality profile ID.
        """
        return pulumi.get(self, "quality_profile_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Movie status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[int]:
        """
        List of associated tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Movie title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="tmdbId")
    def tmdb_id(self) -> int:
        """
        TMDB ID.
        """
        return pulumi.get(self, "tmdb_id")

    @property
    @pulumi.getter
    def website(self) -> str:
        """
        Website.
        """
        return pulumi.get(self, "website")

    @property
    @pulumi.getter
    def year(self) -> int:
        """
        Year.
        """
        return pulumi.get(self, "year")

    @property
    @pulumi.getter(name="youtubeTrailerId")
    def youtube_trailer_id(self) -> str:
        """
        Youtube trailer ID.
        """
        return pulumi.get(self, "youtube_trailer_id")


@pulumi.output_type
class GetMoviesMovieOriginalLanguageResult(dict):
    def __init__(__self__, *,
                 id: int,
                 name: str):
        """
        :param int id: Movie ID.
        :param str name: Name.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Movie ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name.
        """
        return pulumi.get(self, "name")


