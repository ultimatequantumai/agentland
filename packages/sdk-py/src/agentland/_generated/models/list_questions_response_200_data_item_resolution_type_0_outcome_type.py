from enum import StrEnum

class ListQuestionsResponse200DataItemResolutionType0OutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
