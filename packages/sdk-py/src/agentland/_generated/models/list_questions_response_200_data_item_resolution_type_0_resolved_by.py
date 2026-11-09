from enum import StrEnum

class ListQuestionsResponse200DataItemResolutionType0ResolvedBy(StrEnum):
    SOURCE = "source"
    STEWARD = "steward"

    def __str__(self) -> str:
        return str(self.value)
