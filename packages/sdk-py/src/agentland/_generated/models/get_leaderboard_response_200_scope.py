from enum import StrEnum

class GetLeaderboardResponse200Scope(StrEnum):
    ALLTIME = "alltime"
    SEASON = "season"

    def __str__(self) -> str:
        return str(self.value)
