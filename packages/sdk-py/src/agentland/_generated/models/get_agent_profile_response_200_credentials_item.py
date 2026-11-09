from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_agent_profile_response_200_credentials_item_revocation_reason import GetAgentProfileResponse200CredentialsItemRevocationReason
from ..models.get_agent_profile_response_200_credentials_item_type import GetAgentProfileResponse200CredentialsItemType
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_agent_profile_response_200_credentials_item_evidence import GetAgentProfileResponse200CredentialsItemEvidence





T = TypeVar("T", bound="GetAgentProfileResponse200CredentialsItem")



@_attrs_define
class GetAgentProfileResponse200CredentialsItem:
    """ 
        Attributes:
            id (UUID):
            type_ (GetAgentProfileResponse200CredentialsItemType):
            scope_label (str):
            issued_at (str):
            revoked_at (None | str):
            revocation_reason (GetAgentProfileResponse200CredentialsItemRevocationReason):
            evidence (GetAgentProfileResponse200CredentialsItemEvidence):
            vc (str):
     """

    id: UUID
    type_: GetAgentProfileResponse200CredentialsItemType
    scope_label: str
    issued_at: str
    revoked_at: None | str
    revocation_reason: GetAgentProfileResponse200CredentialsItemRevocationReason
    evidence: GetAgentProfileResponse200CredentialsItemEvidence
    vc: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_profile_response_200_credentials_item_evidence import GetAgentProfileResponse200CredentialsItemEvidence # noqa: PLC0415
        id = str(self.id)

        type_ = self.type_.value

        scope_label = self.scope_label

        issued_at = self.issued_at

        revoked_at: None | str
        revoked_at = self.revoked_at

        revocation_reason = self.revocation_reason.value

        evidence = self.evidence.to_dict()

        vc = self.vc


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "type": type_,
            "scope_label": scope_label,
            "issued_at": issued_at,
            "revoked_at": revoked_at,
            "revocation_reason": revocation_reason,
            "evidence": evidence,
            "vc": vc,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_profile_response_200_credentials_item_evidence import GetAgentProfileResponse200CredentialsItemEvidence # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        type_ = GetAgentProfileResponse200CredentialsItemType(d.pop("type"))




        scope_label = d.pop("scope_label")

        issued_at = d.pop("issued_at")

        def _parse_revoked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))


        revocation_reason = GetAgentProfileResponse200CredentialsItemRevocationReason(d.pop("revocation_reason"))




        evidence = GetAgentProfileResponse200CredentialsItemEvidence.from_dict(d.pop("evidence"))




        vc = d.pop("vc")

        get_agent_profile_response_200_credentials_item = cls(
            id=id,
            type_=type_,
            scope_label=scope_label,
            issued_at=issued_at,
            revoked_at=revoked_at,
            revocation_reason=revocation_reason,
            evidence=evidence,
            vc=vc,
        )

        return get_agent_profile_response_200_credentials_item

