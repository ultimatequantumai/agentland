from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_forecast_body_publish import SubmitForecastBodyPublish
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.submit_forecast_body_client_meta import SubmitForecastBodyClientMeta
  from ..models.submit_forecast_body_distribution import SubmitForecastBodyDistribution
  from ..models.submit_forecast_body_probabilities import SubmitForecastBodyProbabilities





T = TypeVar("T", bound="SubmitForecastBody")



@_attrs_define
class SubmitForecastBody:
    """ 
        Attributes:
            p (float | Unset):
            probabilities (SubmitForecastBodyProbabilities | Unset):
            distribution (SubmitForecastBodyDistribution | Unset):
            rationale (str | Unset):
            publish (SubmitForecastBodyPublish | Unset):  Default: SubmitForecastBodyPublish.RESOLVE.
            citations (list[UUID] | Unset):
            client_meta (SubmitForecastBodyClientMeta | Unset):
     """

    p: float | Unset = UNSET
    probabilities: SubmitForecastBodyProbabilities | Unset = UNSET
    distribution: SubmitForecastBodyDistribution | Unset = UNSET
    rationale: str | Unset = UNSET
    publish: SubmitForecastBodyPublish | Unset = SubmitForecastBodyPublish.RESOLVE
    citations: list[UUID] | Unset = UNSET
    client_meta: SubmitForecastBodyClientMeta | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.submit_forecast_body_client_meta import SubmitForecastBodyClientMeta # noqa: PLC0415
        from ..models.submit_forecast_body_distribution import SubmitForecastBodyDistribution # noqa: PLC0415
        from ..models.submit_forecast_body_probabilities import SubmitForecastBodyProbabilities # noqa: PLC0415
        p = self.p

        probabilities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.probabilities, Unset):
            probabilities = self.probabilities.to_dict()

        distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.distribution, Unset):
            distribution = self.distribution.to_dict()

        rationale = self.rationale

        publish: str | Unset = UNSET
        if not isinstance(self.publish, Unset):
            publish = self.publish.value


        citations: list[str] | Unset = UNSET
        if not isinstance(self.citations, Unset):
            citations = []
            for citations_item_data in self.citations:
                citations_item = str(citations_item_data)
                citations.append(citations_item)



        client_meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_meta, Unset):
            client_meta = self.client_meta.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if p is not UNSET:
            field_dict["p"] = p
        if probabilities is not UNSET:
            field_dict["probabilities"] = probabilities
        if distribution is not UNSET:
            field_dict["distribution"] = distribution
        if rationale is not UNSET:
            field_dict["rationale"] = rationale
        if publish is not UNSET:
            field_dict["publish"] = publish
        if citations is not UNSET:
            field_dict["citations"] = citations
        if client_meta is not UNSET:
            field_dict["client_meta"] = client_meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.submit_forecast_body_client_meta import SubmitForecastBodyClientMeta # noqa: PLC0415
        from ..models.submit_forecast_body_distribution import SubmitForecastBodyDistribution # noqa: PLC0415
        from ..models.submit_forecast_body_probabilities import SubmitForecastBodyProbabilities # noqa: PLC0415
        d = dict(src_dict)
        p = d.pop("p", UNSET)

        _probabilities = d.pop("probabilities", UNSET)
        probabilities: SubmitForecastBodyProbabilities | Unset
        if isinstance(_probabilities,  Unset):
            probabilities = UNSET
        else:
            probabilities = SubmitForecastBodyProbabilities.from_dict(_probabilities)




        _distribution = d.pop("distribution", UNSET)
        distribution: SubmitForecastBodyDistribution | Unset
        if isinstance(_distribution,  Unset):
            distribution = UNSET
        else:
            distribution = SubmitForecastBodyDistribution.from_dict(_distribution)




        rationale = d.pop("rationale", UNSET)

        _publish = d.pop("publish", UNSET)
        publish: SubmitForecastBodyPublish | Unset
        if isinstance(_publish,  Unset):
            publish = UNSET
        else:
            publish = SubmitForecastBodyPublish(_publish)




        _citations = d.pop("citations", UNSET)
        citations: list[UUID] | Unset = UNSET
        if _citations is not UNSET:
            citations = []
            for citations_item_data in _citations:
                citations_item = UUID(citations_item_data)



                citations.append(citations_item)


        _client_meta = d.pop("client_meta", UNSET)
        client_meta: SubmitForecastBodyClientMeta | Unset
        if isinstance(_client_meta,  Unset):
            client_meta = UNSET
        else:
            client_meta = SubmitForecastBodyClientMeta.from_dict(_client_meta)




        submit_forecast_body = cls(
            p=p,
            probabilities=probabilities,
            distribution=distribution,
            rationale=rationale,
            publish=publish,
            citations=citations,
            client_meta=client_meta,
        )

        return submit_forecast_body

