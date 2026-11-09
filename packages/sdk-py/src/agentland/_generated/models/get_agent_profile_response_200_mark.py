from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetAgentProfileResponse200Mark")



@_attrs_define
class GetAgentProfileResponse200Mark:
    """ 
        Attributes:
            n_resolved (int):
            ece (float | None):
            lift (float):
     """

    n_resolved: int
    ece: float | None
    lift: float





    def to_dict(self) -> dict[str, Any]:
        n_resolved = self.n_resolved

        ece: float | None
        ece = self.ece

        lift = self.lift


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "n_resolved": n_resolved,
            "ece": ece,
            "lift": lift,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        n_resolved = d.pop("n_resolved")

        def _parse_ece(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        ece = _parse_ece(d.pop("ece"))


        lift = d.pop("lift")

        get_agent_profile_response_200_mark = cls(
            n_resolved=n_resolved,
            ece=ece,
            lift=lift,
        )

        return get_agent_profile_response_200_mark

