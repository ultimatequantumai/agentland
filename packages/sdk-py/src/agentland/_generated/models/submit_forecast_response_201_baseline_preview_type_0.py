from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_forecast_response_201_baseline_preview_type_0_kind import SubmitForecastResponse201BaselinePreviewType0Kind






T = TypeVar("T", bound="SubmitForecastResponse201BaselinePreviewType0")



@_attrs_define
class SubmitForecastResponse201BaselinePreviewType0:
    """ 
        Attributes:
            kind (SubmitForecastResponse201BaselinePreviewType0Kind):
            p (float):
     """

    kind: SubmitForecastResponse201BaselinePreviewType0Kind
    p: float





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        p = self.p


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "p": p,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = SubmitForecastResponse201BaselinePreviewType0Kind(d.pop("kind"))




        p = d.pop("p")

        submit_forecast_response_201_baseline_preview_type_0 = cls(
            kind=kind,
            p=p,
        )

        return submit_forecast_response_201_baseline_preview_type_0

