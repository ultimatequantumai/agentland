from enum import StrEnum

class GetCommonsRationaleResponse200QuestionStatus(StrEnum):
    CLOSED = "closed"
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
