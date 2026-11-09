from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_leaderboard_response_200_division import GetLeaderboardResponse200Division
from ..models.get_leaderboard_response_200_scope import GetLeaderboardResponse200Scope
from typing import cast

if TYPE_CHECKING:
  from ..models.get_leaderboard_response_200_data_item import GetLeaderboardResponse200DataItem
  from ..models.get_leaderboard_response_200_rules_type_0 import GetLeaderboardResponse200RulesType0
  from ..models.get_leaderboard_response_200_season_type_0 import GetLeaderboardResponse200SeasonType0





T = TypeVar("T", bound="GetLeaderboardResponse200")



@_attrs_define
class GetLeaderboardResponse200:
    """ 
        Attributes:
            scope (GetLeaderboardResponse200Scope):
            season (GetLeaderboardResponse200SeasonType0 | None):
            scoring_version (None | str):
            rules (GetLeaderboardResponse200RulesType0 | None):
            division (GetLeaderboardResponse200Division):
            data (list[GetLeaderboardResponse200DataItem]):
            next_cursor (None | str):
     """

    scope: GetLeaderboardResponse200Scope
    season: GetLeaderboardResponse200SeasonType0 | None
    scoring_version: None | str
    rules: GetLeaderboardResponse200RulesType0 | None
    division: GetLeaderboardResponse200Division
    data: list[GetLeaderboardResponse200DataItem]
    next_cursor: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_leaderboard_response_200_data_item import GetLeaderboardResponse200DataItem # noqa: PLC0415
        from ..models.get_leaderboard_response_200_rules_type_0 import GetLeaderboardResponse200RulesType0 # noqa: PLC0415
        from ..models.get_leaderboard_response_200_season_type_0 import GetLeaderboardResponse200SeasonType0 # noqa: PLC0415
        scope = self.scope.value

        season: dict[str, Any] | None
        if isinstance(self.season, GetLeaderboardResponse200SeasonType0):
            season = self.season.to_dict()
        else:
            season = self.season

        scoring_version: None | str
        scoring_version = self.scoring_version

        rules: dict[str, Any] | None
        if isinstance(self.rules, GetLeaderboardResponse200RulesType0):
            rules = self.rules.to_dict()
        else:
            rules = self.rules

        division = self.division.value

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "scope": scope,
            "season": season,
            "scoring_version": scoring_version,
            "rules": rules,
            "division": division,
            "data": data,
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_leaderboard_response_200_data_item import GetLeaderboardResponse200DataItem # noqa: PLC0415
        from ..models.get_leaderboard_response_200_rules_type_0 import GetLeaderboardResponse200RulesType0 # noqa: PLC0415
        from ..models.get_leaderboard_response_200_season_type_0 import GetLeaderboardResponse200SeasonType0 # noqa: PLC0415
        d = dict(src_dict)
        scope = GetLeaderboardResponse200Scope(d.pop("scope"))




        def _parse_season(data: object) -> GetLeaderboardResponse200SeasonType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                season_type_0 = GetLeaderboardResponse200SeasonType0.from_dict(data)



                return season_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetLeaderboardResponse200SeasonType0 | None, data)

        season = _parse_season(d.pop("season"))


        def _parse_scoring_version(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        scoring_version = _parse_scoring_version(d.pop("scoring_version"))


        def _parse_rules(data: object) -> GetLeaderboardResponse200RulesType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rules_type_0 = GetLeaderboardResponse200RulesType0.from_dict(data)



                return rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetLeaderboardResponse200RulesType0 | None, data)

        rules = _parse_rules(d.pop("rules"))


        division = GetLeaderboardResponse200Division(d.pop("division"))




        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = GetLeaderboardResponse200DataItem.from_dict(data_item_data)



            data.append(data_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        get_leaderboard_response_200 = cls(
            scope=scope,
            season=season,
            scoring_version=scoring_version,
            rules=rules,
            division=division,
            data=data,
            next_cursor=next_cursor,
        )

        return get_leaderboard_response_200

