from enum import StrEnum

class ListQuestionDisputesResponse200DataItemBasisType1(StrEnum):
    DOCUMENTED_SOURCE_ERROR = "documented_source_error"
    SOURCE_FINAL = "source_final"

    def __str__(self) -> str:
        return str(self.value)
