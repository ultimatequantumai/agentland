from enum import StrEnum

class GetLeaderboardResponse200DataItemAgentStatus(StrEnum):
    ACTIVE = "active"
    PAUSED = "paused"
    RETIRED = "retired"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
