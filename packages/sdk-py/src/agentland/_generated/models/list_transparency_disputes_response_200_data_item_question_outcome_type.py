from enum import StrEnum

class ListTransparencyDisputesResponse200DataItemQuestionOutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
