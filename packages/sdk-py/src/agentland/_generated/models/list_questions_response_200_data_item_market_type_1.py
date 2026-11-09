from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_questions_response_200_data_item_market_type_1_vector import ListQuestionsResponse200DataItemMarketType1Vector





T = TypeVar("T", bound="ListQuestionsResponse200DataItemMarketType1")



@_attrs_define
class ListQuestionsResponse200DataItemMarketType1:
    """ 
        Attributes:
            vector (ListQuestionsResponse200DataItemMarketType1Vector):
            taken_at (str):
     """

    vector: ListQuestionsResponse200DataItemMarketType1Vector
    taken_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_questions_response_200_data_item_market_type_1_vector import ListQuestionsResponse200DataItemMarketType1Vector # noqa: PLC0415
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
        from ..models.list_questions_response_200_data_item_market_type_1_vector import ListQuestionsResponse200DataItemMarketType1Vector # noqa: PLC0415
        d = dict(src_dict)
        vector = ListQuestionsResponse200DataItemMarketType1Vector.from_dict(d.pop("vector"))




        taken_at = d.pop("taken_at")

        list_questions_response_200_data_item_market_type_1 = cls(
            vector=vector,
            taken_at=taken_at,
        )

        return list_questions_response_200_data_item_market_type_1

