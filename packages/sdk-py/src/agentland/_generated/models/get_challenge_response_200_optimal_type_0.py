from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetChallengeResponse200OptimalType0")



@_attrs_define
class GetChallengeResponse200OptimalType0:
    """ 
        Attributes:
            lower_bound (str):
     """

    lower_bound: str





    def to_dict(self) -> dict[str, Any]:
        lower_bound = self.lower_bound


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "lower_bound": lower_bound,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lower_bound = d.pop("lower_bound")

        get_challenge_response_200_optimal_type_0 = cls(
            lower_bound=lower_bound,
        )

        return get_challenge_response_200_optimal_type_0

