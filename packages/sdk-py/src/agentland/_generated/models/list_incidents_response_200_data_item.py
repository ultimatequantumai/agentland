from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_incidents_response_200_data_item_opened_by import ListIncidentsResponse200DataItemOpenedBy
from ..models.list_incidents_response_200_data_item_severity_type_0 import ListIncidentsResponse200DataItemSeverityType0
from ..models.list_incidents_response_200_data_item_severity_type_1 import ListIncidentsResponse200DataItemSeverityType1
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_incidents_response_200_data_item_updates_item import ListIncidentsResponse200DataItemUpdatesItem





T = TypeVar("T", bound="ListIncidentsResponse200DataItem")



@_attrs_define
class ListIncidentsResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            severity (ListIncidentsResponse200DataItemSeverityType0 | ListIncidentsResponse200DataItemSeverityType1):
            title (str):
            created_at (str):
            opened_by (ListIncidentsResponse200DataItemOpenedBy):
            updates (list[ListIncidentsResponse200DataItemUpdatesItem]):
            resolved_at (None | str):
     """

    id: UUID
    severity: ListIncidentsResponse200DataItemSeverityType0 | ListIncidentsResponse200DataItemSeverityType1
    title: str
    created_at: str
    opened_by: ListIncidentsResponse200DataItemOpenedBy
    updates: list[ListIncidentsResponse200DataItemUpdatesItem]
    resolved_at: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_incidents_response_200_data_item_updates_item import ListIncidentsResponse200DataItemUpdatesItem # noqa: PLC0415
        id = str(self.id)

        severity: int
        if isinstance(self.severity, ListIncidentsResponse200DataItemSeverityType0):
            severity = self.severity.value
        else:
            severity = self.severity.value


        title = self.title

        created_at = self.created_at

        opened_by = self.opened_by.value

        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)



        resolved_at: None | str
        resolved_at = self.resolved_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "severity": severity,
            "title": title,
            "created_at": created_at,
            "opened_by": opened_by,
            "updates": updates,
            "resolved_at": resolved_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_incidents_response_200_data_item_updates_item import ListIncidentsResponse200DataItemUpdatesItem # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_severity(data: object) -> ListIncidentsResponse200DataItemSeverityType0 | ListIncidentsResponse200DataItemSeverityType1:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                severity_type_0 = ListIncidentsResponse200DataItemSeverityType0(data)



                return severity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            severity_type_1 = ListIncidentsResponse200DataItemSeverityType1(data)



            return severity_type_1

        severity = _parse_severity(d.pop("severity"))


        title = d.pop("title")

        created_at = d.pop("created_at")

        opened_by = ListIncidentsResponse200DataItemOpenedBy(d.pop("opened_by"))




        updates = []
        _updates = d.pop("updates")
        for updates_item_data in (_updates):
            updates_item = ListIncidentsResponse200DataItemUpdatesItem.from_dict(updates_item_data)



            updates.append(updates_item)


        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))


        list_incidents_response_200_data_item = cls(
            id=id,
            severity=severity,
            title=title,
            created_at=created_at,
            opened_by=opened_by,
            updates=updates,
            resolved_at=resolved_at,
        )

        return list_incidents_response_200_data_item

