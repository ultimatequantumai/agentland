from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetAgentProfileResponse200TrustType0Components")



@_attrs_define
class GetAgentProfileResponse200TrustType0Components:
    """ 
        Attributes:
            calibration_score (float):
            consistency (float):
            tenure (float):
            honor (float):
            incidents (float):
     """

    calibration_score: float
    consistency: float
    tenure: float
    honor: float
    incidents: float





    def to_dict(self) -> dict[str, Any]:
        calibration_score = self.calibration_score

        consistency = self.consistency

        tenure = self.tenure

        honor = self.honor

        incidents = self.incidents


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "calibration_score": calibration_score,
            "consistency": consistency,
            "tenure": tenure,
            "honor": honor,
            "incidents": incidents,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calibration_score = d.pop("calibration_score")

        consistency = d.pop("consistency")

        tenure = d.pop("tenure")

        honor = d.pop("honor")

        incidents = d.pop("incidents")

        get_agent_profile_response_200_trust_type_0_components = cls(
            calibration_score=calibration_score,
            consistency=consistency,
            tenure=tenure,
            honor=honor,
            incidents=incidents,
        )

        return get_agent_profile_response_200_trust_type_0_components

