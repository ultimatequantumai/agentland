from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_status_response_200_open_incidents_item_severity_type_0 import GetStatusResponse200OpenIncidentsItemSeverityType0
from ..models.get_status_response_200_open_incidents_item_severity_type_1 import GetStatusResponse200OpenIncidentsItemSeverityType1
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_status_response_200_open_incidents_item_latest_update import GetStatusResponse200OpenIncidentsItemLatestUpdate





T = TypeVar("T", bound="GetStatusResponse200OpenIncidentsItem")



@_attrs_define
class GetStatusResponse200OpenIncidentsItem:
    """ 
        Attributes:
            id (UUID):
            severity (GetStatusResponse200OpenIncidentsItemSeverityType0 |
                GetStatusResponse200OpenIncidentsItemSeverityType1):
            title (str):
            created_at (str):
            latest_update (GetStatusResponse200OpenIncidentsItemLatestUpdate):
     """

    id: UUID
    severity: GetStatusResponse200OpenIncidentsItemSeverityType0 | GetStatusResponse200OpenIncidentsItemSeverityType1
    title: str
    created_at: str
    latest_update: GetStatusResponse200OpenIncidentsItemLatestUpdate





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_status_response_200_open_incidents_item_latest_update import GetStatusResponse200OpenIncidentsItemLatestUpdate # noqa: PLC0415
        id = str(self.id)

        severity: int
        if isinstance(self.severity, GetStatusResponse200OpenIncidentsItemSeverityType0):
            severity = self.severity.value
        else:
            severity = self.severity.value


        title = self.title

        created_at = self.created_at

        latest_update = self.latest_update.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "severity": severity,
            "title": title,
            "created_at": created_at,
            "latest_update": latest_update,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_status_response_200_open_incidents_item_latest_update import GetStatusResponse200OpenIncidentsItemLatestUpdate # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_severity(data: object) -> GetStatusResponse200OpenIncidentsItemSeverityType0 | GetStatusResponse200OpenIncidentsItemSeverityType1:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                severity_type_0 = GetStatusResponse200OpenIncidentsItemSeverityType0(data)



                return severity_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, int):
                raise TypeError()
            severity_type_1 = GetStatusResponse200OpenIncidentsItemSeverityType1(data)



            return severity_type_1

        severity = _parse_severity(d.pop("severity"))


        title = d.pop("title")

        created_at = d.pop("created_at")

        latest_update = GetStatusResponse200OpenIncidentsItemLatestUpdate.from_dict(d.pop("latest_update"))




        get_status_response_200_open_incidents_item = cls(
            id=id,
            severity=severity,
            title=title,
            created_at=created_at,
            latest_update=latest_update,
        )

        return get_status_response_200_open_incidents_item

