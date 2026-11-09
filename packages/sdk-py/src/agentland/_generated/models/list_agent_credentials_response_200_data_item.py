from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_agent_credentials_response_200_data_item_revocation_reason import ListAgentCredentialsResponse200DataItemRevocationReason
from ..models.list_agent_credentials_response_200_data_item_type import ListAgentCredentialsResponse200DataItemType
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_agent_credentials_response_200_data_item_evidence import ListAgentCredentialsResponse200DataItemEvidence





T = TypeVar("T", bound="ListAgentCredentialsResponse200DataItem")



@_attrs_define
class ListAgentCredentialsResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            type_ (ListAgentCredentialsResponse200DataItemType):
            scope_label (str):
            issued_at (str):
            revoked_at (None | str):
            revocation_reason (ListAgentCredentialsResponse200DataItemRevocationReason):
            evidence (ListAgentCredentialsResponse200DataItemEvidence):
            vc (str):
     """

    id: UUID
    type_: ListAgentCredentialsResponse200DataItemType
    scope_label: str
    issued_at: str
    revoked_at: None | str
    revocation_reason: ListAgentCredentialsResponse200DataItemRevocationReason
    evidence: ListAgentCredentialsResponse200DataItemEvidence
    vc: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_agent_credentials_response_200_data_item_evidence import ListAgentCredentialsResponse200DataItemEvidence # noqa: PLC0415
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
        from ..models.list_agent_credentials_response_200_data_item_evidence import ListAgentCredentialsResponse200DataItemEvidence # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        type_ = ListAgentCredentialsResponse200DataItemType(d.pop("type"))




        scope_label = d.pop("scope_label")

        issued_at = d.pop("issued_at")

        def _parse_revoked_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at"))


        revocation_reason = ListAgentCredentialsResponse200DataItemRevocationReason(d.pop("revocation_reason"))




        evidence = ListAgentCredentialsResponse200DataItemEvidence.from_dict(d.pop("evidence"))




        vc = d.pop("vc")

        list_agent_credentials_response_200_data_item = cls(
            id=id,
            type_=type_,
            scope_label=scope_label,
            issued_at=issued_at,
            revoked_at=revoked_at,
            revocation_reason=revocation_reason,
            evidence=evidence,
            vc=vc,
        )

        return list_agent_credentials_response_200_data_item

