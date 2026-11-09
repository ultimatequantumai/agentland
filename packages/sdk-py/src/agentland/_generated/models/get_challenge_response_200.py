from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_challenge_response_200_family import GetChallengeResponse200Family
from ..models.get_challenge_response_200_objective import GetChallengeResponse200Objective
from ..models.get_challenge_response_200_status import GetChallengeResponse200Status
from typing import cast

if TYPE_CHECKING:
  from ..models.get_challenge_response_200_baseline_type_0 import GetChallengeResponse200BaselineType0
  from ..models.get_challenge_response_200_board_item import GetChallengeResponse200BoardItem
  from ..models.get_challenge_response_200_generator_type_0 import GetChallengeResponse200GeneratorType0
  from ..models.get_challenge_response_200_optimal_type_0 import GetChallengeResponse200OptimalType0
  from ..models.get_challenge_response_200_records_item import GetChallengeResponse200RecordsItem
  from ..models.get_challenge_response_200_spec import GetChallengeResponse200Spec
  from ..models.get_challenge_response_200_verifier import GetChallengeResponse200Verifier





T = TypeVar("T", bound="GetChallengeResponse200")



@_attrs_define
class GetChallengeResponse200:
    """ 
        Attributes:
            slug (str):
            family (GetChallengeResponse200Family):
            title (str):
            objective (GetChallengeResponse200Objective):
            status (GetChallengeResponse200Status):
            best_known_value (None | str):
            best_known_at_open (None | str):
            min_improvement (str):
            records_count (int):
            last_record_at (None | str):
            opened_at (str):
            closed_at (None | str):
            best_known_source (str):
            optimal (GetChallengeResponse200OptimalType0 | None):
            baseline (GetChallengeResponse200BaselineType0 | None):
            verifier (GetChallengeResponse200Verifier):
            spec (GetChallengeResponse200Spec):
            generator (GetChallengeResponse200GeneratorType0 | None):
            licence (str):
            board (list[GetChallengeResponse200BoardItem]):
            records (list[GetChallengeResponse200RecordsItem]):
     """

    slug: str
    family: GetChallengeResponse200Family
    title: str
    objective: GetChallengeResponse200Objective
    status: GetChallengeResponse200Status
    best_known_value: None | str
    best_known_at_open: None | str
    min_improvement: str
    records_count: int
    last_record_at: None | str
    opened_at: str
    closed_at: None | str
    best_known_source: str
    optimal: GetChallengeResponse200OptimalType0 | None
    baseline: GetChallengeResponse200BaselineType0 | None
    verifier: GetChallengeResponse200Verifier
    spec: GetChallengeResponse200Spec
    generator: GetChallengeResponse200GeneratorType0 | None
    licence: str
    board: list[GetChallengeResponse200BoardItem]
    records: list[GetChallengeResponse200RecordsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_challenge_response_200_baseline_type_0 import GetChallengeResponse200BaselineType0 # noqa: PLC0415
        from ..models.get_challenge_response_200_board_item import GetChallengeResponse200BoardItem # noqa: PLC0415
        from ..models.get_challenge_response_200_generator_type_0 import GetChallengeResponse200GeneratorType0 # noqa: PLC0415
        from ..models.get_challenge_response_200_optimal_type_0 import GetChallengeResponse200OptimalType0 # noqa: PLC0415
        from ..models.get_challenge_response_200_records_item import GetChallengeResponse200RecordsItem # noqa: PLC0415
        from ..models.get_challenge_response_200_spec import GetChallengeResponse200Spec # noqa: PLC0415
        from ..models.get_challenge_response_200_verifier import GetChallengeResponse200Verifier # noqa: PLC0415
        slug = self.slug

        family = self.family.value

        title = self.title

        objective = self.objective.value

        status = self.status.value

        best_known_value: None | str
        best_known_value = self.best_known_value

        best_known_at_open: None | str
        best_known_at_open = self.best_known_at_open

        min_improvement = self.min_improvement

        records_count = self.records_count

        last_record_at: None | str
        last_record_at = self.last_record_at

        opened_at = self.opened_at

        closed_at: None | str
        closed_at = self.closed_at

        best_known_source = self.best_known_source

        optimal: dict[str, Any] | None
        if isinstance(self.optimal, GetChallengeResponse200OptimalType0):
            optimal = self.optimal.to_dict()
        else:
            optimal = self.optimal

        baseline: dict[str, Any] | None
        if isinstance(self.baseline, GetChallengeResponse200BaselineType0):
            baseline = self.baseline.to_dict()
        else:
            baseline = self.baseline

        verifier = self.verifier.to_dict()

        spec = self.spec.to_dict()

        generator: dict[str, Any] | None
        if isinstance(self.generator, GetChallengeResponse200GeneratorType0):
            generator = self.generator.to_dict()
        else:
            generator = self.generator

        licence = self.licence

        board = []
        for board_item_data in self.board:
            board_item = board_item_data.to_dict()
            board.append(board_item)



        records = []
        for records_item_data in self.records:
            records_item = records_item_data.to_dict()
            records.append(records_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "slug": slug,
            "family": family,
            "title": title,
            "objective": objective,
            "status": status,
            "best_known_value": best_known_value,
            "best_known_at_open": best_known_at_open,
            "min_improvement": min_improvement,
            "records_count": records_count,
            "last_record_at": last_record_at,
            "opened_at": opened_at,
            "closed_at": closed_at,
            "best_known_source": best_known_source,
            "optimal": optimal,
            "baseline": baseline,
            "verifier": verifier,
            "spec": spec,
            "generator": generator,
            "licence": licence,
            "board": board,
            "records": records,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_challenge_response_200_baseline_type_0 import GetChallengeResponse200BaselineType0 # noqa: PLC0415
        from ..models.get_challenge_response_200_board_item import GetChallengeResponse200BoardItem # noqa: PLC0415
        from ..models.get_challenge_response_200_generator_type_0 import GetChallengeResponse200GeneratorType0 # noqa: PLC0415
        from ..models.get_challenge_response_200_optimal_type_0 import GetChallengeResponse200OptimalType0 # noqa: PLC0415
        from ..models.get_challenge_response_200_records_item import GetChallengeResponse200RecordsItem # noqa: PLC0415
        from ..models.get_challenge_response_200_spec import GetChallengeResponse200Spec # noqa: PLC0415
        from ..models.get_challenge_response_200_verifier import GetChallengeResponse200Verifier # noqa: PLC0415
        d = dict(src_dict)
        slug = d.pop("slug")

        family = GetChallengeResponse200Family(d.pop("family"))




        title = d.pop("title")

        objective = GetChallengeResponse200Objective(d.pop("objective"))




        status = GetChallengeResponse200Status(d.pop("status"))




        def _parse_best_known_value(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        best_known_value = _parse_best_known_value(d.pop("best_known_value"))


        def _parse_best_known_at_open(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        best_known_at_open = _parse_best_known_at_open(d.pop("best_known_at_open"))


        min_improvement = d.pop("min_improvement")

        records_count = d.pop("records_count")

        def _parse_last_record_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_record_at = _parse_last_record_at(d.pop("last_record_at"))


        opened_at = d.pop("opened_at")

        def _parse_closed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        closed_at = _parse_closed_at(d.pop("closed_at"))


        best_known_source = d.pop("best_known_source")

        def _parse_optimal(data: object) -> GetChallengeResponse200OptimalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                optimal_type_0 = GetChallengeResponse200OptimalType0.from_dict(data)



                return optimal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetChallengeResponse200OptimalType0 | None, data)

        optimal = _parse_optimal(d.pop("optimal"))


        def _parse_baseline(data: object) -> GetChallengeResponse200BaselineType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                baseline_type_0 = GetChallengeResponse200BaselineType0.from_dict(data)



                return baseline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetChallengeResponse200BaselineType0 | None, data)

        baseline = _parse_baseline(d.pop("baseline"))


        verifier = GetChallengeResponse200Verifier.from_dict(d.pop("verifier"))




        spec = GetChallengeResponse200Spec.from_dict(d.pop("spec"))




        def _parse_generator(data: object) -> GetChallengeResponse200GeneratorType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                generator_type_0 = GetChallengeResponse200GeneratorType0.from_dict(data)



                return generator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetChallengeResponse200GeneratorType0 | None, data)

        generator = _parse_generator(d.pop("generator"))


        licence = d.pop("licence")

        board = []
        _board = d.pop("board")
        for board_item_data in (_board):
            board_item = GetChallengeResponse200BoardItem.from_dict(board_item_data)



            board.append(board_item)


        records = []
        _records = d.pop("records")
        for records_item_data in (_records):
            records_item = GetChallengeResponse200RecordsItem.from_dict(records_item_data)



            records.append(records_item)


        get_challenge_response_200 = cls(
            slug=slug,
            family=family,
            title=title,
            objective=objective,
            status=status,
            best_known_value=best_known_value,
            best_known_at_open=best_known_at_open,
            min_improvement=min_improvement,
            records_count=records_count,
            last_record_at=last_record_at,
            opened_at=opened_at,
            closed_at=closed_at,
            best_known_source=best_known_source,
            optimal=optimal,
            baseline=baseline,
            verifier=verifier,
            spec=spec,
            generator=generator,
            licence=licence,
            board=board,
            records=records,
        )

        return get_challenge_response_200

