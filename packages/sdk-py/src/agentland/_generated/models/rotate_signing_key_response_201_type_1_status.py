from enum import StrEnum

class RotateSigningKeyResponse201Type1Status(StrEnum):
    CHALLENGE_OPENED = "challenge_opened"

    def __str__(self) -> str:
        return str(self.value)
