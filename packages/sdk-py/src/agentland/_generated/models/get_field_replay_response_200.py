from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_field_replay_response_200_frames_item import GetFieldReplayResponse200FramesItem





T = TypeVar("T", bound="GetFieldReplayResponse200")



@_attrs_define
class GetFieldReplayResponse200:
    """ 
        Attributes:
            from_slot (int):
            to_slot (int):
            frames (list[GetFieldReplayResponse200FramesItem]):
            next_cursor (None | str): The next hour slot while it is inside the ring
     """

    from_slot: int
    to_slot: int
    frames: list[GetFieldReplayResponse200FramesItem]
    next_cursor: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_field_replay_response_200_frames_item import GetFieldReplayResponse200FramesItem # noqa: PLC0415
        from_slot = self.from_slot

        to_slot = self.to_slot

        frames = []
        for frames_item_data in self.frames:
            frames_item = frames_item_data.to_dict()
            frames.append(frames_item)



        next_cursor: None | str
        next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "from_slot": from_slot,
            "to_slot": to_slot,
            "frames": frames,
            "next_cursor": next_cursor,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_field_replay_response_200_frames_item import GetFieldReplayResponse200FramesItem # noqa: PLC0415
        d = dict(src_dict)
        from_slot = d.pop("from_slot")

        to_slot = d.pop("to_slot")

        frames = []
        _frames = d.pop("frames")
        for frames_item_data in (_frames):
            frames_item = GetFieldReplayResponse200FramesItem.from_dict(frames_item_data)



            frames.append(frames_item)


        def _parse_next_cursor(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))


        get_field_replay_response_200 = cls(
            from_slot=from_slot,
            to_slot=to_slot,
            frames=frames,
            next_cursor=next_cursor,
        )


        get_field_replay_response_200.additional_properties = d
        return get_field_replay_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
