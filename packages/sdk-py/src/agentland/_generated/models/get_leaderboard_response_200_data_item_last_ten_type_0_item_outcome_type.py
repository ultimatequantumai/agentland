from enum import StrEnum

class GetLeaderboardResponse200DataItemLastTenType0ItemOutcomeType(StrEnum):
    BINARY = "binary"
    MULTI = "multi"

    def __str__(self) -> str:
        return str(self.value)
