from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_daily_response_200_resolved_item_worst_type_0_agent import GetDailyResponse200ResolvedItemWorstType0Agent





T = TypeVar("T", bound="GetDailyResponse200ResolvedItemWorstType0")



@_attrs_define
class GetDailyResponse200ResolvedItemWorstType0:
    """ 
        Attributes:
            agent (GetDailyResponse200ResolvedItemWorstType0Agent):
            edge (float):
     """

    agent: GetDailyResponse200ResolvedItemWorstType0Agent
    edge: float





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_daily_response_200_resolved_item_worst_type_0_agent import GetDailyResponse200ResolvedItemWorstType0Agent # noqa: PLC0415
        agent = self.agent.to_dict()

        edge = self.edge


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "agent": agent,
            "edge": edge,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_daily_response_200_resolved_item_worst_type_0_agent import GetDailyResponse200ResolvedItemWorstType0Agent # noqa: PLC0415
        d = dict(src_dict)
        agent = GetDailyResponse200ResolvedItemWorstType0Agent.from_dict(d.pop("agent"))




        edge = d.pop("edge")

        get_daily_response_200_resolved_item_worst_type_0 = cls(
            agent=agent,
            edge=edge,
        )

        return get_daily_response_200_resolved_item_worst_type_0

