from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_profile_response_200_stats_alltime_type_0 import GetAgentProfileResponse200StatsAlltimeType0
  from ..models.get_agent_profile_response_200_stats_season_type_0 import GetAgentProfileResponse200StatsSeasonType0





T = TypeVar("T", bound="GetAgentProfileResponse200Stats")



@_attrs_define
class GetAgentProfileResponse200Stats:
    """ 
        Attributes:
            season (GetAgentProfileResponse200StatsSeasonType0 | None):
            alltime (GetAgentProfileResponse200StatsAlltimeType0 | None):
     """

    season: GetAgentProfileResponse200StatsSeasonType0 | None
    alltime: GetAgentProfileResponse200StatsAlltimeType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_profile_response_200_stats_alltime_type_0 import GetAgentProfileResponse200StatsAlltimeType0 # noqa: PLC0415
        from ..models.get_agent_profile_response_200_stats_season_type_0 import GetAgentProfileResponse200StatsSeasonType0 # noqa: PLC0415
        season: dict[str, Any] | None
        if isinstance(self.season, GetAgentProfileResponse200StatsSeasonType0):
            season = self.season.to_dict()
        else:
            season = self.season

        alltime: dict[str, Any] | None
        if isinstance(self.alltime, GetAgentProfileResponse200StatsAlltimeType0):
            alltime = self.alltime.to_dict()
        else:
            alltime = self.alltime


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "season": season,
            "alltime": alltime,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_profile_response_200_stats_alltime_type_0 import GetAgentProfileResponse200StatsAlltimeType0 # noqa: PLC0415
        from ..models.get_agent_profile_response_200_stats_season_type_0 import GetAgentProfileResponse200StatsSeasonType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_season(data: object) -> GetAgentProfileResponse200StatsSeasonType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                season_type_0 = GetAgentProfileResponse200StatsSeasonType0.from_dict(data)



                return season_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAgentProfileResponse200StatsSeasonType0 | None, data)

        season = _parse_season(d.pop("season"))


        def _parse_alltime(data: object) -> GetAgentProfileResponse200StatsAlltimeType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alltime_type_0 = GetAgentProfileResponse200StatsAlltimeType0.from_dict(data)



                return alltime_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAgentProfileResponse200StatsAlltimeType0 | None, data)

        alltime = _parse_alltime(d.pop("alltime"))


        get_agent_profile_response_200_stats = cls(
            season=season,
            alltime=alltime,
        )

        return get_agent_profile_response_200_stats

