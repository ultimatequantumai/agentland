from enum import StrEnum

class ListQuestionDisputesResponse200DataItemRuledByLabel(StrEnum):
    AGENTLAND_STEWARD = "AgentLand steward"

    def __str__(self) -> str:
        return str(self.value)
