from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.submit_forecast_response_201_baseline_preview_type_0 import SubmitForecastResponse201BaselinePreviewType0
  from ..models.submit_forecast_response_201_distribution import SubmitForecastResponse201Distribution
  from ..models.submit_forecast_response_201_probabilities import SubmitForecastResponse201Probabilities
  from ..models.submit_forecast_response_201_question import SubmitForecastResponse201Question





T = TypeVar("T", bound="SubmitForecastResponse201")



@_attrs_define
class SubmitForecastResponse201:
    """ 
        Attributes:
            id (UUID):
            p (float | None):
            submitted_at (str):
            question (SubmitForecastResponse201Question):
            baseline_preview (None | SubmitForecastResponse201BaselinePreviewType0):
            probabilities (SubmitForecastResponse201Probabilities | Unset):
            distribution (SubmitForecastResponse201Distribution | Unset):
     """

    id: UUID
    p: float | None
    submitted_at: str
    question: SubmitForecastResponse201Question
    baseline_preview: None | SubmitForecastResponse201BaselinePreviewType0
    probabilities: SubmitForecastResponse201Probabilities | Unset = UNSET
    distribution: SubmitForecastResponse201Distribution | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_forecast_response_201_baseline_preview_type_0 import SubmitForecastResponse201BaselinePreviewType0 # noqa: PLC0415
        from ..models.submit_forecast_response_201_distribution import SubmitForecastResponse201Distribution # noqa: PLC0415
        from ..models.submit_forecast_response_201_probabilities import SubmitForecastResponse201Probabilities # noqa: PLC0415
        from ..models.submit_forecast_response_201_question import SubmitForecastResponse201Question # noqa: PLC0415
        id = str(self.id)

        p: float | None
        p = self.p

        submitted_at = self.submitted_at

        question = self.question.to_dict()

        baseline_preview: dict[str, Any] | None
        if isinstance(self.baseline_preview, SubmitForecastResponse201BaselinePreviewType0):
            baseline_preview = self.baseline_preview.to_dict()
        else:
            baseline_preview = self.baseline_preview

        probabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.probabilities, Unset):
            probabilities = self.probabilities.to_dict()

        distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "p": p,
            "submitted_at": submitted_at,
            "question": question,
            "baseline_preview": baseline_preview,
        })
        if probabilities is not UNSET:
            field_dict["probabilities"] = probabilities
        if distribution is not UNSET:
            field_dict["distribution"] = distribution

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_forecast_response_201_baseline_preview_type_0 import SubmitForecastResponse201BaselinePreviewType0 # noqa: PLC0415
        from ..models.submit_forecast_response_201_distribution import SubmitForecastResponse201Distribution # noqa: PLC0415
        from ..models.submit_forecast_response_201_probabilities import SubmitForecastResponse201Probabilities # noqa: PLC0415
        from ..models.submit_forecast_response_201_question import SubmitForecastResponse201Question # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        submitted_at = d.pop("submitted_at")

        question = SubmitForecastResponse201Question.from_dict(d.pop("question"))




        def _parse_baseline_preview(data: object) -> None | SubmitForecastResponse201BaselinePreviewType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                baseline_preview_type_0 = SubmitForecastResponse201BaselinePreviewType0.from_dict(data)



                return baseline_preview_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubmitForecastResponse201BaselinePreviewType0, data)

        baseline_preview = _parse_baseline_preview(d.pop("baseline_preview"))


        _probabilities = d.pop("probabilities", UNSET)
        probabilities: SubmitForecastResponse201Probabilities | Unset
        if isinstance(_probabilities,  Unset):
            probabilities = UNSET
        else:
            probabilities = SubmitForecastResponse201Probabilities.from_dict(_probabilities)




        _distribution = d.pop("distribution", UNSET)
        distribution: SubmitForecastResponse201Distribution | Unset
        if isinstance(_distribution,  Unset):
            distribution = UNSET
        else:
            distribution = SubmitForecastResponse201Distribution.from_dict(_distribution)




        submit_forecast_response_201 = cls(
            id=id,
            p=p,
            submitted_at=submitted_at,
            question=question,
            baseline_preview=baseline_preview,
            probabilities=probabilities,
            distribution=distribution,
        )

        return submit_forecast_response_201

