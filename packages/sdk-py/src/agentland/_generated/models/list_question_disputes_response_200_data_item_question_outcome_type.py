from enum import StrEnum

class ListQuestionDisputesResponse200DataItemQuestionOutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
