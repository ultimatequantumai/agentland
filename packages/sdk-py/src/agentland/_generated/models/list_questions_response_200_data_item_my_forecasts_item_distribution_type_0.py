from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ListQuestionsResponse200DataItemMyForecastsItemDistributionType0")



@_attrs_define
class ListQuestionsResponse200DataItemMyForecastsItemDistributionType0:
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


        list_questions_response_200_data_item_my_forecasts_item_distribution_type_0 = cls(
            masses=masses,
        )

        return list_questions_response_200_data_item_my_forecasts_item_distribution_type_0

