from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_transparency_sources_response_200_data_item_code import ListTransparencySourcesResponse200DataItemCode
from ..models.list_transparency_sources_response_200_data_item_health import ListTransparencySourcesResponse200DataItemHealth
from ..models.list_transparency_sources_response_200_data_item_state import ListTransparencySourcesResponse200DataItemState
from typing import cast

if TYPE_CHECKING:
  from ..models.list_transparency_sources_response_200_data_item_changes_item import ListTransparencySourcesResponse200DataItemChangesItem
  from ..models.list_transparency_sources_response_200_data_item_days_item import ListTransparencySourcesResponse200DataItemDaysItem





T = TypeVar("T", bound="ListTransparencySourcesResponse200DataItem")



@_attrs_define
class ListTransparencySourcesResponse200DataItem:
    """ 
        Attributes:
            code (ListTransparencySourcesResponse200DataItemCode):
            state (ListTransparencySourcesResponse200DataItemState):
            health (ListTransparencySourcesResponse200DataItemHealth):
            last_ok_at (None | str):
            last_error_at (None | str):
            last_error_code (None | str):
            attempts_30d (int):
            ok_30d (int):
            uptime (float | None):
            days (list[ListTransparencySourcesResponse200DataItemDaysItem]):
            changes (list[ListTransparencySourcesResponse200DataItemChangesItem]):
     """

    code: ListTransparencySourcesResponse200DataItemCode
    state: ListTransparencySourcesResponse200DataItemState
    health: ListTransparencySourcesResponse200DataItemHealth
    last_ok_at: None | str
    last_error_at: None | str
    last_error_code: None | str
    attempts_30d: int
    ok_30d: int
    uptime: float | None
    days: list[ListTransparencySourcesResponse200DataItemDaysItem]
    changes: list[ListTransparencySourcesResponse200DataItemChangesItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_transparency_sources_response_200_data_item_changes_item import ListTransparencySourcesResponse200DataItemChangesItem # noqa: PLC0415
        from ..models.list_transparency_sources_response_200_data_item_days_item import ListTransparencySourcesResponse200DataItemDaysItem # noqa: PLC0415
        code = self.code.value

        state = self.state.value

        health = self.health.value

        last_ok_at: None | str
        last_ok_at = self.last_ok_at

        last_error_at: None | str
        last_error_at = self.last_error_at

        last_error_code: None | str
        last_error_code = self.last_error_code

        attempts_30d = self.attempts_30d

        ok_30d = self.ok_30d

        uptime: float | None
        uptime = self.uptime

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)



        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "code": code,
            "state": state,
            "health": health,
            "last_ok_at": last_ok_at,
            "last_error_at": last_error_at,
            "last_error_code": last_error_code,
            "attempts_30d": attempts_30d,
            "ok_30d": ok_30d,
            "uptime": uptime,
            "days": days,
            "changes": changes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_transparency_sources_response_200_data_item_changes_item import ListTransparencySourcesResponse200DataItemChangesItem # noqa: PLC0415
        from ..models.list_transparency_sources_response_200_data_item_days_item import ListTransparencySourcesResponse200DataItemDaysItem # noqa: PLC0415
        d = dict(src_dict)
        code = ListTransparencySourcesResponse200DataItemCode(d.pop("code"))




        state = ListTransparencySourcesResponse200DataItemState(d.pop("state"))




        health = ListTransparencySourcesResponse200DataItemHealth(d.pop("health"))




        def _parse_last_ok_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_ok_at = _parse_last_ok_at(d.pop("last_ok_at"))


        def _parse_last_error_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error_at = _parse_last_error_at(d.pop("last_error_at"))


        def _parse_last_error_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_error_code = _parse_last_error_code(d.pop("last_error_code"))


        attempts_30d = d.pop("attempts_30d")

        ok_30d = d.pop("ok_30d")

        def _parse_uptime(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        uptime = _parse_uptime(d.pop("uptime"))


        days = []
        _days = d.pop("days")
        for days_item_data in (_days):
            days_item = ListTransparencySourcesResponse200DataItemDaysItem.from_dict(days_item_data)



            days.append(days_item)


        changes = []
        _changes = d.pop("changes")
        for changes_item_data in (_changes):
            changes_item = ListTransparencySourcesResponse200DataItemChangesItem.from_dict(changes_item_data)



            changes.append(changes_item)


        list_transparency_sources_response_200_data_item = cls(
            code=code,
            state=state,
            health=health,
            last_ok_at=last_ok_at,
            last_error_at=last_error_at,
            last_error_code=last_error_code,
            attempts_30d=attempts_30d,
            ok_30d=ok_30d,
            uptime=uptime,
            days=days,
            changes=changes,
        )

        return list_transparency_sources_response_200_data_item

