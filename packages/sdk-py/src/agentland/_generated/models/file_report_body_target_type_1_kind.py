from enum import StrEnum

class FileReportBodyTargetType1Kind(StrEnum):
    BIO = "bio"

    def __str__(self) -> str:
        return str(self.value)
