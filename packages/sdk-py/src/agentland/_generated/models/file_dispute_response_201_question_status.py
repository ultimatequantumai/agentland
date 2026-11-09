from enum import StrEnum

class FileDisputeResponse201QuestionStatus(StrEnum):
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
