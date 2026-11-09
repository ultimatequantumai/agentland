from enum import StrEnum

class ListAgentRationalesResponse200DataItemQuestionStatus(StrEnum):
    CLOSED = "closed"
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
