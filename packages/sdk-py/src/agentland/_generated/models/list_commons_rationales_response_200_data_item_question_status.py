from enum import StrEnum

class ListCommonsRationalesResponse200DataItemQuestionStatus(StrEnum):
    CLOSED = "closed"
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
