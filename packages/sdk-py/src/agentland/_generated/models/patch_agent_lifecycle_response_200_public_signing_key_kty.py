from enum import StrEnum

class PatchAgentLifecycleResponse200PublicSigningKeyKty(StrEnum):
    OKP = "OKP"

    def __str__(self) -> str:
        return str(self.value)
