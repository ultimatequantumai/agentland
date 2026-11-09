from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_operator_credits_response_200_data_item_submission_type_0_status import ListOperatorCreditsResponse200DataItemSubmissionType0Status
from typing import cast






T = TypeVar("T", bound="ListOperatorCreditsResponse200DataItemSubmissionType0")



@_attrs_define
class ListOperatorCreditsResponse200DataItemSubmissionType0:
    """ 
        Attributes:
            status (ListOperatorCreditsResponse200DataItemSubmissionType0Status):
            value (None | str):
            compute_ms (int | None):
     """

    status: ListOperatorCreditsResponse200DataItemSubmissionType0Status
    value: None | str
    compute_ms: int | None





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        value: None | str
        value = self.value

        compute_ms: int | None
        compute_ms = self.compute_ms


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "value": value,
            "compute_ms": compute_ms,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ListOperatorCreditsResponse200DataItemSubmissionType0Status(d.pop("status"))




        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))


        def _parse_compute_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        compute_ms = _parse_compute_ms(d.pop("compute_ms"))


        list_operator_credits_response_200_data_item_submission_type_0 = cls(
            status=status,
            value=value,
            compute_ms=compute_ms,
        )

        return list_operator_credits_response_200_data_item_submission_type_0

