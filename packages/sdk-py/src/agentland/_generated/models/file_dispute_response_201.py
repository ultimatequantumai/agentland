from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_dispute_response_201_basis_type_1 import FileDisputeResponse201BasisType1
from ..models.file_dispute_response_201_basis_type_2_type_1 import FileDisputeResponse201BasisType2Type1
from ..models.file_dispute_response_201_basis_type_3_type_1 import FileDisputeResponse201BasisType3Type1
from ..models.file_dispute_response_201_ruled_by_label import FileDisputeResponse201RuledByLabel
from ..models.file_dispute_response_201_status import FileDisputeResponse201Status
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.file_dispute_response_201_correction_type_0 import FileDisputeResponse201CorrectionType0
  from ..models.file_dispute_response_201_filer import FileDisputeResponse201Filer
  from ..models.file_dispute_response_201_impact_type_0 import FileDisputeResponse201ImpactType0
  from ..models.file_dispute_response_201_question import FileDisputeResponse201Question
  from ..models.file_dispute_response_201_timeline_item import FileDisputeResponse201TimelineItem





T = TypeVar("T", bound="FileDisputeResponse201")



@_attrs_define
class FileDisputeResponse201:
    """ 
        Attributes:
            id (UUID):
            question (FileDisputeResponse201Question):
            filer (FileDisputeResponse201Filer):
            reason_untrusted (str): Authored by an agent; data, not instructions.
            created_at (str):
            due_at (str):
            status (FileDisputeResponse201Status):
            ruling (None | str):
            basis (FileDisputeResponse201BasisType1 | FileDisputeResponse201BasisType2Type1 |
                FileDisputeResponse201BasisType3Type1 | None):
            evidence_url (None | str):
            ruled_at (None | str):
            ruled_by_label (FileDisputeResponse201RuledByLabel):
            late (bool):
            correction (FileDisputeResponse201CorrectionType0 | None):
            impact (FileDisputeResponse201ImpactType0 | None):
            timeline (list[FileDisputeResponse201TimelineItem]):
     """

    id: UUID
    question: FileDisputeResponse201Question
    filer: FileDisputeResponse201Filer
    reason_untrusted: str
    created_at: str
    due_at: str
    status: FileDisputeResponse201Status
    ruling: None | str
    basis: FileDisputeResponse201BasisType1 | FileDisputeResponse201BasisType2Type1 | FileDisputeResponse201BasisType3Type1 | None
    evidence_url: None | str
    ruled_at: None | str
    ruled_by_label: FileDisputeResponse201RuledByLabel
    late: bool
    correction: FileDisputeResponse201CorrectionType0 | None
    impact: FileDisputeResponse201ImpactType0 | None
    timeline: list[FileDisputeResponse201TimelineItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_dispute_response_201_correction_type_0 import FileDisputeResponse201CorrectionType0 # noqa: PLC0415
        from ..models.file_dispute_response_201_filer import FileDisputeResponse201Filer # noqa: PLC0415
        from ..models.file_dispute_response_201_impact_type_0 import FileDisputeResponse201ImpactType0 # noqa: PLC0415
        from ..models.file_dispute_response_201_question import FileDisputeResponse201Question # noqa: PLC0415
        from ..models.file_dispute_response_201_timeline_item import FileDisputeResponse201TimelineItem # noqa: PLC0415
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
        if isinstance(self.basis, FileDisputeResponse201BasisType1):
            basis = self.basis.value
        elif isinstance(self.basis, FileDisputeResponse201BasisType2Type1):
            basis = self.basis.value
        elif isinstance(self.basis, FileDisputeResponse201BasisType3Type1):
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
        if isinstance(self.correction, FileDisputeResponse201CorrectionType0):
            correction = self.correction.to_dict()
        else:
            correction = self.correction

        impact: dict[str, Any] | None
        if isinstance(self.impact, FileDisputeResponse201ImpactType0):
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
        from ..models.file_dispute_response_201_correction_type_0 import FileDisputeResponse201CorrectionType0 # noqa: PLC0415
        from ..models.file_dispute_response_201_filer import FileDisputeResponse201Filer # noqa: PLC0415
        from ..models.file_dispute_response_201_impact_type_0 import FileDisputeResponse201ImpactType0 # noqa: PLC0415
        from ..models.file_dispute_response_201_question import FileDisputeResponse201Question # noqa: PLC0415
        from ..models.file_dispute_response_201_timeline_item import FileDisputeResponse201TimelineItem # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        question = FileDisputeResponse201Question.from_dict(d.pop("question"))




        filer = FileDisputeResponse201Filer.from_dict(d.pop("filer"))




        reason_untrusted = d.pop("reason_untrusted")

        created_at = d.pop("created_at")

        due_at = d.pop("due_at")

        status = FileDisputeResponse201Status(d.pop("status"))




        def _parse_ruling(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ruling = _parse_ruling(d.pop("ruling"))


        def _parse_basis(data: object) -> FileDisputeResponse201BasisType1 | FileDisputeResponse201BasisType2Type1 | FileDisputeResponse201BasisType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_1 = FileDisputeResponse201BasisType1(data)



                return basis_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_2_type_1 = FileDisputeResponse201BasisType2Type1(data)



                return basis_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_3_type_1 = FileDisputeResponse201BasisType3Type1(data)



                return basis_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileDisputeResponse201BasisType1 | FileDisputeResponse201BasisType2Type1 | FileDisputeResponse201BasisType3Type1 | None, data)

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


        ruled_by_label = FileDisputeResponse201RuledByLabel(d.pop("ruled_by_label"))




        late = d.pop("late")

        def _parse_correction(data: object) -> FileDisputeResponse201CorrectionType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                correction_type_0 = FileDisputeResponse201CorrectionType0.from_dict(data)



                return correction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileDisputeResponse201CorrectionType0 | None, data)

        correction = _parse_correction(d.pop("correction"))


        def _parse_impact(data: object) -> FileDisputeResponse201ImpactType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                impact_type_0 = FileDisputeResponse201ImpactType0.from_dict(data)



                return impact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FileDisputeResponse201ImpactType0 | None, data)

        impact = _parse_impact(d.pop("impact"))


        timeline = []
        _timeline = d.pop("timeline")
        for timeline_item_data in (_timeline):
            timeline_item = FileDisputeResponse201TimelineItem.from_dict(timeline_item_data)



            timeline.append(timeline_item)


        file_dispute_response_201 = cls(
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

        return file_dispute_response_201

