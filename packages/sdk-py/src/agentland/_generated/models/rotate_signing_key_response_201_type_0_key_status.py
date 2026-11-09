from enum import StrEnum

class RotateSigningKeyResponse201Type0KeyStatus(StrEnum):
    ACTIVE = "active"
    REVOKED = "revoked"
    ROTATED = "rotated"

    def __str__(self) -> str:
        return str(self.value)
