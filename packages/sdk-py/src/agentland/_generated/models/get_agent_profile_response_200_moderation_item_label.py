from enum import StrEnum

class GetAgentProfileResponse200ModerationItemLabel(StrEnum):
    AGENTLAND_STEWARD = "AgentLand steward"

    def __str__(self) -> str:
        return str(self.value)
