from enum import StrEnum

class GetChallengeResponse200VerifierProtocol(StrEnum):
    AGENTLAND_VERIFIER1 = "agentland-verifier/1"

    def __str__(self) -> str:
        return str(self.value)
