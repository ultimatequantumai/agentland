from enum import StrEnum

class GetVaultProofResponse200Type1BundleFormat(StrEnum):
    AGENTLAND_VAULT1 = "agentland-vault/1"

    def __str__(self) -> str:
        return str(self.value)
