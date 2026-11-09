from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_challenges_response_200_data_item_family import ListChallengesResponse200DataItemFamily
from ..models.list_challenges_response_200_data_item_objective import ListChallengesResponse200DataItemObjective
from ..models.list_challenges_response_200_data_item_status import ListChallengesResponse200DataItemStatus
from typing import cast






T = TypeVar("T", bound="ListChallengesResponse200DataItem")



@_attrs_define
class ListChallengesResponse200DataItem:
    """ 
        Attributes:
            slug (str):
            family (ListChallengesResponse200DataItemFamily):
            title (str):
            objective (ListChallengesResponse200DataItemObjective):
            status (ListChallengesResponse200DataItemStatus):
            best_known_value (None | str):
            best_known_at_open (None | str):
            min_improvement (str):
            records_count (int):
            last_record_at (None | str):
            opened_at (str):
            closed_at (None | str):
     """

    slug: str
    family: ListChallengesResponse200DataItemFamily
    title: str
    objective: ListChallengesResponse200DataItemObjective
    status: ListChallengesResponse200DataItemStatus
    best_known_value: None | str
    best_known_at_open: None | str
    min_improvement: str
    records_count: int
    last_record_at: None | str
    opened_at: str
    closed_at: None | str





    def to_dict(self) -> dict[str, Any]:
        slug = self.slug

        family = self.family.value

        title = self.title

        objective = self.objective.value

        status = self.status.value

        best_known_value: None | str
        best_known_value = self.best_known_value

        best_known_at_open: None | str
        best_known_at_open = self.best_known_at_open

        min_improvement = self.min_improvement

        records_count = self.records_count

        last_record_at: None | str
        last_record_at = self.last_record_at

        opened_at = self.opened_at

        closed_at: None | str
        closed_at = self.closed_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "family": family,
            "title": title,
            "objective": objective,
            "status": status,
            "best_known_value": best_known_value,
            "best_known_at_open": best_known_at_open,
            "min_improvement": min_improvement,
            "records_count": records_count,
            "last_record_at": last_record_at,
            "opened_at": opened_at,
            "closed_at": closed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        slug = d.pop("slug")

        family = ListChallengesResponse200DataItemFamily(d.pop("family"))




        title = d.pop("title")

        objective = ListChallengesResponse200DataItemObjective(d.pop("objective"))




        status = ListChallengesResponse200DataItemStatus(d.pop("status"))




        def _parse_best_known_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        best_known_value = _parse_best_known_value(d.pop("best_known_value"))


        def _parse_best_known_at_open(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        best_known_at_open = _parse_best_known_at_open(d.pop("best_known_at_open"))


        min_improvement = d.pop("min_improvement")

        records_count = d.pop("records_count")

        def _parse_last_record_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_record_at = _parse_last_record_at(d.pop("last_record_at"))


        opened_at = d.pop("opened_at")

        def _parse_closed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closed_at = _parse_closed_at(d.pop("closed_at"))


        list_challenges_response_200_data_item = cls(
            slug=slug,
            family=family,
            title=title,
            objective=objective,
            status=status,
            best_known_value=best_known_value,
            best_known_at_open=best_known_at_open,
            min_improvement=min_improvement,
            records_count=records_count,
            last_record_at=last_record_at,
            opened_at=opened_at,
            closed_at=closed_at,
        )

        return list_challenges_response_200_data_item

