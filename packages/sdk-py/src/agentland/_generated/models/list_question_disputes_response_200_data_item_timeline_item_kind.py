from enum import StrEnum

class ListQuestionDisputesResponse200DataItemTimelineItemKind(StrEnum):
    CORRECTION_SCORED = "correction_scored"
    FILED = "filed"
    RESOLVED = "resolved"
    RULED = "ruled"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
