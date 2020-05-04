from RagaGraph import constructRagaGraph
from ConstructGrams import constructGrams
from ProbabilityAllocation import probabilityAllocation, cummulativeProbability
from OutputGenerator import outputGenerator
import winsound

import matplotlib.pyplot as plt
import csv
import numpy as np


twoGrams = []
fourGrams = []
eightGrams = []
sixteenGrams = []
twoGramGraph = {}
fourGramGraph = {}
eightGramGraph = {}
sixteenGramGraph = {}
twoCummGraph = {}
fourCummGraph = {}
eightCummGraph = {}
sixteenCummGraph = {}
distanceMatrix = [[]]


if __name__ == '__main__':
    print("Program Begins")
    distanceMatrix = constructRagaGraph("mohanam")
    twoGrams, twoGramGraph, fourGrams, fourGramGraph, eightGrams, eightGramGraph, sixteenGrams, sixteenGramGraph = constructGrams(
        "33232122121323121112323434554444345456787786675564456786654432123332321233312333354323336543234455443211232211123445566654432345667876765654321211112233445567878756767645656534545476543212", distanceMatrix)

    twoGramGraph = probabilityAllocation([twoGramGraph])
    fourGramGraph = probabilityAllocation([fourGramGraph])
    eightGramGraph = probabilityAllocation([eightGramGraph, eightGrams])
    sixteenGramGraph = probabilityAllocation([sixteenGramGraph, sixteenGrams])

    # print(twoGramGraph)
    twoCummGraph = cummulativeProbability(twoGramGraph)
    fourCummGraph = cummulativeProbability(fourGramGraph)
    eightCummGraph = cummulativeProbability(eightGramGraph)
    sixteenCummGraph = cummulativeProbability(sixteenGramGraph)

    # print(twoCummGraph)

    outputGenerator(twoCummGraph, fourCummGraph,
                    eightCummGraph, sixteenCummGraph)

    # print(twoCummGraph)
    # print(sixteenGrams)
    # print(sixteenGramGraph)
    # print(distanceMatrix[1][3])  # MUST QUERY FOR (i-1,j-1)
