from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_season_report_response_200_method_baseline_kind import GetSeasonReportResponse200MethodBaselineKind






T = TypeVar("T", bound="GetSeasonReportResponse200Method")



@_attrs_define
class GetSeasonReportResponse200Method:
    """ 
        Attributes:
            baseline_kind (GetSeasonReportResponse200MethodBaselineKind):
            min_forecasts (int):
            shrink_k (int):
     """

    baseline_kind: GetSeasonReportResponse200MethodBaselineKind
    min_forecasts: int
    shrink_k: int





    def to_dict(self) -> dict[str, Any]:
        baseline_kind = self.baseline_kind.value

        min_forecasts = self.min_forecasts

        shrink_k = self.shrink_k


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "baseline_kind": baseline_kind,
            "min_forecasts": min_forecasts,
            "shrink_k": shrink_k,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        baseline_kind = GetSeasonReportResponse200MethodBaselineKind(d.pop("baseline_kind"))




        min_forecasts = d.pop("min_forecasts")

        shrink_k = d.pop("shrink_k")

        get_season_report_response_200_method = cls(
            baseline_kind=baseline_kind,
            min_forecasts=min_forecasts,
            shrink_k=shrink_k,
        )

        return get_season_report_response_200_method

