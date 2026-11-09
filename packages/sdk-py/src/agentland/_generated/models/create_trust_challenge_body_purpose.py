from enum import StrEnum

class CreateTrustChallengeBodyPurpose(StrEnum):
    POP = "pop"
    VERIFY = "verify"

    def __str__(self) -> str:
        return str(self.value)
