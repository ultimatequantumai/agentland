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
  from ..models.list_questions_response_200_data_item_my_forecasts_item_distribution_type_0 import ListQuestionsResponse200DataItemMyForecastsItemDistributionType0
  from ..models.list_questions_response_200_data_item_my_forecasts_item_probabilities_type_0 import ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0





T = TypeVar("T", bound="ListQuestionsResponse200DataItemMyForecastsItem")



@_attrs_define
class ListQuestionsResponse200DataItemMyForecastsItem:
    """ 
        Attributes:
            id (UUID):
            p (float | None):
            submitted_at (str):
            probabilities (ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0 | None | Unset):
            distribution (ListQuestionsResponse200DataItemMyForecastsItemDistributionType0 | None | Unset):
     """

    id: UUID
    p: float | None
    submitted_at: str
    probabilities: ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0 | None | Unset = UNSET
    distribution: ListQuestionsResponse200DataItemMyForecastsItemDistributionType0 | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_questions_response_200_data_item_my_forecasts_item_distribution_type_0 import ListQuestionsResponse200DataItemMyForecastsItemDistributionType0 # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_my_forecasts_item_probabilities_type_0 import ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0 # noqa: PLC0415
        id = str(self.id)

        p: float | None
        p = self.p

        submitted_at = self.submitted_at

        probabilities: dict[str, Any] | None | Unset
        if isinstance(self.probabilities, Unset):
            probabilities = UNSET
        elif isinstance(self.probabilities, ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0):
            probabilities = self.probabilities.to_dict()
        else:
            probabilities = self.probabilities

        distribution: dict[str, Any] | None | Unset
        if isinstance(self.distribution, Unset):
            distribution = UNSET
        elif isinstance(self.distribution, ListQuestionsResponse200DataItemMyForecastsItemDistributionType0):
            distribution = self.distribution.to_dict()
        else:
            distribution = self.distribution


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "p": p,
            "submitted_at": submitted_at,
        })
        if probabilities is not UNSET:
            field_dict["probabilities"] = probabilities
        if distribution is not UNSET:
            field_dict["distribution"] = distribution

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_questions_response_200_data_item_my_forecasts_item_distribution_type_0 import ListQuestionsResponse200DataItemMyForecastsItemDistributionType0 # noqa: PLC0415
        from ..models.list_questions_response_200_data_item_my_forecasts_item_probabilities_type_0 import ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0 # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_p(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        p = _parse_p(d.pop("p"))


        submitted_at = d.pop("submitted_at")

        def _parse_probabilities(data: object) -> ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                probabilities_type_0 = ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0.from_dict(data)



                return probabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListQuestionsResponse200DataItemMyForecastsItemProbabilitiesType0 | None | Unset, data)

        probabilities = _parse_probabilities(d.pop("probabilities", UNSET))


        def _parse_distribution(data: object) -> ListQuestionsResponse200DataItemMyForecastsItemDistributionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                distribution_type_0 = ListQuestionsResponse200DataItemMyForecastsItemDistributionType0.from_dict(data)



                return distribution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListQuestionsResponse200DataItemMyForecastsItemDistributionType0 | None | Unset, data)

        distribution = _parse_distribution(d.pop("distribution", UNSET))


        list_questions_response_200_data_item_my_forecasts_item = cls(
            id=id,
            p=p,
            submitted_at=submitted_at,
            probabilities=probabilities,
            distribution=distribution,
        )

        return list_questions_response_200_data_item_my_forecasts_item

