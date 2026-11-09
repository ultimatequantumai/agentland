from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="GetChallengeResponse200RecordsItemSignatureType0")



@_attrs_define
class GetChallengeResponse200RecordsItemSignatureType0:
    """ 
        Attributes:
            signing_key_id (UUID):
     """

    signing_key_id: UUID





    def to_dict(self) -> dict[str, Any]:
        signing_key_id = str(self.signing_key_id)


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "signing_key_id": signing_key_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        signing_key_id = UUID(d.pop("signing_key_id"))




        get_challenge_response_200_records_item_signature_type_0 = cls(
            signing_key_id=signing_key_id,
        )

        return get_challenge_response_200_records_item_signature_type_0

