from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_status_response_200_checks_item import GetStatusResponse200ChecksItem
  from ..models.get_status_response_200_open_incidents_item import GetStatusResponse200OpenIncidentsItem





T = TypeVar("T", bound="GetStatusResponse200")



@_attrs_define
class GetStatusResponse200:
    """ 
        Attributes:
            as_of (str):
            checks (list[GetStatusResponse200ChecksItem]):
            scoring_frozen (bool):
            open_incidents (list[GetStatusResponse200OpenIncidentsItem]):
     """

    as_of: str
    checks: list[GetStatusResponse200ChecksItem]
    scoring_frozen: bool
    open_incidents: list[GetStatusResponse200OpenIncidentsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_status_response_200_checks_item import GetStatusResponse200ChecksItem # noqa: PLC0415
        from ..models.get_status_response_200_open_incidents_item import GetStatusResponse200OpenIncidentsItem # noqa: PLC0415
        as_of = self.as_of

        checks = []
        for checks_item_data in self.checks:
            checks_item = checks_item_data.to_dict()
            checks.append(checks_item)



        scoring_frozen = self.scoring_frozen

        open_incidents = []
        for open_incidents_item_data in self.open_incidents:
            open_incidents_item = open_incidents_item_data.to_dict()
            open_incidents.append(open_incidents_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "as_of": as_of,
            "checks": checks,
            "scoring_frozen": scoring_frozen,
            "open_incidents": open_incidents,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_status_response_200_checks_item import GetStatusResponse200ChecksItem # noqa: PLC0415
        from ..models.get_status_response_200_open_incidents_item import GetStatusResponse200OpenIncidentsItem # noqa: PLC0415
        d = dict(src_dict)
        as_of = d.pop("as_of")

        checks = []
        _checks = d.pop("checks")
        for checks_item_data in (_checks):
            checks_item = GetStatusResponse200ChecksItem.from_dict(checks_item_data)



            checks.append(checks_item)


        scoring_frozen = d.pop("scoring_frozen")

        open_incidents = []
        _open_incidents = d.pop("open_incidents")
        for open_incidents_item_data in (_open_incidents):
            open_incidents_item = GetStatusResponse200OpenIncidentsItem.from_dict(open_incidents_item_data)



            open_incidents.append(open_incidents_item)


        get_status_response_200 = cls(
            as_of=as_of,
            checks=checks,
            scoring_frozen=scoring_frozen,
            open_incidents=open_incidents,
        )

        return get_status_response_200

