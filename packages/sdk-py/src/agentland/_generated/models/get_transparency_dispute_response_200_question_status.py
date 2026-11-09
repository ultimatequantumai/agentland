from enum import StrEnum

class GetTransparencyDisputeResponse200QuestionStatus(StrEnum):
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
