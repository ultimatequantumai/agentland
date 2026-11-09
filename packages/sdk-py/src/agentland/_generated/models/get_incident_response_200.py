from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_incident_response_200_opened_by import GetIncidentResponse200OpenedBy
from ..models.get_incident_response_200_severity_type_0 import GetIncidentResponse200SeverityType0
from ..models.get_incident_response_200_severity_type_1 import GetIncidentResponse200SeverityType1
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_incident_response_200_updates_item import GetIncidentResponse200UpdatesItem





T = TypeVar("T", bound="GetIncidentResponse200")



@_attrs_define
class GetIncidentResponse200:
    """ 
        Attributes:
            id (UUID):
            severity (GetIncidentResponse200SeverityType0 | GetIncidentResponse200SeverityType1):
            title (str):
            created_at (str):
            opened_by (GetIncidentResponse200OpenedBy):
            updates (list[GetIncidentResponse200UpdatesItem]):
            resolved_at (None | str):
     """

    id: UUID
    severity: GetIncidentResponse200SeverityType0 | GetIncidentResponse200SeverityType1
    title: str
    created_at: str
    opened_by: GetIncidentResponse200OpenedBy
    updates: list[GetIncidentResponse200UpdatesItem]
    resolved_at: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_incident_response_200_updates_item import GetIncidentResponse200UpdatesItem # noqa: PLC0415
        id = str(self.id)

        severity: int
        if isinstance(self.severity, GetIncidentResponse200SeverityType0):
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
        from ..models.get_incident_response_200_updates_item import GetIncidentResponse200UpdatesItem # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_severity(data: object) -> GetIncidentResponse200SeverityType0 | GetIncidentResponse200SeverityType1:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                severity_type_0 = GetIncidentResponse200SeverityType0(data)



                return severity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            severity_type_1 = GetIncidentResponse200SeverityType1(data)



            return severity_type_1

        severity = _parse_severity(d.pop("severity"))


        title = d.pop("title")

        created_at = d.pop("created_at")

        opened_by = GetIncidentResponse200OpenedBy(d.pop("opened_by"))




        updates = []
        _updates = d.pop("updates")
        for updates_item_data in (_updates):
            updates_item = GetIncidentResponse200UpdatesItem.from_dict(updates_item_data)



            updates.append(updates_item)


        def _parse_resolved_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at"))


        get_incident_response_200 = cls(
            id=id,
            severity=severity,
            title=title,
            created_at=created_at,
            opened_by=opened_by,
            updates=updates,
            resolved_at=resolved_at,
        )

        return get_incident_response_200

