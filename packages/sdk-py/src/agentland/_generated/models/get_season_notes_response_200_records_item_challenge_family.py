from enum import StrEnum

class GetSeasonNotesResponse200RecordsItemChallengeFamily(StrEnum):
    BINPACK = "binpack"
    CVRP = "cvrp"
    JOBSHOP = "jobshop"
    MAXSAT = "maxsat"
    TSP = "tsp"

    def __str__(self) -> str:
        return str(self.value)
