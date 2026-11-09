from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_transparency_moderation_response_200_data_item_content_type_0_kind import ListTransparencyModerationResponse200DataItemContentType0Kind
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.list_transparency_moderation_response_200_data_item_content_type_0_question import ListTransparencyModerationResponse200DataItemContentType0Question





T = TypeVar("T", bound="ListTransparencyModerationResponse200DataItemContentType0")



@_attrs_define
class ListTransparencyModerationResponse200DataItemContentType0:
    """ 
        Attributes:
            kind (ListTransparencyModerationResponse200DataItemContentType0Kind):
            rationale_id (UUID):
            question (ListTransparencyModerationResponse200DataItemContentType0Question):
     """

    kind: ListTransparencyModerationResponse200DataItemContentType0Kind
    rationale_id: UUID
    question: ListTransparencyModerationResponse200DataItemContentType0Question





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_transparency_moderation_response_200_data_item_content_type_0_question import ListTransparencyModerationResponse200DataItemContentType0Question # noqa: PLC0415
        kind = self.kind.value

        rationale_id = str(self.rationale_id)

        question = self.question.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "kind": kind,
            "rationale_id": rationale_id,
            "question": question,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_transparency_moderation_response_200_data_item_content_type_0_question import ListTransparencyModerationResponse200DataItemContentType0Question # noqa: PLC0415
        d = dict(src_dict)
        kind = ListTransparencyModerationResponse200DataItemContentType0Kind(d.pop("kind"))




        rationale_id = UUID(d.pop("rationale_id"))




        question = ListTransparencyModerationResponse200DataItemContentType0Question.from_dict(d.pop("question"))




        list_transparency_moderation_response_200_data_item_content_type_0 = cls(
            kind=kind,
            rationale_id=rationale_id,
            question=question,
        )

        return list_transparency_moderation_response_200_data_item_content_type_0

