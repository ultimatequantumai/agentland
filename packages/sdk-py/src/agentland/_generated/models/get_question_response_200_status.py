from enum import StrEnum

class GetQuestionResponse200Status(StrEnum):
    CLOSED = "closed"
    OPEN = "open"
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
