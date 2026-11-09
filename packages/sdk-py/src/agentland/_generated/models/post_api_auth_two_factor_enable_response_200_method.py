from enum import StrEnum

class PostApiAuthTwoFactorEnableResponse200Method(StrEnum):
    OTP = "otp"
    TOTP = "totp"

    def __str__(self) -> str:
        return str(self.value)
