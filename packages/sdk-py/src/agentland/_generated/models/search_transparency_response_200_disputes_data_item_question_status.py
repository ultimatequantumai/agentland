from enum import StrEnum

class SearchTransparencyResponse200DisputesDataItemQuestionStatus(StrEnum):
    RESOLVED = "resolved"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
