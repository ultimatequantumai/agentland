from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_profile_response_200_trust_type_0_components import GetAgentProfileResponse200TrustType0Components





T = TypeVar("T", bound="GetAgentProfileResponse200TrustType0")



@_attrs_define
class GetAgentProfileResponse200TrustType0:
    """ 
        Attributes:
            score (float):
            components (GetAgentProfileResponse200TrustType0Components):
            version (str):
            computed_at (str):
     """

    score: float
    components: GetAgentProfileResponse200TrustType0Components
    version: str
    computed_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_profile_response_200_trust_type_0_components import GetAgentProfileResponse200TrustType0Components # noqa: PLC0415
        score = self.score

        components = self.components.to_dict()

        version = self.version

        computed_at = self.computed_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "score": score,
            "components": components,
            "version": version,
            "computed_at": computed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_profile_response_200_trust_type_0_components import GetAgentProfileResponse200TrustType0Components # noqa: PLC0415
        d = dict(src_dict)
        score = d.pop("score")

        components = GetAgentProfileResponse200TrustType0Components.from_dict(d.pop("components"))




        version = d.pop("version")

        computed_at = d.pop("computed_at")

        get_agent_profile_response_200_trust_type_0 = cls(
            score=score,
            components=components,
            version=version,
            computed_at=computed_at,
        )

        return get_agent_profile_response_200_trust_type_0

