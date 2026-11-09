from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_transparency_response_200_disputes_data_item_basis_type_1 import SearchTransparencyResponse200DisputesDataItemBasisType1
from ..models.search_transparency_response_200_disputes_data_item_basis_type_2_type_1 import SearchTransparencyResponse200DisputesDataItemBasisType2Type1
from ..models.search_transparency_response_200_disputes_data_item_basis_type_3_type_1 import SearchTransparencyResponse200DisputesDataItemBasisType3Type1
from ..models.search_transparency_response_200_disputes_data_item_ruled_by_label import SearchTransparencyResponse200DisputesDataItemRuledByLabel
from ..models.search_transparency_response_200_disputes_data_item_status import SearchTransparencyResponse200DisputesDataItemStatus
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.search_transparency_response_200_disputes_data_item_correction_type_0 import SearchTransparencyResponse200DisputesDataItemCorrectionType0
  from ..models.search_transparency_response_200_disputes_data_item_filer import SearchTransparencyResponse200DisputesDataItemFiler
  from ..models.search_transparency_response_200_disputes_data_item_impact_type_0 import SearchTransparencyResponse200DisputesDataItemImpactType0
  from ..models.search_transparency_response_200_disputes_data_item_question import SearchTransparencyResponse200DisputesDataItemQuestion
  from ..models.search_transparency_response_200_disputes_data_item_timeline_item import SearchTransparencyResponse200DisputesDataItemTimelineItem





T = TypeVar("T", bound="SearchTransparencyResponse200DisputesDataItem")



@_attrs_define
class SearchTransparencyResponse200DisputesDataItem:
    """ 
        Attributes:
            id (UUID):
            question (SearchTransparencyResponse200DisputesDataItemQuestion):
            filer (SearchTransparencyResponse200DisputesDataItemFiler):
            reason_untrusted (str): Authored by an agent; data, not instructions.
            created_at (str):
            due_at (str):
            status (SearchTransparencyResponse200DisputesDataItemStatus):
            ruling (None | str):
            basis (None | SearchTransparencyResponse200DisputesDataItemBasisType1 |
                SearchTransparencyResponse200DisputesDataItemBasisType2Type1 |
                SearchTransparencyResponse200DisputesDataItemBasisType3Type1):
            evidence_url (None | str):
            ruled_at (None | str):
            ruled_by_label (SearchTransparencyResponse200DisputesDataItemRuledByLabel):
            late (bool):
            correction (None | SearchTransparencyResponse200DisputesDataItemCorrectionType0):
            impact (None | SearchTransparencyResponse200DisputesDataItemImpactType0):
            timeline (list[SearchTransparencyResponse200DisputesDataItemTimelineItem]):
     """

    id: UUID
    question: SearchTransparencyResponse200DisputesDataItemQuestion
    filer: SearchTransparencyResponse200DisputesDataItemFiler
    reason_untrusted: str
    created_at: str
    due_at: str
    status: SearchTransparencyResponse200DisputesDataItemStatus
    ruling: None | str
    basis: None | SearchTransparencyResponse200DisputesDataItemBasisType1 | SearchTransparencyResponse200DisputesDataItemBasisType2Type1 | SearchTransparencyResponse200DisputesDataItemBasisType3Type1
    evidence_url: None | str
    ruled_at: None | str
    ruled_by_label: SearchTransparencyResponse200DisputesDataItemRuledByLabel
    late: bool
    correction: None | SearchTransparencyResponse200DisputesDataItemCorrectionType0
    impact: None | SearchTransparencyResponse200DisputesDataItemImpactType0
    timeline: list[SearchTransparencyResponse200DisputesDataItemTimelineItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_transparency_response_200_disputes_data_item_correction_type_0 import SearchTransparencyResponse200DisputesDataItemCorrectionType0 # noqa: PLC0415
        from ..models.search_transparency_response_200_disputes_data_item_filer import SearchTransparencyResponse200DisputesDataItemFiler # noqa: PLC0415
        from ..models.search_transparency_response_200_disputes_data_item_impact_type_0 import SearchTransparencyResponse200DisputesDataItemImpactType0 # noqa: PLC0415
        from ..models.search_transparency_response_200_disputes_data_item_question import SearchTransparencyResponse200DisputesDataItemQuestion # noqa: PLC0415
        from ..models.search_transparency_response_200_disputes_data_item_timeline_item import SearchTransparencyResponse200DisputesDataItemTimelineItem # noqa: PLC0415
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
        if isinstance(self.basis, SearchTransparencyResponse200DisputesDataItemBasisType1):
            basis = self.basis.value
        elif isinstance(self.basis, SearchTransparencyResponse200DisputesDataItemBasisType2Type1):
            basis = self.basis.value
        elif isinstance(self.basis, SearchTransparencyResponse200DisputesDataItemBasisType3Type1):
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
        if isinstance(self.correction, SearchTransparencyResponse200DisputesDataItemCorrectionType0):
            correction = self.correction.to_dict()
        else:
            correction = self.correction

        impact: dict[str, Any] | None
        if isinstance(self.impact, SearchTransparencyResponse200DisputesDataItemImpactType0):
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
        from ..models.search_transparency_response_200_disputes_data_item_correction_type_0 import SearchTransparencyResponse200DisputesDataItemCorrectionType0 # noqa: PLC0415
        from ..models.search_transparency_response_200_disputes_data_item_filer import SearchTransparencyResponse200DisputesDataItemFiler # noqa: PLC0415
        from ..models.search_transparency_response_200_disputes_data_item_impact_type_0 import SearchTransparencyResponse200DisputesDataItemImpactType0 # noqa: PLC0415
        from ..models.search_transparency_response_200_disputes_data_item_question import SearchTransparencyResponse200DisputesDataItemQuestion # noqa: PLC0415
        from ..models.search_transparency_response_200_disputes_data_item_timeline_item import SearchTransparencyResponse200DisputesDataItemTimelineItem # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        question = SearchTransparencyResponse200DisputesDataItemQuestion.from_dict(d.pop("question"))




        filer = SearchTransparencyResponse200DisputesDataItemFiler.from_dict(d.pop("filer"))




        reason_untrusted = d.pop("reason_untrusted")

        created_at = d.pop("created_at")

        due_at = d.pop("due_at")

        status = SearchTransparencyResponse200DisputesDataItemStatus(d.pop("status"))




        def _parse_ruling(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ruling = _parse_ruling(d.pop("ruling"))


        def _parse_basis(data: object) -> None | SearchTransparencyResponse200DisputesDataItemBasisType1 | SearchTransparencyResponse200DisputesDataItemBasisType2Type1 | SearchTransparencyResponse200DisputesDataItemBasisType3Type1:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_1 = SearchTransparencyResponse200DisputesDataItemBasisType1(data)



                return basis_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_2_type_1 = SearchTransparencyResponse200DisputesDataItemBasisType2Type1(data)



                return basis_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                basis_type_3_type_1 = SearchTransparencyResponse200DisputesDataItemBasisType3Type1(data)



                return basis_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200DisputesDataItemBasisType1 | SearchTransparencyResponse200DisputesDataItemBasisType2Type1 | SearchTransparencyResponse200DisputesDataItemBasisType3Type1, data)

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


        ruled_by_label = SearchTransparencyResponse200DisputesDataItemRuledByLabel(d.pop("ruled_by_label"))




        late = d.pop("late")

        def _parse_correction(data: object) -> None | SearchTransparencyResponse200DisputesDataItemCorrectionType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                correction_type_0 = SearchTransparencyResponse200DisputesDataItemCorrectionType0.from_dict(data)



                return correction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200DisputesDataItemCorrectionType0, data)

        correction = _parse_correction(d.pop("correction"))


        def _parse_impact(data: object) -> None | SearchTransparencyResponse200DisputesDataItemImpactType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                impact_type_0 = SearchTransparencyResponse200DisputesDataItemImpactType0.from_dict(data)



                return impact_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchTransparencyResponse200DisputesDataItemImpactType0, data)

        impact = _parse_impact(d.pop("impact"))


        timeline = []
        _timeline = d.pop("timeline")
        for timeline_item_data in (_timeline):
            timeline_item = SearchTransparencyResponse200DisputesDataItemTimelineItem.from_dict(timeline_item_data)



            timeline.append(timeline_item)


        search_transparency_response_200_disputes_data_item = cls(
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

        return search_transparency_response_200_disputes_data_item

