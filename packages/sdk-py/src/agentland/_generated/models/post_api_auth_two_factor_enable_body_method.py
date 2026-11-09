from enum import StrEnum

class PostApiAuthTwoFactorEnableBodyMethod(StrEnum):
    OTP = "otp"
    TOTP = "totp"

    def __str__(self) -> str:
        return str(self.value)
