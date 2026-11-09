from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GetSeriesResponse200TopItemPointsItem")



@_attrs_define
class GetSeriesResponse200TopItemPointsItem:
    """ 
        Attributes:
            question_id (UUID):
            p (float):
            edge (float | None):
     """

    question_id: UUID
    p: float
    edge: float | None





    def to_dict(self) -> dict[str, Any]:
        question_id = str(self.question_id)

        p = self.p

        edge: float | None
        edge = self.edge


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "question_id": question_id,
            "p": p,
            "edge": edge,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        question_id = UUID(d.pop("question_id"))




        p = d.pop("p")

        def _parse_edge(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        edge = _parse_edge(d.pop("edge"))


        get_series_response_200_top_item_points_item = cls(
            question_id=question_id,
            p=p,
            edge=edge,
        )

        return get_series_response_200_top_item_points_item

