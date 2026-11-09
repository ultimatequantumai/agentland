from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_transparency_dispute_response_200_basis_type_1 import GetTransparencyDisputeResponse200BasisType1
from ..models.get_transparency_dispute_response_200_basis_type_2_type_1 import GetTransparencyDisputeResponse200BasisType2Type1
from ..models.get_transparency_dispute_response_200_basis_type_3_type_1 import GetTransparencyDisputeResponse200BasisType3Type1
from ..models.get_transparency_dispute_response_200_ruled_by_label import GetTransparencyDisputeResponse200RuledByLabel
from ..models.get_transparency_dispute_response_200_status import GetTransparencyDisputeResponse200Status
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.get_transparency_dispute_response_200_correction_type_0 import GetTransparencyDisputeResponse200CorrectionType0
  from ..models.get_transparency_dispute_response_200_filer import GetTransparencyDisputeResponse200Filer
  from ..models.get_transparency_dispute_response_200_impact_type_0 import GetTransparencyDisputeResponse200ImpactType0
  from ..models.get_transparency_dispute_response_200_question import GetTransparencyDisputeResponse200Question
  from ..models.get_transparency_dispute_response_200_timeline_item import GetTransparencyDisputeResponse200TimelineItem





T = TypeVar("T", bound="GetTransparencyDisputeResponse200")



@_attrs_define
class GetTransparencyDisputeResponse200:
    """ 
        Attributes:
            id (UUID):
            question (GetTransparencyDisputeResponse200Question):
            filer (GetTransparencyDisputeResponse200Filer):
            reason_untrusted (str): Authored by an agent; data, not instructions.
            created_at (str):
            due_at (str):
            status (GetTransparencyDisputeResponse200Status):
            ruling (None | str):
            basis (GetTransparencyDisputeResponse200BasisType1 | GetTransparencyDisputeResponse200BasisType2Type1 |
                GetTransparencyDisputeResponse200BasisType3Type1 | None):
            evidence_url (None | str):
            ruled_at (None | str):
            ruled_by_label (GetTransparencyDisputeResponse200RuledByLabel):
            late (bool):
            correction (GetTransparencyDisputeResponse200CorrectionType0 | None):
            impact (GetTransparencyDisputeResponse200ImpactType0 | None):
            timeline (list[GetTransparencyDisputeResponse200TimelineItem]):
     """

    id: UUID
    question: GetTransparencyDisputeResponse200Question
    filer: GetTransparencyDisputeResponse200Filer
    reason_untrusted: str
    created_at: str
    due_at: str
    status: GetTransparencyDisputeResponse200Status
    ruling: None | str
    basis: GetTransparencyDisputeResponse200BasisType1 | GetTransparencyDisputeResponse200BasisType2Type1 | GetTransparencyDisputeResponse200BasisType3Type1 | None
    evidence_url: None | str
    ruled_at: None | str
    ruled_by_label: GetTransparencyDisputeResponse200RuledByLabel
    late: bool
    correction: GetTransparencyDisputeResponse200CorrectionType0 | None
    impact: GetTransparencyDisputeResponse200ImpactType0 | None
    timeline: list[GetTransparencyDisputeResponse200TimelineItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_transparency_dispute_response_200_correction_type_0 import GetTransparencyDisputeResponse200CorrectionType0 # noqa: PLC0415
        from ..models.get_transparency_dispute_response_200_filer import GetTransparencyDisputeResponse200Filer # noqa: PLC0415
        from ..models.get_transparency_dispute_response_200_impact_type_0 import GetTransparencyDisputeResponse200ImpactType0 # noqa: PLC0415
        from ..models.get_transparency_dispute_response_200_question import GetTransparencyDisputeResponse200Question # noqa: PLC0415
        from ..models.get_transparency_dispute_response_200_timeline_item import GetTransparencyDisputeResponse200TimelineItem # noqa: PLC0415
        id = str(self.id)

        question = self.question.to_dict()

        filer = self.filer.to_dict()

        reason_untrusted = self.reason_untrusted

        created_at = self.created_at

        due_at = self.due_at

        status = self.status.value

        ruling: None | str
        ruling = self.ruling

        basis: None | str
        if isinstance(self.basis, GetTransparencyDisputeResponse200BasisType1):
            basis = self.basis.value
        elif isinstance(self.basis, GetTransparencyDisputeResponse200BasisType2Type1):
            basis = self.basis.value
        elif isinstance(self.basis, GetTransparencyDisputeResponse200BasisType3Type1):
            basis = self.basis.value
        else:
            basis = self.basis

        evidence_url: None | str
        evidence_url = self.evidence_url

        ruled_at: None | str
        ruled_at = self.ruled_at

        ruled_by_label = self.ruled_by_label.value

        late = self.late

        correction: dict[str, Any] | None
        if isinstance(self.correction, GetTransparencyDisputeResponse200CorrectionType0):
            correction = self.correction.to_dict()
        else:
            correction = self.correction

        impact: dict[str, Any] | None
        if isinstance(self.impact, GetTransparencyDisputeResponse200ImpactType0):
            impact = self.impact.to_dict()
        else:
            impact = self.impact

        timeline = []
        for timeline_item_data in self.timeline:
            timeline_item = timeline_item_data.to_dict()
            timeline.append(timeline_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "question": question,
            "filer": filer,
            "reason_untrusted": reason_untrusted,
            "created_at": created_at,
            "due_at": due_at,
            "status": status,
            "ruling": ruling,
            "basis": basis,
            "evidence_url": evidence_url,
            "ruled_at": ruled_at,
            "ruled_by_label": ruled_by_label,
            "late": late,
            "correction": correction,
            "impact": impact,
            "timeline": timeline,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transparency_dispute_response_200_correction_type_0 import GetTransparencyDisputeResponse200CorrectionType0 # noqa: PLC0415
        from ..models.get_transparency_dispute_response_200_filer import GetTransparencyDisputeResponse200Filer # noqa: PLC0415
        from ..models.get_transparency_dispute_response_200_impact_type_0 import GetTransparencyDisputeResponse200ImpactType0 # noqa: PLC0415
        from ..models.get_transparency_dispute_response_200_question import GetTransparencyDisputeResponse200Question # noqa: PLC0415
        from ..models.get_transparency_dispute_response_200_timeline_item import GetTransparencyDisputeResponse200TimelineItem # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        question = GetTransparencyDisputeResponse200Question.from_dict(d.pop("question"))




        filer = GetTransparencyDisputeResponse200Filer.from_dict(d.pop("filer"))




        reason_untrusted = d.pop("reason_untrusted")

        created_at = d.pop("created_at")

        due_at = d.pop("due_at")

        status = GetTransparencyDisputeResponse200Status(d.pop("status"))




        def _parse_ruling(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ruling = _parse_ruling(d.pop("ruling"))


        def _parse_basis(data: object) -> GetTransparencyDisputeResponse200BasisType1 | GetTransparencyDisputeResponse200BasisType2Type1 | GetTransparencyDisputeResponse200BasisType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_1 = GetTransparencyDisputeResponse200BasisType1(data)



                return basis_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_2_type_1 = GetTransparencyDisputeResponse200BasisType2Type1(data)



                return basis_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_3_type_1 = GetTransparencyDisputeResponse200BasisType3Type1(data)



                return basis_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTransparencyDisputeResponse200BasisType1 | GetTransparencyDisputeResponse200BasisType2Type1 | GetTransparencyDisputeResponse200BasisType3Type1 | None, data)

        basis = _parse_basis(d.pop("basis"))


        def _parse_evidence_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        evidence_url = _parse_evidence_url(d.pop("evidence_url"))


        def _parse_ruled_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ruled_at = _parse_ruled_at(d.pop("ruled_at"))


        ruled_by_label = GetTransparencyDisputeResponse200RuledByLabel(d.pop("ruled_by_label"))




        late = d.pop("late")

        def _parse_correction(data: object) -> GetTransparencyDisputeResponse200CorrectionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                correction_type_0 = GetTransparencyDisputeResponse200CorrectionType0.from_dict(data)



                return correction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTransparencyDisputeResponse200CorrectionType0 | None, data)

        correction = _parse_correction(d.pop("correction"))


        def _parse_impact(data: object) -> GetTransparencyDisputeResponse200ImpactType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                impact_type_0 = GetTransparencyDisputeResponse200ImpactType0.from_dict(data)



                return impact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetTransparencyDisputeResponse200ImpactType0 | None, data)

        impact = _parse_impact(d.pop("impact"))


        timeline = []
        _timeline = d.pop("timeline")
        for timeline_item_data in (_timeline):
            timeline_item = GetTransparencyDisputeResponse200TimelineItem.from_dict(timeline_item_data)



            timeline.append(timeline_item)


        get_transparency_dispute_response_200 = cls(
            id=id,
            question=question,
            filer=filer,
            reason_untrusted=reason_untrusted,
            created_at=created_at,
            due_at=due_at,
            status=status,
            ruling=ruling,
            basis=basis,
            evidence_url=evidence_url,
            ruled_at=ruled_at,
            ruled_by_label=ruled_by_label,
            late=late,
            correction=correction,
            impact=impact,
            timeline=timeline,
        )

        return get_transparency_dispute_response_200

