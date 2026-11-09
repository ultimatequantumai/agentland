from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.search_transparency_response_200_disputes import SearchTransparencyResponse200Disputes
  from ..models.search_transparency_response_200_moderation import SearchTransparencyResponse200Moderation
  from ..models.search_transparency_response_200_resolutions import SearchTransparencyResponse200Resolutions
  from ..models.search_transparency_response_200_sources import SearchTransparencyResponse200Sources





T = TypeVar("T", bound="SearchTransparencyResponse200")



@_attrs_define
class SearchTransparencyResponse200:
    """ 
        Attributes:
            q (str):
            resolutions (SearchTransparencyResponse200Resolutions):
            disputes (SearchTransparencyResponse200Disputes):
            moderation (SearchTransparencyResponse200Moderation):
            sources (SearchTransparencyResponse200Sources):
     """

    q: str
    resolutions: SearchTransparencyResponse200Resolutions
    disputes: SearchTransparencyResponse200Disputes
    moderation: SearchTransparencyResponse200Moderation
    sources: SearchTransparencyResponse200Sources





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_transparency_response_200_disputes import SearchTransparencyResponse200Disputes # noqa: PLC0415
        from ..models.search_transparency_response_200_moderation import SearchTransparencyResponse200Moderation # noqa: PLC0415
        from ..models.search_transparency_response_200_resolutions import SearchTransparencyResponse200Resolutions # noqa: PLC0415
        from ..models.search_transparency_response_200_sources import SearchTransparencyResponse200Sources # noqa: PLC0415
        q = self.q

        resolutions = self.resolutions.to_dict()

        disputes = self.disputes.to_dict()

        moderation = self.moderation.to_dict()

        sources = self.sources.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "q": q,
            "resolutions": resolutions,
            "disputes": disputes,
            "moderation": moderation,
            "sources": sources,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_transparency_response_200_disputes import SearchTransparencyResponse200Disputes # noqa: PLC0415
        from ..models.search_transparency_response_200_moderation import SearchTransparencyResponse200Moderation # noqa: PLC0415
        from ..models.search_transparency_response_200_resolutions import SearchTransparencyResponse200Resolutions # noqa: PLC0415
        from ..models.search_transparency_response_200_sources import SearchTransparencyResponse200Sources # noqa: PLC0415
        d = dict(src_dict)
        q = d.pop("q")

        resolutions = SearchTransparencyResponse200Resolutions.from_dict(d.pop("resolutions"))




        disputes = SearchTransparencyResponse200Disputes.from_dict(d.pop("disputes"))




        moderation = SearchTransparencyResponse200Moderation.from_dict(d.pop("moderation"))




        sources = SearchTransparencyResponse200Sources.from_dict(d.pop("sources"))




        search_transparency_response_200 = cls(
            q=q,
            resolutions=resolutions,
            disputes=disputes,
            moderation=moderation,
            sources=sources,
        )

        return search_transparency_response_200

