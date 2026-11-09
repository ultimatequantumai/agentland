from enum import StrEnum

class RotateSigningKeyResponse201Type0KeyCustody(StrEnum):
    PLATFORM = "platform"
    SELF = "self"

    def __str__(self) -> str:
        return str(self.value)
