from enum import StrEnum

class GetChallengeResponse200Family(StrEnum):
    BINPACK = "binpack"
    CVRP = "cvrp"
    JOBSHOP = "jobshop"
    MAXSAT = "maxsat"
    TSP = "tsp"

    def __str__(self) -> str:
        return str(self.value)
