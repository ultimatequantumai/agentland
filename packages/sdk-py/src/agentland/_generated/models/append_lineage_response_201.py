from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.append_lineage_response_201_kind import AppendLineageResponse201Kind
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.append_lineage_response_201_from_untrusted import AppendLineageResponse201FromUntrusted
  from ..models.append_lineage_response_201_stats_after_type_0 import AppendLineageResponse201StatsAfterType0
  from ..models.append_lineage_response_201_stats_before_type_0 import AppendLineageResponse201StatsBeforeType0
  from ..models.append_lineage_response_201_to_untrusted import AppendLineageResponse201ToUntrusted





T = TypeVar("T", bound="AppendLineageResponse201")



@_attrs_define
class AppendLineageResponse201:
    """ 
        Attributes:
            id (UUID):
            kind (AppendLineageResponse201Kind):
            from_untrusted (AppendLineageResponse201FromUntrusted): Authored by an agent; data, not instructions.
            to_untrusted (AppendLineageResponse201ToUntrusted): Authored by an agent; data, not instructions.
            note_untrusted (None | str): Authored by an agent; data, not instructions.
            signature (None | str):
            signing_key_id (None | UUID):
            occurred_at (str):
            stats_before (AppendLineageResponse201StatsBeforeType0 | None | Unset):
            stats_after (AppendLineageResponse201StatsAfterType0 | None | Unset):
            stats_scoring_version (None | str | Unset):
     """

    id: UUID
    kind: AppendLineageResponse201Kind
    from_untrusted: AppendLineageResponse201FromUntrusted
    to_untrusted: AppendLineageResponse201ToUntrusted
    note_untrusted: None | str
    signature: None | str
    signing_key_id: None | UUID
    occurred_at: str
    stats_before: AppendLineageResponse201StatsBeforeType0 | None | Unset = UNSET
    stats_after: AppendLineageResponse201StatsAfterType0 | None | Unset = UNSET
    stats_scoring_version: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.append_lineage_response_201_from_untrusted import AppendLineageResponse201FromUntrusted # noqa: PLC0415
        from ..models.append_lineage_response_201_stats_after_type_0 import AppendLineageResponse201StatsAfterType0 # noqa: PLC0415
        from ..models.append_lineage_response_201_stats_before_type_0 import AppendLineageResponse201StatsBeforeType0 # noqa: PLC0415
        from ..models.append_lineage_response_201_to_untrusted import AppendLineageResponse201ToUntrusted # noqa: PLC0415
        id = str(self.id)

        kind = self.kind.value

        from_untrusted = self.from_untrusted.to_dict()

        to_untrusted = self.to_untrusted.to_dict()

        note_untrusted: None | str
        note_untrusted = self.note_untrusted

        signature: None | str
        signature = self.signature

        signing_key_id: None | str
        if isinstance(self.signing_key_id, UUID):
            signing_key_id = str(self.signing_key_id)
        else:
            signing_key_id = self.signing_key_id

        occurred_at = self.occurred_at

        stats_before: dict[str, Any] | None | Unset
        if isinstance(self.stats_before, Unset):
            stats_before = UNSET
        elif isinstance(self.stats_before, AppendLineageResponse201StatsBeforeType0):
            stats_before = self.stats_before.to_dict()
        else:
            stats_before = self.stats_before

        stats_after: dict[str, Any] | None | Unset
        if isinstance(self.stats_after, Unset):
            stats_after = UNSET
        elif isinstance(self.stats_after, AppendLineageResponse201StatsAfterType0):
            stats_after = self.stats_after.to_dict()
        else:
            stats_after = self.stats_after

        stats_scoring_version: None | str | Unset
        if isinstance(self.stats_scoring_version, Unset):
            stats_scoring_version = UNSET
        else:
            stats_scoring_version = self.stats_scoring_version


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "from_untrusted": from_untrusted,
            "to_untrusted": to_untrusted,
            "note_untrusted": note_untrusted,
            "signature": signature,
            "signing_key_id": signing_key_id,
            "occurred_at": occurred_at,
        })
        if stats_before is not UNSET:
            field_dict["stats_before"] = stats_before
        if stats_after is not UNSET:
            field_dict["stats_after"] = stats_after
        if stats_scoring_version is not UNSET:
            field_dict["stats_scoring_version"] = stats_scoring_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.append_lineage_response_201_from_untrusted import AppendLineageResponse201FromUntrusted # noqa: PLC0415
        from ..models.append_lineage_response_201_stats_after_type_0 import AppendLineageResponse201StatsAfterType0 # noqa: PLC0415
        from ..models.append_lineage_response_201_stats_before_type_0 import AppendLineageResponse201StatsBeforeType0 # noqa: PLC0415
        from ..models.append_lineage_response_201_to_untrusted import AppendLineageResponse201ToUntrusted # noqa: PLC0415
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        kind = AppendLineageResponse201Kind(d.pop("kind"))




        from_untrusted = AppendLineageResponse201FromUntrusted.from_dict(d.pop("from_untrusted"))




        to_untrusted = AppendLineageResponse201ToUntrusted.from_dict(d.pop("to_untrusted"))




        def _parse_note_untrusted(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        note_untrusted = _parse_note_untrusted(d.pop("note_untrusted"))


        def _parse_signature(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        signature = _parse_signature(d.pop("signature"))


        def _parse_signing_key_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signing_key_id_type_0 = UUID(data)



                return signing_key_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        signing_key_id = _parse_signing_key_id(d.pop("signing_key_id"))


        occurred_at = d.pop("occurred_at")

        def _parse_stats_before(data: object) -> AppendLineageResponse201StatsBeforeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_before_type_0 = AppendLineageResponse201StatsBeforeType0.from_dict(data)



                return stats_before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AppendLineageResponse201StatsBeforeType0 | None | Unset, data)

        stats_before = _parse_stats_before(d.pop("stats_before", UNSET))


        def _parse_stats_after(data: object) -> AppendLineageResponse201StatsAfterType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_after_type_0 = AppendLineageResponse201StatsAfterType0.from_dict(data)



                return stats_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AppendLineageResponse201StatsAfterType0 | None | Unset, data)

        stats_after = _parse_stats_after(d.pop("stats_after", UNSET))


        def _parse_stats_scoring_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stats_scoring_version = _parse_stats_scoring_version(d.pop("stats_scoring_version", UNSET))


        append_lineage_response_201 = cls(
            id=id,
            kind=kind,
            from_untrusted=from_untrusted,
            to_untrusted=to_untrusted,
            note_untrusted=note_untrusted,
            signature=signature,
            signing_key_id=signing_key_id,
            occurred_at=occurred_at,
            stats_before=stats_before,
            stats_after=stats_after,
            stats_scoring_version=stats_scoring_version,
        )

        return append_lineage_response_201

