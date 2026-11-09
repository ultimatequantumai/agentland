from enum import StrEnum

class GetLeaderboardResponse200SeasonType0Status(StrEnum):
    ACTIVE = "active"
    FINAL = "final"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
