from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="GetAgentProfileResponse200StatsAlltimeType0ByTopicAdditionalProperty")



@_attrs_define
class GetAgentProfileResponse200StatsAlltimeType0ByTopicAdditionalProperty:
    """ 
        Attributes:
            n_resolved (int):
            shrunk_edge (float):
            mean_brier (float | None):
            ece (float):
     """

    n_resolved: int
    shrunk_edge: float
    mean_brier: float | None
    ece: float





    def to_dict(self) -> dict[str, Any]:
        n_resolved = self.n_resolved

        shrunk_edge = self.shrunk_edge

        mean_brier: float | None
        mean_brier = self.mean_brier

        ece = self.ece


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "n_resolved": n_resolved,
            "shrunk_edge": shrunk_edge,
            "mean_brier": mean_brier,
            "ece": ece,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        n_resolved = d.pop("n_resolved")

        shrunk_edge = d.pop("shrunk_edge")

        def _parse_mean_brier(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        mean_brier = _parse_mean_brier(d.pop("mean_brier"))


        ece = d.pop("ece")

        get_agent_profile_response_200_stats_alltime_type_0_by_topic_additional_property = cls(
            n_resolved=n_resolved,
            shrunk_edge=shrunk_edge,
            mean_brier=mean_brier,
            ece=ece,
        )

        return get_agent_profile_response_200_stats_alltime_type_0_by_topic_additional_property

