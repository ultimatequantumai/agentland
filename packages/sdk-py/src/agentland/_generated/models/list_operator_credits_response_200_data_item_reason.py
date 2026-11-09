from enum import StrEnum

class ListOperatorCreditsResponse200DataItemReason(StrEnum):
    ADJUSTMENT = "adjustment"
    GRANT = "grant"
    VERIFICATION = "verification"

    def __str__(self) -> str:
        return str(self.value)
