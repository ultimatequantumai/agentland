from enum import StrEnum

class ListTransparencyDisputesResponse200DataItemQuestionStatus(StrEnum):
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
