from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_latest_digest_response_200_issue_type_0 import GetLatestDigestResponse200IssueType0





T = TypeVar("T", bound="GetLatestDigestResponse200")



@_attrs_define
class GetLatestDigestResponse200:
    """ 
        Attributes:
            issue (GetLatestDigestResponse200IssueType0 | None):
     """

    issue: GetLatestDigestResponse200IssueType0 | None





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_latest_digest_response_200_issue_type_0 import GetLatestDigestResponse200IssueType0 # noqa: PLC0415
        issue: dict[str, Any] | None
        if isinstance(self.issue, GetLatestDigestResponse200IssueType0):
            issue = self.issue.to_dict()
        else:
            issue = self.issue


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "issue": issue,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_latest_digest_response_200_issue_type_0 import GetLatestDigestResponse200IssueType0 # noqa: PLC0415
        d = dict(src_dict)
        def _parse_issue(data: object) -> GetLatestDigestResponse200IssueType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                issue_type_0 = GetLatestDigestResponse200IssueType0.from_dict(data)



                return issue_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetLatestDigestResponse200IssueType0 | None, data)

        issue = _parse_issue(d.pop("issue"))


        get_latest_digest_response_200 = cls(
            issue=issue,
        )

        return get_latest_digest_response_200

