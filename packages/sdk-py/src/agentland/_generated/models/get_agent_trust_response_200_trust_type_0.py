from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_agent_trust_response_200_trust_type_0_components import GetAgentTrustResponse200TrustType0Components
  from ..models.get_agent_trust_response_200_trust_type_0_weights import GetAgentTrustResponse200TrustType0Weights





T = TypeVar("T", bound="GetAgentTrustResponse200TrustType0")



@_attrs_define
class GetAgentTrustResponse200TrustType0:
    """ 
        Attributes:
            score (float):
            components (GetAgentTrustResponse200TrustType0Components):
            weights (GetAgentTrustResponse200TrustType0Weights):
            version (str):
            computed_at (str):
     """

    score: float
    components: GetAgentTrustResponse200TrustType0Components
    weights: GetAgentTrustResponse200TrustType0Weights
    version: str
    computed_at: str





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_agent_trust_response_200_trust_type_0_components import GetAgentTrustResponse200TrustType0Components # noqa: PLC0415
        from ..models.get_agent_trust_response_200_trust_type_0_weights import GetAgentTrustResponse200TrustType0Weights # noqa: PLC0415
        score = self.score

        components = self.components.to_dict()

        weights = self.weights.to_dict()

        version = self.version

        computed_at = self.computed_at


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "score": score,
            "components": components,
            "weights": weights,
            "version": version,
            "computed_at": computed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_agent_trust_response_200_trust_type_0_components import GetAgentTrustResponse200TrustType0Components # noqa: PLC0415
        from ..models.get_agent_trust_response_200_trust_type_0_weights import GetAgentTrustResponse200TrustType0Weights # noqa: PLC0415
        d = dict(src_dict)
        score = d.pop("score")

        components = GetAgentTrustResponse200TrustType0Components.from_dict(d.pop("components"))




        weights = GetAgentTrustResponse200TrustType0Weights.from_dict(d.pop("weights"))




        version = d.pop("version")

        computed_at = d.pop("computed_at")

        get_agent_trust_response_200_trust_type_0 = cls(
            score=score,
            components=components,
            weights=weights,
            version=version,
            computed_at=computed_at,
        )

        return get_agent_trust_response_200_trust_type_0

