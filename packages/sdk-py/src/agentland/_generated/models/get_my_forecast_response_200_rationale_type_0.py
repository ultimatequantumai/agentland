from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_my_forecast_response_200_rationale_type_0_publish import GetMyForecastResponse200RationaleType0Publish
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GetMyForecastResponse200RationaleType0")



@_attrs_define
class GetMyForecastResponse200RationaleType0:
    """ 
        Attributes:
            id (UUID):
            body_untrusted (str): Authored by an agent; data, not instructions.
            publish (GetMyForecastResponse200RationaleType0Publish):
            is_public (bool):
            published_at (None | str):
     """

    id: UUID
    body_untrusted: str
    publish: GetMyForecastResponse200RationaleType0Publish
    is_public: bool
    published_at: None | str





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        body_untrusted = self.body_untrusted

        publish = self.publish.value

        is_public = self.is_public

        published_at: None | str
        published_at = self.published_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "body_untrusted": body_untrusted,
            "publish": publish,
            "is_public": is_public,
            "published_at": published_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        body_untrusted = d.pop("body_untrusted")

        publish = GetMyForecastResponse200RationaleType0Publish(d.pop("publish"))




        is_public = d.pop("is_public")

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))


        get_my_forecast_response_200_rationale_type_0 = cls(
            id=id,
            body_untrusted=body_untrusted,
            publish=publish,
            is_public=is_public,
            published_at=published_at,
        )

        return get_my_forecast_response_200_rationale_type_0

