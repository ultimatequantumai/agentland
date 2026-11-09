from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetQuestionResponse200MarketType0")



@_attrs_define
class GetQuestionResponse200MarketType0:
    """ 
        Attributes:
            p_yes (float):
            taken_at (str):
            bid (float | None):
            ask (float | None):
            volume_usd (float | None):
     """

    p_yes: float
    taken_at: str
    bid: float | None
    ask: float | None
    volume_usd: float | None





    def to_dict(self) -> dict[str, Any]:
        p_yes = self.p_yes

        taken_at = self.taken_at

        bid: float | None
        bid = self.bid

        ask: float | None
        ask = self.ask

        volume_usd: float | None
        volume_usd = self.volume_usd


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "p_yes": p_yes,
            "taken_at": taken_at,
            "bid": bid,
            "ask": ask,
            "volume_usd": volume_usd,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        p_yes = d.pop("p_yes")

        taken_at = d.pop("taken_at")

        def _parse_bid(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        bid = _parse_bid(d.pop("bid"))


        def _parse_ask(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        ask = _parse_ask(d.pop("ask"))


        def _parse_volume_usd(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        volume_usd = _parse_volume_usd(d.pop("volume_usd"))


        get_question_response_200_market_type_0 = cls(
            p_yes=p_yes,
            taken_at=taken_at,
            bid=bid,
            ask=ask,
            volume_usd=volume_usd,
        )

        return get_question_response_200_market_type_0

