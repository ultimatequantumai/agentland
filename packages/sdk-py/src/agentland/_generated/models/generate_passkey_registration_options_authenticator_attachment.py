from enum import StrEnum

class GeneratePasskeyRegistrationOptionsAuthenticatorAttachment(StrEnum):
    CROSS_PLATFORM = "cross-platform"
    PLATFORM = "platform"

    def __str__(self) -> str:
        return str(self.value)
