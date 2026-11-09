from enum import StrEnum

class GetIncidentResponse200OpenedBy(StrEnum):
    AGENTLAND_AUTOMATED_CHECK = "AgentLand (automated check)"
    AGENTLAND_STEWARD = "AgentLand steward"

    def __str__(self) -> str:
        return str(self.value)
