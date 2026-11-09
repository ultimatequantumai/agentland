from enum import StrEnum

class GetQuestionResponse200ResolutionType0ResolvedBy(StrEnum):
    SOURCE = "source"
    STEWARD = "steward"

    def __str__(self) -> str:
        return str(self.value)
