from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_challenge_records_response_200_data_item_agent import ListChallengeRecordsResponse200DataItemAgent
  from ..models.list_challenge_records_response_200_data_item_challenge import ListChallengeRecordsResponse200DataItemChallenge
  from ..models.list_challenge_records_response_200_data_item_daily_root_type_0 import ListChallengeRecordsResponse200DataItemDailyRootType0
  from ..models.list_challenge_records_response_200_data_item_signature_type_0 import ListChallengeRecordsResponse200DataItemSignatureType0





T = TypeVar("T", bound="ListChallengeRecordsResponse200DataItem")



@_attrs_define
class ListChallengeRecordsResponse200DataItem:
    """ 
        Attributes:
            id (UUID):
            challenge (ListChallengeRecordsResponse200DataItemChallenge):
            agent (ListChallengeRecordsResponse200DataItemAgent):
            previous_value (str):
            new_value (str):
            display_score (float | None):
            artifact_sha256 (str):
            spec_sha256 (str):
            verifier_image (str):
            submission_id (UUID):
            signature (ListChallengeRecordsResponse200DataItemSignatureType0 | None):
            set_at (str):
            artifact_url (str):
            log_url (str):
            daily_root (ListChallengeRecordsResponse200DataItemDailyRootType0 | None):
     """

    id: UUID
    challenge: ListChallengeRecordsResponse200DataItemChallenge
    agent: ListChallengeRecordsResponse200DataItemAgent
    previous_value: str
    new_value: str
    display_score: float | None
    artifact_sha256: str
    spec_sha256: str
    verifier_image: str
    submission_id: UUID
    signature: ListChallengeRecordsResponse200DataItemSignatureType0 | None
    set_at: str
    artifact_url: str
    log_url: str
    daily_root: ListChallengeRecordsResponse200DataItemDailyRootType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_challenge_records_response_200_data_item_agent import ListChallengeRecordsResponse200DataItemAgent # noqa: PLC0415
        from ..models.list_challenge_records_response_200_data_item_challenge import ListChallengeRecordsResponse200DataItemChallenge # noqa: PLC0415
        from ..models.list_challenge_records_response_200_data_item_daily_root_type_0 import ListChallengeRecordsResponse200DataItemDailyRootType0 # noqa: PLC0415
        from ..models.list_challenge_records_response_200_data_item_signature_type_0 import ListChallengeRecordsResponse200DataItemSignatureType0 # noqa: PLC0415
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
        if isinstance(self.signature, ListChallengeRecordsResponse200DataItemSignatureType0):
            signature = self.signature.to_dict()
        else:
            signature = self.signature

        set_at = self.set_at

        artifact_url = self.artifact_url

        log_url = self.log_url

        daily_root: dict[str, Any] | None
        if isinstance(self.daily_root, ListChallengeRecordsResponse200DataItemDailyRootType0):
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
        from ..models.list_challenge_records_response_200_data_item_agent import ListChallengeRecordsResponse200DataItemAgent # noqa: PLC0415
        from ..models.list_challenge_records_response_200_data_item_challenge import ListChallengeRecordsResponse200DataItemChallenge # noqa: PLC0415
        from ..models.list_challenge_records_response_200_data_item_daily_root_type_0 import ListChallengeRecordsResponse200DataItemDailyRootType0 # noqa: PLC0415
        from ..models.list_challenge_records_response_200_data_item_signature_type_0 import ListChallengeRecordsResponse200DataItemSignatureType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        challenge = ListChallengeRecordsResponse200DataItemChallenge.from_dict(d.pop("challenge"))




        agent = ListChallengeRecordsResponse200DataItemAgent.from_dict(d.pop("agent"))




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




        def _parse_signature(data: object) -> ListChallengeRecordsResponse200DataItemSignatureType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signature_type_0 = ListChallengeRecordsResponse200DataItemSignatureType0.from_dict(data)



                return signature_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListChallengeRecordsResponse200DataItemSignatureType0 | None, data)

        signature = _parse_signature(d.pop("signature"))


        set_at = d.pop("set_at")

        artifact_url = d.pop("artifact_url")

        log_url = d.pop("log_url")

        def _parse_daily_root(data: object) -> ListChallengeRecordsResponse200DataItemDailyRootType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                daily_root_type_0 = ListChallengeRecordsResponse200DataItemDailyRootType0.from_dict(data)



                return daily_root_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListChallengeRecordsResponse200DataItemDailyRootType0 | None, data)

        daily_root = _parse_daily_root(d.pop("daily_root"))


        list_challenge_records_response_200_data_item = cls(
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

        return list_challenge_records_response_200_data_item

