from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_notary_proof_response_200_type_0_status import GetNotaryProofResponse200Type0Status
from typing import cast

if TYPE_CHECKING:
  from ..models.get_notary_proof_response_200_type_0_receipt import GetNotaryProofResponse200Type0Receipt





T = TypeVar("T", bound="GetNotaryProofResponse200Type0")



@_attrs_define
class GetNotaryProofResponse200Type0:
    """ 
        Attributes:
            status (GetNotaryProofResponse200Type0Status):
            receipt (GetNotaryProofResponse200Type0Receipt):
     """

    status: GetNotaryProofResponse200Type0Status
    receipt: GetNotaryProofResponse200Type0Receipt





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_notary_proof_response_200_type_0_receipt import GetNotaryProofResponse200Type0Receipt # noqa: PLC0415
        status = self.status.value

        receipt = self.receipt.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "receipt": receipt,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_notary_proof_response_200_type_0_receipt import GetNotaryProofResponse200Type0Receipt # noqa: PLC0415
        d = dict(src_dict)
        status = GetNotaryProofResponse200Type0Status(d.pop("status"))




        receipt = GetNotaryProofResponse200Type0Receipt.from_dict(d.pop("receipt"))




        get_notary_proof_response_200_type_0 = cls(
            status=status,
            receipt=receipt,
        )

        return get_notary_proof_response_200_type_0

