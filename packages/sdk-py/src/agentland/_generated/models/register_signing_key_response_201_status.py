from enum import StrEnum

class RegisterSigningKeyResponse201Status(StrEnum):
    ACTIVE = "active"
    REVOKED = "revoked"
    ROTATED = "rotated"

    def __str__(self) -> str:
        return str(self.value)
