from enum import StrEnum

class GetLatestDigestResponse200IssueType0RationalesItemRationaleQuestionStatus(StrEnum):
    CLOSED = "closed"
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
