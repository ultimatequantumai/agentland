from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_notary_proof_response_200_type_1_status import GetNotaryProofResponse200Type1Status
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_notary_proof_response_200_type_1_proof import GetNotaryProofResponse200Type1Proof
  from ..models.get_notary_proof_response_200_type_1_receipt import GetNotaryProofResponse200Type1Receipt





T = TypeVar("T", bound="GetNotaryProofResponse200Type1")



@_attrs_define
class GetNotaryProofResponse200Type1:
    """ 
        Attributes:
            status (GetNotaryProofResponse200Type1Status):
            receipt (GetNotaryProofResponse200Type1Receipt):
            root_date (datetime.date):
            proof (GetNotaryProofResponse200Type1Proof):
     """

    status: GetNotaryProofResponse200Type1Status
    receipt: GetNotaryProofResponse200Type1Receipt
    root_date: datetime.date
    proof: GetNotaryProofResponse200Type1Proof





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_notary_proof_response_200_type_1_proof import GetNotaryProofResponse200Type1Proof # noqa: PLC0415
        from ..models.get_notary_proof_response_200_type_1_receipt import GetNotaryProofResponse200Type1Receipt # noqa: PLC0415
        status = self.status.value

        receipt = self.receipt.to_dict()

        root_date = self.root_date.isoformat()

        proof = self.proof.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "status": status,
            "receipt": receipt,
            "root_date": root_date,
            "proof": proof,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_notary_proof_response_200_type_1_proof import GetNotaryProofResponse200Type1Proof # noqa: PLC0415
        from ..models.get_notary_proof_response_200_type_1_receipt import GetNotaryProofResponse200Type1Receipt # noqa: PLC0415
        d = dict(src_dict)
        status = GetNotaryProofResponse200Type1Status(d.pop("status"))




        receipt = GetNotaryProofResponse200Type1Receipt.from_dict(d.pop("receipt"))




        root_date = datetime.date.fromisoformat(d.pop("root_date"))




        proof = GetNotaryProofResponse200Type1Proof.from_dict(d.pop("proof"))




        get_notary_proof_response_200_type_1 = cls(
            status=status,
            receipt=receipt,
            root_date=root_date,
            proof=proof,
        )

        return get_notary_proof_response_200_type_1

