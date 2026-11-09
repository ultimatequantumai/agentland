from enum import StrEnum

class OnboardOperatorResponse201Kind(StrEnum):
    INDIVIDUAL = "individual"
    ORG = "org"

    def __str__(self) -> str:
        return str(self.value)
