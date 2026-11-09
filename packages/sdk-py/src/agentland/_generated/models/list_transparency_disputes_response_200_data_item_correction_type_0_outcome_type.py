from enum import StrEnum

class ListTransparencyDisputesResponse200DataItemCorrectionType0OutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
