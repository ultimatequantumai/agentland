from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_question_response_200_market_type_1_vector import GetQuestionResponse200MarketType1Vector





T = TypeVar("T", bound="GetQuestionResponse200MarketType1")



@_attrs_define
class GetQuestionResponse200MarketType1:
    """ 
        Attributes:
            vector (GetQuestionResponse200MarketType1Vector):
            taken_at (str):
     """

    vector: GetQuestionResponse200MarketType1Vector
    taken_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_question_response_200_market_type_1_vector import GetQuestionResponse200MarketType1Vector # noqa: PLC0415
        vector = self.vector.to_dict()

        taken_at = self.taken_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "vector": vector,
            "taken_at": taken_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_question_response_200_market_type_1_vector import GetQuestionResponse200MarketType1Vector # noqa: PLC0415
        d = dict(src_dict)
        vector = GetQuestionResponse200MarketType1Vector.from_dict(d.pop("vector"))




        taken_at = d.pop("taken_at")

        get_question_response_200_market_type_1 = cls(
            vector=vector,
            taken_at=taken_at,
        )

        return get_question_response_200_market_type_1

