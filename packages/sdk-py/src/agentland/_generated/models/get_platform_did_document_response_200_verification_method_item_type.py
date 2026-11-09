from enum import StrEnum

class GetPlatformDidDocumentResponse200VerificationMethodItemType(StrEnum):
    JSONWEBKEY2020 = "JsonWebKey2020"

    def __str__(self) -> str:
        return str(self.value)
