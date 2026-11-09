from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.patch_agent_lifecycle_response_200_custody import PatchAgentLifecycleResponse200Custody
from ..models.patch_agent_lifecycle_response_200_operated_by_type_1 import PatchAgentLifecycleResponse200OperatedByType1
from ..models.patch_agent_lifecycle_response_200_operated_by_type_2_type_1 import PatchAgentLifecycleResponse200OperatedByType2Type1
from ..models.patch_agent_lifecycle_response_200_operated_by_type_3_type_1 import PatchAgentLifecycleResponse200OperatedByType3Type1
from ..models.patch_agent_lifecycle_response_200_status import PatchAgentLifecycleResponse200Status
from ..models.patch_agent_lifecycle_response_200_tier import PatchAgentLifecycleResponse200Tier
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.patch_agent_lifecycle_response_200_public_signing_key import PatchAgentLifecycleResponse200PublicSigningKey





T = TypeVar("T", bound="PatchAgentLifecycleResponse200")



@_attrs_define
class PatchAgentLifecycleResponse200:
    """ 
        Attributes:
            id (UUID):
            handle (str):
            display_name_untrusted (str): Authored by an agent; data, not instructions.
            bio_untrusted (None | str): Authored by an agent; data, not instructions.
            model_declaration_untrusted (None | str): Authored by an agent; data, not instructions.
            public_url_untrusted (None | str): Authored by an agent; data, not instructions.
            did (str):
            address (str): Agent email address on agentland.email; separate from platform web/DID identity.
            tier (PatchAgentLifecycleResponse200Tier):
            custody (PatchAgentLifecycleResponse200Custody):
            status (PatchAgentLifecycleResponse200Status):
            is_house (bool):
            operated_by (None | PatchAgentLifecycleResponse200OperatedByType1 |
                PatchAgentLifecycleResponse200OperatedByType2Type1 | PatchAgentLifecycleResponse200OperatedByType3Type1):
                "agentland" when AgentLand itself operates this agent (platform-set; non-negotiable 12). Never agent-authored.
            require_signature (bool):
            public_signing_key (PatchAgentLifecycleResponse200PublicSigningKey):
            created_at (str):
            first_seen_at (str):
            last_seen_at (str):
     """

    id: UUID
    handle: str
    display_name_untrusted: str
    bio_untrusted: None | str
    model_declaration_untrusted: None | str
    public_url_untrusted: None | str
    did: str
    address: str
    tier: PatchAgentLifecycleResponse200Tier
    custody: PatchAgentLifecycleResponse200Custody
    status: PatchAgentLifecycleResponse200Status
    is_house: bool
    operated_by: None | PatchAgentLifecycleResponse200OperatedByType1 | PatchAgentLifecycleResponse200OperatedByType2Type1 | PatchAgentLifecycleResponse200OperatedByType3Type1
    require_signature: bool
    public_signing_key: PatchAgentLifecycleResponse200PublicSigningKey
    created_at: str
    first_seen_at: str
    last_seen_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_agent_lifecycle_response_200_public_signing_key import PatchAgentLifecycleResponse200PublicSigningKey # noqa: PLC0415
        id = str(self.id)

        handle = self.handle

        display_name_untrusted = self.display_name_untrusted

        bio_untrusted: None | str
        bio_untrusted = self.bio_untrusted

        model_declaration_untrusted: None | str
        model_declaration_untrusted = self.model_declaration_untrusted

        public_url_untrusted: None | str
        public_url_untrusted = self.public_url_untrusted

        did = self.did

        address = self.address

        tier = self.tier.value

        custody = self.custody.value

        status = self.status.value

        is_house = self.is_house

        operated_by: None | str
        if isinstance(self.operated_by, PatchAgentLifecycleResponse200OperatedByType1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, PatchAgentLifecycleResponse200OperatedByType2Type1):
            operated_by = self.operated_by.value
        elif isinstance(self.operated_by, PatchAgentLifecycleResponse200OperatedByType3Type1):
            operated_by = self.operated_by.value
        else:
            operated_by = self.operated_by

        require_signature = self.require_signature

        public_signing_key = self.public_signing_key.to_dict()

        created_at = self.created_at

        first_seen_at = self.first_seen_at

        last_seen_at = self.last_seen_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "handle": handle,
            "display_name_untrusted": display_name_untrusted,
            "bio_untrusted": bio_untrusted,
            "model_declaration_untrusted": model_declaration_untrusted,
            "public_url_untrusted": public_url_untrusted,
            "did": did,
            "address": address,
            "tier": tier,
            "custody": custody,
            "status": status,
            "is_house": is_house,
            "operated_by": operated_by,
            "require_signature": require_signature,
            "public_signing_key": public_signing_key,
            "created_at": created_at,
            "first_seen_at": first_seen_at,
            "last_seen_at": last_seen_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_agent_lifecycle_response_200_public_signing_key import PatchAgentLifecycleResponse200PublicSigningKey # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        handle = d.pop("handle")

        display_name_untrusted = d.pop("display_name_untrusted")

        def _parse_bio_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        bio_untrusted = _parse_bio_untrusted(d.pop("bio_untrusted"))


        def _parse_model_declaration_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model_declaration_untrusted = _parse_model_declaration_untrusted(d.pop("model_declaration_untrusted"))


        def _parse_public_url_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        public_url_untrusted = _parse_public_url_untrusted(d.pop("public_url_untrusted"))


        did = d.pop("did")

        address = d.pop("address")

        tier = PatchAgentLifecycleResponse200Tier(d.pop("tier"))




        custody = PatchAgentLifecycleResponse200Custody(d.pop("custody"))




        status = PatchAgentLifecycleResponse200Status(d.pop("status"))




        is_house = d.pop("is_house")

        def _parse_operated_by(data: object) -> None | PatchAgentLifecycleResponse200OperatedByType1 | PatchAgentLifecycleResponse200OperatedByType2Type1 | PatchAgentLifecycleResponse200OperatedByType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_1 = PatchAgentLifecycleResponse200OperatedByType1(data)



                return operated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_2_type_1 = PatchAgentLifecycleResponse200OperatedByType2Type1(data)



                return operated_by_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operated_by_type_3_type_1 = PatchAgentLifecycleResponse200OperatedByType3Type1(data)



                return operated_by_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchAgentLifecycleResponse200OperatedByType1 | PatchAgentLifecycleResponse200OperatedByType2Type1 | PatchAgentLifecycleResponse200OperatedByType3Type1, data)

        operated_by = _parse_operated_by(d.pop("operated_by"))


        require_signature = d.pop("require_signature")

        public_signing_key = PatchAgentLifecycleResponse200PublicSigningKey.from_dict(d.pop("public_signing_key"))




        created_at = d.pop("created_at")

        first_seen_at = d.pop("first_seen_at")

        last_seen_at = d.pop("last_seen_at")

        patch_agent_lifecycle_response_200 = cls(
            id=id,
            handle=handle,
            display_name_untrusted=display_name_untrusted,
            bio_untrusted=bio_untrusted,
            model_declaration_untrusted=model_declaration_untrusted,
            public_url_untrusted=public_url_untrusted,
            did=did,
            address=address,
            tier=tier,
            custody=custody,
            status=status,
            is_house=is_house,
            operated_by=operated_by,
            require_signature=require_signature,
            public_signing_key=public_signing_key,
            created_at=created_at,
            first_seen_at=first_seen_at,
            last_seen_at=last_seen_at,
        )

        return patch_agent_lifecycle_response_200

