from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_me_response_200_agent import GetMeResponse200Agent
  from ..models.get_me_response_200_limits import GetMeResponse200Limits
  from ..models.get_me_response_200_season_type_0 import GetMeResponse200SeasonType0
  from ..models.get_me_response_200_standing import GetMeResponse200Standing
  from ..models.get_me_response_200_vault import GetMeResponse200Vault





T = TypeVar("T", bound="GetMeResponse200")



@_attrs_define
class GetMeResponse200:
    """ 
        Attributes:
            agent (GetMeResponse200Agent):
            limits (GetMeResponse200Limits):
            vault (GetMeResponse200Vault):
            season (GetMeResponse200SeasonType0 | None):
            standing (GetMeResponse200Standing):
     """

    agent: GetMeResponse200Agent
    limits: GetMeResponse200Limits
    vault: GetMeResponse200Vault
    season: GetMeResponse200SeasonType0 | None
    standing: GetMeResponse200Standing





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_me_response_200_agent import GetMeResponse200Agent # noqa: PLC0415
        from ..models.get_me_response_200_limits import GetMeResponse200Limits # noqa: PLC0415
        from ..models.get_me_response_200_season_type_0 import GetMeResponse200SeasonType0 # noqa: PLC0415
        from ..models.get_me_response_200_standing import GetMeResponse200Standing # noqa: PLC0415
        from ..models.get_me_response_200_vault import GetMeResponse200Vault # noqa: PLC0415
        agent = self.agent.to_dict()

        limits = self.limits.to_dict()

        vault = self.vault.to_dict()

        season: dict[str, Any] | None
        if isinstance(self.season, GetMeResponse200SeasonType0):
            season = self.season.to_dict()
        else:
            season = self.season

        standing = self.standing.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
            "limits": limits,
            "vault": vault,
            "season": season,
            "standing": standing,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_me_response_200_agent import GetMeResponse200Agent # noqa: PLC0415
        from ..models.get_me_response_200_limits import GetMeResponse200Limits # noqa: PLC0415
        from ..models.get_me_response_200_season_type_0 import GetMeResponse200SeasonType0 # noqa: PLC0415
        from ..models.get_me_response_200_standing import GetMeResponse200Standing # noqa: PLC0415
        from ..models.get_me_response_200_vault import GetMeResponse200Vault # noqa: PLC0415
        d = dict(src_dict)
        agent = GetMeResponse200Agent.from_dict(d.pop("agent"))




        limits = GetMeResponse200Limits.from_dict(d.pop("limits"))




        vault = GetMeResponse200Vault.from_dict(d.pop("vault"))




        def _parse_season(data: object) -> GetMeResponse200SeasonType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                season_type_0 = GetMeResponse200SeasonType0.from_dict(data)



                return season_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetMeResponse200SeasonType0 | None, data)

        season = _parse_season(d.pop("season"))


        standing = GetMeResponse200Standing.from_dict(d.pop("standing"))




        get_me_response_200 = cls(
            agent=agent,
            limits=limits,
            vault=vault,
            season=season,
            standing=standing,
        )

        return get_me_response_200

