from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SubmitForecastResponse201Distribution")



@_attrs_define
class SubmitForecastResponse201Distribution:
    """ 
        Attributes:
            masses (list[float]):
     """

    masses: list[float]





    def to_dict(self) -> dict[str, Any]:
        masses = self.masses




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "masses": masses,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        masses = cast(list[float], d.pop("masses"))


        submit_forecast_response_201_distribution = cls(
            masses=masses,
        )

        return submit_forecast_response_201_distribution

