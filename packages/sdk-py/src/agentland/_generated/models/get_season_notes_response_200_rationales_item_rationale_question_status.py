from enum import StrEnum

class GetSeasonNotesResponse200RationalesItemRationaleQuestionStatus(StrEnum):
    CLOSED = "closed"
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
