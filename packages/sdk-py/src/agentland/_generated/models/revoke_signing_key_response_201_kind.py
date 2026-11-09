from enum import StrEnum

class RevokeSigningKeyResponse201Kind(StrEnum):
    COMPROMISE_ROTATION = "compromise_rotation"
    REVOKE = "revoke"

    def __str__(self) -> str:
        return str(self.value)
