from enum import StrEnum

class ListLedgerResponse200DataItemOutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"

    def __str__(self) -> str:
        return str(self.value)
