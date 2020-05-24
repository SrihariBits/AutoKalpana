from Probabilistic_Approach import constructRagaGraph
from Probabilistic_Approach import constructGrams
from ToNpArray import toNpArray
import numpy as np


def findPatterns(inputList, raga='mohanam'):
    distanceMatrix = constructRagaGraph(raga)
    for size in range(20, 1, -1):
        i = 0
        while i < len(inputList)-2*size:
            subpartA = inputList[i+size:i+2*size]
            subpartB = inputList[i:i+size]
            diff = [distanceMatrix[subpartA[x]][subpartB[x]]
                    for x in range(len(subpartA))]
            cnt = 0
            currdiff = diff
            while i+2*size < len(inputList) and currdiff == diff:
                cnt += 1
                i += size
                subpartA = inputList[i+size:i+2*size]
                subpartB = inputList[i:i+size]
                currdiff = [distanceMatrix[subpartA[x]][subpartB[x]]
                            for x in range(len(subpartA))]
            if cnt > 1:
                print(diff, cnt)
            i += 1


if __name__ == "__main__":
    print("***** PROGRAM STARTED *****\n")
    inputString = "ggppppdpSSSSRSddppdpggrrgpdSdddpggrrggdpggpggrssggggrgpgppppggdpdddpSSSSdGRRSSSdSdddpgpdSdpdpggrssrgggggrpgrrsrsgrsggppppdpSSSS"
    arr = toNpArray(inputString)
    findPatterns(arr, 'mohanam')
    print("\n***** PROGRAM ENDED *****")
