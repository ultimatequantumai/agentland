from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.list_agent_resolved_response_200_calibration_type_0_reliability_bins_item import ListAgentResolvedResponse200CalibrationType0ReliabilityBinsItem





T = TypeVar("T", bound="ListAgentResolvedResponse200CalibrationType0")



@_attrs_define
class ListAgentResolvedResponse200CalibrationType0:
    """ 
        Attributes:
            n (int):
            ece (float | None):
            reliability_bins (list[ListAgentResolvedResponse200CalibrationType0ReliabilityBinsItem]):
     """

    n: int
    ece: float | None
    reliability_bins: list[ListAgentResolvedResponse200CalibrationType0ReliabilityBinsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_resolved_response_200_calibration_type_0_reliability_bins_item import ListAgentResolvedResponse200CalibrationType0ReliabilityBinsItem # noqa: PLC0415
        n = self.n

        ece: float | None
        ece = self.ece

        reliability_bins = []
        for reliability_bins_item_data in self.reliability_bins:
            reliability_bins_item = reliability_bins_item_data.to_dict()
            reliability_bins.append(reliability_bins_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "n": n,
            "ece": ece,
            "reliability_bins": reliability_bins,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_agent_resolved_response_200_calibration_type_0_reliability_bins_item import ListAgentResolvedResponse200CalibrationType0ReliabilityBinsItem # noqa: PLC0415
        d = dict(src_dict)
        n = d.pop("n")

        def _parse_ece(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        ece = _parse_ece(d.pop("ece"))


        reliability_bins = []
        _reliability_bins = d.pop("reliability_bins")
        for reliability_bins_item_data in (_reliability_bins):
            reliability_bins_item = ListAgentResolvedResponse200CalibrationType0ReliabilityBinsItem.from_dict(reliability_bins_item_data)



            reliability_bins.append(reliability_bins_item)


        list_agent_resolved_response_200_calibration_type_0 = cls(
            n=n,
            ece=ece,
            reliability_bins=reliability_bins,
        )

        return list_agent_resolved_response_200_calibration_type_0

