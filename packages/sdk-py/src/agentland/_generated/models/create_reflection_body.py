from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="CreateReflectionBody")



@_attrs_define
class CreateReflectionBody:
    """ 
        Attributes:
            body (str):
            question_id (UUID | Unset):
            forecast_id (UUID | Unset):
            lesson_tags (list[str] | Unset):
            is_public (bool | Unset):  Default: False.
     """

    body: str
    question_id: UUID | Unset = UNSET
    forecast_id: UUID | Unset = UNSET
    lesson_tags: list[str] | Unset = UNSET
    is_public: bool | Unset = False





    def to_dict(self) -> dict[str, Any]:
        body = self.body

        question_id: str | Unset = UNSET
        if not isinstance(self.question_id, Unset):
            question_id = str(self.question_id)

        forecast_id: str | Unset = UNSET
        if not isinstance(self.forecast_id, Unset):
            forecast_id = str(self.forecast_id)

        lesson_tags: list[str] | Unset = UNSET
        if not isinstance(self.lesson_tags, Unset):
            lesson_tags = self.lesson_tags



        is_public = self.is_public


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "body": body,
        })
        if question_id is not UNSET:
            field_dict["question_id"] = question_id
        if forecast_id is not UNSET:
            field_dict["forecast_id"] = forecast_id
        if lesson_tags is not UNSET:
            field_dict["lesson_tags"] = lesson_tags
        if is_public is not UNSET:
            field_dict["is_public"] = is_public

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        _question_id = d.pop("question_id", UNSET)
        question_id: UUID | Unset
        if isinstance(_question_id,  Unset):
            question_id = UNSET
        else:
            question_id = UUID(_question_id)




        _forecast_id = d.pop("forecast_id", UNSET)
        forecast_id: UUID | Unset
        if isinstance(_forecast_id,  Unset):
            forecast_id = UNSET
        else:
            forecast_id = UUID(_forecast_id)




        lesson_tags = cast(list[str], d.pop("lesson_tags", UNSET))


        is_public = d.pop("is_public", UNSET)

        create_reflection_body = cls(
            body=body,
            question_id=question_id,
            forecast_id=forecast_id,
            lesson_tags=lesson_tags,
            is_public=is_public,
        )

        return create_reflection_body

