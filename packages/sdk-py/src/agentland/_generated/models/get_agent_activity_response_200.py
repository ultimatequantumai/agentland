from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_activity_response_200_minutes_item import GetAgentActivityResponse200MinutesItem





T = TypeVar("T", bound="GetAgentActivityResponse200")



@_attrs_define
class GetAgentActivityResponse200:
    """ 
        Attributes:
            last_seen_at (None | str):
            minutes (list[GetAgentActivityResponse200MinutesItem]):
            forecasts_today (int):
     """

    last_seen_at: None | str
    minutes: list[GetAgentActivityResponse200MinutesItem]
    forecasts_today: int





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_activity_response_200_minutes_item import GetAgentActivityResponse200MinutesItem # noqa: PLC0415
        last_seen_at: None | str
        last_seen_at = self.last_seen_at

        minutes = []
        for minutes_item_data in self.minutes:
            minutes_item = minutes_item_data.to_dict()
            minutes.append(minutes_item)



        forecasts_today = self.forecasts_today


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "last_seen_at": last_seen_at,
            "minutes": minutes,
            "forecasts_today": forecasts_today,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_activity_response_200_minutes_item import GetAgentActivityResponse200MinutesItem # noqa: PLC0415
        d = dict(src_dict)
        def _parse_last_seen_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_seen_at = _parse_last_seen_at(d.pop("last_seen_at"))


        minutes = []
        _minutes = d.pop("minutes")
        for minutes_item_data in (_minutes):
            minutes_item = GetAgentActivityResponse200MinutesItem.from_dict(minutes_item_data)



            minutes.append(minutes_item)


        forecasts_today = d.pop("forecasts_today")

        get_agent_activity_response_200 = cls(
            last_seen_at=last_seen_at,
            minutes=minutes,
            forecasts_today=forecasts_today,
        )

        return get_agent_activity_response_200

