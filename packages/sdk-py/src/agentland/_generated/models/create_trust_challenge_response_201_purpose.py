from enum import StrEnum

class CreateTrustChallengeResponse201Purpose(StrEnum):
    POP = "pop"
    VERIFY = "verify"

    def __str__(self) -> str:
        return str(self.value)
