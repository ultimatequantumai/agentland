from enum import StrEnum

class RotateSigningKeyResponse201Type0KeyKind(StrEnum):
    SIGN_ED25519 = "sign_ed25519"

    def __str__(self) -> str:
        return str(self.value)
