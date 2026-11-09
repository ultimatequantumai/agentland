from enum import StrEnum

class ListTransparencyDisputesResponse200DataItemTimelineItemStatusType1(StrEnum):
    REJECTED = "rejected"
    UPHELD = "upheld"
    VOIDED_QUESTION = "voided_question"

    def __str__(self) -> str:
        return str(self.value)
