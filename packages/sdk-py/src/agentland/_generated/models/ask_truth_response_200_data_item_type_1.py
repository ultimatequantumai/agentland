from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ask_truth_response_200_data_item_type_1_status import AskTruthResponse200DataItemType1Status
from typing import cast

if TYPE_CHECKING:
  from ..models.ask_truth_response_200_data_item_type_1_market_type_0 import AskTruthResponse200DataItemType1MarketType0
  from ..models.ask_truth_response_200_data_item_type_1_question import AskTruthResponse200DataItemType1Question





T = TypeVar("T", bound="AskTruthResponse200DataItemType1")



@_attrs_define
class AskTruthResponse200DataItemType1:
    """ 
        Attributes:
            status (AskTruthResponse200DataItemType1Status):
            question (AskTruthResponse200DataItemType1Question):
            close_at (str):
            market (AskTruthResponse200DataItemType1MarketType0 | None):
     """

    status: AskTruthResponse200DataItemType1Status
    question: AskTruthResponse200DataItemType1Question
    close_at: str
    market: AskTruthResponse200DataItemType1MarketType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.ask_truth_response_200_data_item_type_1_market_type_0 import AskTruthResponse200DataItemType1MarketType0 # noqa: PLC0415
        from ..models.ask_truth_response_200_data_item_type_1_question import AskTruthResponse200DataItemType1Question # noqa: PLC0415
        status = self.status.value

        question = self.question.to_dict()

        close_at = self.close_at

        market: dict[str, Any] | None
        if isinstance(self.market, AskTruthResponse200DataItemType1MarketType0):
            market = self.market.to_dict()
        else:
            market = self.market


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "question": question,
            "close_at": close_at,
            "market": market,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ask_truth_response_200_data_item_type_1_market_type_0 import AskTruthResponse200DataItemType1MarketType0 # noqa: PLC0415
        from ..models.ask_truth_response_200_data_item_type_1_question import AskTruthResponse200DataItemType1Question # noqa: PLC0415
        d = dict(src_dict)
        status = AskTruthResponse200DataItemType1Status(d.pop("status"))




        question = AskTruthResponse200DataItemType1Question.from_dict(d.pop("question"))




        close_at = d.pop("close_at")

        def _parse_market(data: object) -> AskTruthResponse200DataItemType1MarketType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                market_type_0 = AskTruthResponse200DataItemType1MarketType0.from_dict(data)



                return market_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AskTruthResponse200DataItemType1MarketType0 | None, data)

        market = _parse_market(d.pop("market"))


        ask_truth_response_200_data_item_type_1 = cls(
            status=status,
            question=question,
            close_at=close_at,
            market=market,
        )

        return ask_truth_response_200_data_item_type_1

