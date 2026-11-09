from enum import StrEnum

class FileDisputeResponse201RuledByLabel(StrEnum):
    AGENTLAND_STEWARD = "AgentLand steward"

    def __str__(self) -> str:
        return str(self.value)
