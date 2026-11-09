from enum import StrEnum

class GetOperatorAgentResponse200PendingKeyChallengesItemKind(StrEnum):
    COMPROMISE_ROTATION = "compromise_rotation"
    REVOKE = "revoke"

    def __str__(self) -> str:
        return str(self.value)
