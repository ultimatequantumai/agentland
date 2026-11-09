from enum import StrEnum

class ListIncidentsResponse200DataItemOpenedBy(StrEnum):
    AGENTLAND_AUTOMATED_CHECK = "AgentLand (automated check)"
    AGENTLAND_STEWARD = "AgentLand steward"

    def __str__(self) -> str:
        return str(self.value)
