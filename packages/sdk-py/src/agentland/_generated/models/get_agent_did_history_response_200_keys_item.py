from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_did_history_response_200_keys_item_purpose import GetAgentDidHistoryResponse200KeysItemPurpose
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_did_history_response_200_keys_item_public_key_jwk import GetAgentDidHistoryResponse200KeysItemPublicKeyJwk





T = TypeVar("T", bound="GetAgentDidHistoryResponse200KeysItem")



@_attrs_define
class GetAgentDidHistoryResponse200KeysItem:
    """ 
        Attributes:
            id (str):
            public_key_jwk (GetAgentDidHistoryResponse200KeysItemPublicKeyJwk):
            purpose (GetAgentDidHistoryResponse200KeysItemPurpose):
            activated_at (str):
            revoked_at (str | Unset):
     """

    id: str
    public_key_jwk: GetAgentDidHistoryResponse200KeysItemPublicKeyJwk
    purpose: GetAgentDidHistoryResponse200KeysItemPurpose
    activated_at: str
    revoked_at: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_did_history_response_200_keys_item_public_key_jwk import GetAgentDidHistoryResponse200KeysItemPublicKeyJwk # noqa: PLC0415
        id = self.id

        public_key_jwk = self.public_key_jwk.to_dict()

        purpose = self.purpose.value

        activated_at = self.activated_at

        revoked_at = self.revoked_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "publicKeyJwk": public_key_jwk,
            "purpose": purpose,
            "activated_at": activated_at,
        })
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_did_history_response_200_keys_item_public_key_jwk import GetAgentDidHistoryResponse200KeysItemPublicKeyJwk # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        public_key_jwk = GetAgentDidHistoryResponse200KeysItemPublicKeyJwk.from_dict(d.pop("publicKeyJwk"))




        purpose = GetAgentDidHistoryResponse200KeysItemPurpose(d.pop("purpose"))




        activated_at = d.pop("activated_at")

        revoked_at = d.pop("revoked_at", UNSET)

        get_agent_did_history_response_200_keys_item = cls(
            id=id,
            public_key_jwk=public_key_jwk,
            purpose=purpose,
            activated_at=activated_at,
            revoked_at=revoked_at,
        )

        return get_agent_did_history_response_200_keys_item

