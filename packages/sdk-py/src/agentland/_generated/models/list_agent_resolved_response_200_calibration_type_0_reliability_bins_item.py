from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ListAgentResolvedResponse200CalibrationType0ReliabilityBinsItem")



@_attrs_define
class ListAgentResolvedResponse200CalibrationType0ReliabilityBinsItem:
    """ 
        Attributes:
            lower (float):
            upper (float):
            count (int):
            mean_probability (float | None):
            observed_frequency (float | None):
     """

    lower: float
    upper: float
    count: int
    mean_probability: float | None
    observed_frequency: float | None





    def to_dict(self) -> dict[str, Any]:
        lower = self.lower

        upper = self.upper

        count = self.count

        mean_probability: float | None
        mean_probability = self.mean_probability

        observed_frequency: float | None
        observed_frequency = self.observed_frequency


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "lower": lower,
            "upper": upper,
            "count": count,
            "meanProbability": mean_probability,
            "observedFrequency": observed_frequency,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lower = d.pop("lower")

        upper = d.pop("upper")

        count = d.pop("count")

        def _parse_mean_probability(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_probability = _parse_mean_probability(d.pop("meanProbability"))


        def _parse_observed_frequency(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        observed_frequency = _parse_observed_frequency(d.pop("observedFrequency"))


        list_agent_resolved_response_200_calibration_type_0_reliability_bins_item = cls(
            lower=lower,
            upper=upper,
            count=count,
            mean_probability=mean_probability,
            observed_frequency=observed_frequency,
        )

        return list_agent_resolved_response_200_calibration_type_0_reliability_bins_item

