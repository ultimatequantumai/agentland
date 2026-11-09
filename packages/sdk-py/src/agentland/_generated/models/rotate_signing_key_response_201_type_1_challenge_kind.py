from enum import StrEnum

class RotateSigningKeyResponse201Type1ChallengeKind(StrEnum):
    COMPROMISE_ROTATION = "compromise_rotation"
    REVOKE = "revoke"

    def __str__(self) -> str:
        return str(self.value)
