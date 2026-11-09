from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_record_response_200_agent import GetRecordResponse200Agent
  from ..models.get_record_response_200_challenge import GetRecordResponse200Challenge
  from ..models.get_record_response_200_daily_root_type_0 import GetRecordResponse200DailyRootType0
  from ..models.get_record_response_200_signature_type_0 import GetRecordResponse200SignatureType0





T = TypeVar("T", bound="GetRecordResponse200")



@_attrs_define
class GetRecordResponse200:
    """ 
        Attributes:
            id (UUID):
            challenge (GetRecordResponse200Challenge):
            agent (GetRecordResponse200Agent):
            previous_value (str):
            new_value (str):
            display_score (float | None):
            artifact_sha256 (str):
            spec_sha256 (str):
            verifier_image (str):
            submission_id (UUID):
            signature (GetRecordResponse200SignatureType0 | None):
            set_at (str):
            artifact_url (str):
            log_url (str):
            daily_root (GetRecordResponse200DailyRootType0 | None):
     """

    id: UUID
    challenge: GetRecordResponse200Challenge
    agent: GetRecordResponse200Agent
    previous_value: str
    new_value: str
    display_score: float | None
    artifact_sha256: str
    spec_sha256: str
    verifier_image: str
    submission_id: UUID
    signature: GetRecordResponse200SignatureType0 | None
    set_at: str
    artifact_url: str
    log_url: str
    daily_root: GetRecordResponse200DailyRootType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_record_response_200_agent import GetRecordResponse200Agent # noqa: PLC0415
        from ..models.get_record_response_200_challenge import GetRecordResponse200Challenge # noqa: PLC0415
        from ..models.get_record_response_200_daily_root_type_0 import GetRecordResponse200DailyRootType0 # noqa: PLC0415
        from ..models.get_record_response_200_signature_type_0 import GetRecordResponse200SignatureType0 # noqa: PLC0415
        id = str(self.id)

        challenge = self.challenge.to_dict()

        agent = self.agent.to_dict()

        previous_value = self.previous_value

        new_value = self.new_value

        display_score: float | None
        display_score = self.display_score

        artifact_sha256 = self.artifact_sha256

        spec_sha256 = self.spec_sha256

        verifier_image = self.verifier_image

        submission_id = str(self.submission_id)

        signature: dict[str, Any] | None
        if isinstance(self.signature, GetRecordResponse200SignatureType0):
            signature = self.signature.to_dict()
        else:
            signature = self.signature

        set_at = self.set_at

        artifact_url = self.artifact_url

        log_url = self.log_url

        daily_root: dict[str, Any] | None
        if isinstance(self.daily_root, GetRecordResponse200DailyRootType0):
            daily_root = self.daily_root.to_dict()
        else:
            daily_root = self.daily_root


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "challenge": challenge,
            "agent": agent,
            "previous_value": previous_value,
            "new_value": new_value,
            "display_score": display_score,
            "artifact_sha256": artifact_sha256,
            "spec_sha256": spec_sha256,
            "verifier_image": verifier_image,
            "submission_id": submission_id,
            "signature": signature,
            "set_at": set_at,
            "artifact_url": artifact_url,
            "log_url": log_url,
            "daily_root": daily_root,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_record_response_200_agent import GetRecordResponse200Agent # noqa: PLC0415
        from ..models.get_record_response_200_challenge import GetRecordResponse200Challenge # noqa: PLC0415
        from ..models.get_record_response_200_daily_root_type_0 import GetRecordResponse200DailyRootType0 # noqa: PLC0415
        from ..models.get_record_response_200_signature_type_0 import GetRecordResponse200SignatureType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        challenge = GetRecordResponse200Challenge.from_dict(d.pop("challenge"))




        agent = GetRecordResponse200Agent.from_dict(d.pop("agent"))




        previous_value = d.pop("previous_value")

        new_value = d.pop("new_value")

        def _parse_display_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        display_score = _parse_display_score(d.pop("display_score"))


        artifact_sha256 = d.pop("artifact_sha256")

        spec_sha256 = d.pop("spec_sha256")

        verifier_image = d.pop("verifier_image")

        submission_id = UUID(d.pop("submission_id"))




        def _parse_signature(data: object) -> GetRecordResponse200SignatureType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signature_type_0 = GetRecordResponse200SignatureType0.from_dict(data)



                return signature_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetRecordResponse200SignatureType0 | None, data)

        signature = _parse_signature(d.pop("signature"))


        set_at = d.pop("set_at")

        artifact_url = d.pop("artifact_url")

        log_url = d.pop("log_url")

        def _parse_daily_root(data: object) -> GetRecordResponse200DailyRootType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                daily_root_type_0 = GetRecordResponse200DailyRootType0.from_dict(data)



                return daily_root_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetRecordResponse200DailyRootType0 | None, data)

        daily_root = _parse_daily_root(d.pop("daily_root"))


        get_record_response_200 = cls(
            id=id,
            challenge=challenge,
            agent=agent,
            previous_value=previous_value,
            new_value=new_value,
            display_score=display_score,
            artifact_sha256=artifact_sha256,
            spec_sha256=spec_sha256,
            verifier_image=verifier_image,
            submission_id=submission_id,
            signature=signature,
            set_at=set_at,
            artifact_url=artifact_url,
            log_url=log_url,
            daily_root=daily_root,
        )

        return get_record_response_200

