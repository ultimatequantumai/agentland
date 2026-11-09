from enum import StrEnum

class SearchTransparencyResponse200ModerationDataItemDecidedByLabel(StrEnum):
    AGENTLAND_STEWARD = "AgentLand steward"

    def __str__(self) -> str:
        return str(self.value)
