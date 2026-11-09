from enum import StrEnum

class OnboardOperatorBodyKind(StrEnum):
    INDIVIDUAL = "individual"
    ORG = "org"

    def __str__(self) -> str:
        return str(self.value)
