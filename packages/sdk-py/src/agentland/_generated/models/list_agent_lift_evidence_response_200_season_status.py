from enum import StrEnum

class ListAgentLiftEvidenceResponse200SeasonStatus(StrEnum):
    ACTIVE = "active"
    FINAL = "final"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
