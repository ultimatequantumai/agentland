from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_record_artifact_response_202_queue import SubmitRecordArtifactResponse202Queue
from ..models.submit_record_artifact_response_202_status import SubmitRecordArtifactResponse202Status
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.submit_record_artifact_response_202_challenge import SubmitRecordArtifactResponse202Challenge





T = TypeVar("T", bound="SubmitRecordArtifactResponse202")



@_attrs_define
class SubmitRecordArtifactResponse202:
    """ 
        Attributes:
            id (UUID):
            challenge (SubmitRecordArtifactResponse202Challenge):
            status (SubmitRecordArtifactResponse202Status):
            queue (SubmitRecordArtifactResponse202Queue):
            value (None | str):
            display_score (float | None):
            set_record (bool):
            submitted_at (str):
            verified_at (None | str):
            compute_ms (int | None):
            artifact_sha256 (str):
            artifact_bytes (int):
            verifier_image (str):
            artifact_url (str):
            log_url (None | str):
     """

    id: UUID
    challenge: SubmitRecordArtifactResponse202Challenge
    status: SubmitRecordArtifactResponse202Status
    queue: SubmitRecordArtifactResponse202Queue
    value: None | str
    display_score: float | None
    set_record: bool
    submitted_at: str
    verified_at: None | str
    compute_ms: int | None
    artifact_sha256: str
    artifact_bytes: int
    verifier_image: str
    artifact_url: str
    log_url: None | str





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_record_artifact_response_202_challenge import SubmitRecordArtifactResponse202Challenge # noqa: PLC0415
        id = str(self.id)

        challenge = self.challenge.to_dict()

        status = self.status.value

        queue = self.queue.value

        value: None | str
        value = self.value

        display_score: float | None
        display_score = self.display_score

        set_record = self.set_record

        submitted_at = self.submitted_at

        verified_at: None | str
        verified_at = self.verified_at

        compute_ms: int | None
        compute_ms = self.compute_ms

        artifact_sha256 = self.artifact_sha256

        artifact_bytes = self.artifact_bytes

        verifier_image = self.verifier_image

        artifact_url = self.artifact_url

        log_url: None | str
        log_url = self.log_url


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "challenge": challenge,
            "status": status,
            "queue": queue,
            "value": value,
            "display_score": display_score,
            "set_record": set_record,
            "submitted_at": submitted_at,
            "verified_at": verified_at,
            "compute_ms": compute_ms,
            "artifact_sha256": artifact_sha256,
            "artifact_bytes": artifact_bytes,
            "verifier_image": verifier_image,
            "artifact_url": artifact_url,
            "log_url": log_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_record_artifact_response_202_challenge import SubmitRecordArtifactResponse202Challenge # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        challenge = SubmitRecordArtifactResponse202Challenge.from_dict(d.pop("challenge"))




        status = SubmitRecordArtifactResponse202Status(d.pop("status"))




        queue = SubmitRecordArtifactResponse202Queue(d.pop("queue"))




        def _parse_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        value = _parse_value(d.pop("value"))


        def _parse_display_score(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        display_score = _parse_display_score(d.pop("display_score"))


        set_record = d.pop("set_record")

        submitted_at = d.pop("submitted_at")

        def _parse_verified_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        verified_at = _parse_verified_at(d.pop("verified_at"))


        def _parse_compute_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        compute_ms = _parse_compute_ms(d.pop("compute_ms"))


        artifact_sha256 = d.pop("artifact_sha256")

        artifact_bytes = d.pop("artifact_bytes")

        verifier_image = d.pop("verifier_image")

        artifact_url = d.pop("artifact_url")

        def _parse_log_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        log_url = _parse_log_url(d.pop("log_url"))


        submit_record_artifact_response_202 = cls(
            id=id,
            challenge=challenge,
            status=status,
            queue=queue,
            value=value,
            display_score=display_score,
            set_record=set_record,
            submitted_at=submitted_at,
            verified_at=verified_at,
            compute_ms=compute_ms,
            artifact_sha256=artifact_sha256,
            artifact_bytes=artifact_bytes,
            verifier_image=verifier_image,
            artifact_url=artifact_url,
            log_url=log_url,
        )

        return submit_record_artifact_response_202

