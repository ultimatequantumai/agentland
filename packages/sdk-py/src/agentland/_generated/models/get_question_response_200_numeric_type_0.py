from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetQuestionResponse200NumericType0")



@_attrs_define
class GetQuestionResponse200NumericType0:
    """ 
        Attributes:
            unit (str):
            edges (list[float]):
     """

    unit: str
    edges: list[float]





    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        edges = self.edges




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "unit": unit,
            "edges": edges,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit = d.pop("unit")

        edges = cast(list[float], d.pop("edges"))


        get_question_response_200_numeric_type_0 = cls(
            unit=unit,
            edges=edges,
        )

        return get_question_response_200_numeric_type_0

