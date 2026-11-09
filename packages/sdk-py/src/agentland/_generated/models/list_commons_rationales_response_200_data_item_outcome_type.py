from enum import StrEnum

class ListCommonsRationalesResponse200DataItemOutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
