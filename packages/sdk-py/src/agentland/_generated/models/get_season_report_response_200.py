from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_season_report_response_200_by_horizon_item import GetSeasonReportResponse200ByHorizonItem
  from ..models.get_season_report_response_200_figures import GetSeasonReportResponse200Figures
  from ..models.get_season_report_response_200_method import GetSeasonReportResponse200Method
  from ..models.get_season_report_response_200_season import GetSeasonReportResponse200Season
  from ..models.get_season_report_response_200_withheld_item import GetSeasonReportResponse200WithheldItem





T = TypeVar("T", bound="GetSeasonReportResponse200")



@_attrs_define
class GetSeasonReportResponse200:
    """ 
        Attributes:
            key (str):
            season (GetSeasonReportResponse200Season):
            as_of (str):
            published_at (None | str):
            scoring_versions (list[str]):
            method (GetSeasonReportResponse200Method):
            figures (GetSeasonReportResponse200Figures):
            by_horizon (list[GetSeasonReportResponse200ByHorizonItem]):
            withheld (list[GetSeasonReportResponse200WithheldItem]):
     """

    key: str
    season: GetSeasonReportResponse200Season
    as_of: str
    published_at: None | str
    scoring_versions: list[str]
    method: GetSeasonReportResponse200Method
    figures: GetSeasonReportResponse200Figures
    by_horizon: list[GetSeasonReportResponse200ByHorizonItem]
    withheld: list[GetSeasonReportResponse200WithheldItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_season_report_response_200_by_horizon_item import GetSeasonReportResponse200ByHorizonItem # noqa: PLC0415
        from ..models.get_season_report_response_200_figures import GetSeasonReportResponse200Figures # noqa: PLC0415
        from ..models.get_season_report_response_200_method import GetSeasonReportResponse200Method # noqa: PLC0415
        from ..models.get_season_report_response_200_season import GetSeasonReportResponse200Season # noqa: PLC0415
        from ..models.get_season_report_response_200_withheld_item import GetSeasonReportResponse200WithheldItem # noqa: PLC0415
        key = self.key

        season = self.season.to_dict()

        as_of = self.as_of

        published_at: None | str
        published_at = self.published_at

        scoring_versions = self.scoring_versions



        method = self.method.to_dict()

        figures = self.figures.to_dict()

        by_horizon = []
        for by_horizon_item_data in self.by_horizon:
            by_horizon_item = by_horizon_item_data.to_dict()
            by_horizon.append(by_horizon_item)



        withheld = []
        for withheld_item_data in self.withheld:
            withheld_item = withheld_item_data.to_dict()
            withheld.append(withheld_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "key": key,
            "season": season,
            "as_of": as_of,
            "published_at": published_at,
            "scoring_versions": scoring_versions,
            "method": method,
            "figures": figures,
            "by_horizon": by_horizon,
            "withheld": withheld,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_season_report_response_200_by_horizon_item import GetSeasonReportResponse200ByHorizonItem # noqa: PLC0415
        from ..models.get_season_report_response_200_figures import GetSeasonReportResponse200Figures # noqa: PLC0415
        from ..models.get_season_report_response_200_method import GetSeasonReportResponse200Method # noqa: PLC0415
        from ..models.get_season_report_response_200_season import GetSeasonReportResponse200Season # noqa: PLC0415
        from ..models.get_season_report_response_200_withheld_item import GetSeasonReportResponse200WithheldItem # noqa: PLC0415
        d = dict(src_dict)
        key = d.pop("key")

        season = GetSeasonReportResponse200Season.from_dict(d.pop("season"))




        as_of = d.pop("as_of")

        def _parse_published_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        published_at = _parse_published_at(d.pop("published_at"))


        scoring_versions = cast(list[str], d.pop("scoring_versions"))


        method = GetSeasonReportResponse200Method.from_dict(d.pop("method"))




        figures = GetSeasonReportResponse200Figures.from_dict(d.pop("figures"))




        by_horizon = []
        _by_horizon = d.pop("by_horizon")
        for by_horizon_item_data in (_by_horizon):
            by_horizon_item = GetSeasonReportResponse200ByHorizonItem.from_dict(by_horizon_item_data)



            by_horizon.append(by_horizon_item)


        withheld = []
        _withheld = d.pop("withheld")
        for withheld_item_data in (_withheld):
            withheld_item = GetSeasonReportResponse200WithheldItem.from_dict(withheld_item_data)



            withheld.append(withheld_item)


        get_season_report_response_200 = cls(
            key=key,
            season=season,
            as_of=as_of,
            published_at=published_at,
            scoring_versions=scoring_versions,
            method=method,
            figures=figures,
            by_horizon=by_horizon,
            withheld=withheld,
        )

        return get_season_report_response_200

