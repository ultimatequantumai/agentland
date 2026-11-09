from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="SubmitForecastResponse201Question")



@_attrs_define
class SubmitForecastResponse201Question:
    """ 
        Attributes:
            id (UUID):
            close_at (str):
     """

    id: UUID
    close_at: str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        close_at = self.close_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "close_at": close_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        close_at = d.pop("close_at")

        submit_forecast_response_201_question = cls(
            id=id,
            close_at=close_at,
        )

        return submit_forecast_response_201_question

