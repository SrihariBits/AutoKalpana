from Probabilistic_Approach import constructRagaGraph
from Probabilistic_Approach import constructGrams
from ToNpArray import toNpArray
import numpy as np

##########TODO###########
# compress commas       #
# other 5 yatis         #
# tala patterns         #
# partition algorithm   #
# combo->const-inc patt #
#########################


def findIncPatterns(inputList, raga='mohanam'):
    distanceMatrix = constructRagaGraph(raga)
    for size in range(2, 6, 1):
        i = 0
        expand = 0
        while i + size + expand < len(inputList):
            subpart = inputList[i:i+size+expand]
            diff = [distanceMatrix[subpart[x-1]][subpart[x]]
                    for x in range(1, len(subpart))]
            cnt = 0
            diff = np.array(diff)
            diff.astype(int)
            if np.min(diff) == np.max(diff) and i+2*(size+expand)+1 < len(inputList):
                while np.all(inputList[i+size+expand:i+2*(size+expand)] == inputList[i:i+size+expand]) and distanceMatrix[inputList[i+2*(size+expand)]][inputList[i+2*(size+expand)+1]] == 1:
                    cnt += 1
                    i = i + size + expand
                    expand += 1
                    if i+2*(size+expand)+1 >= len(inputList):
                        break
            if cnt > 1:
                print(diff, cnt)
            i += 1
            expand = 0


def findConstPatterns(inputList, raga='mohanam'):
    distanceMatrix = constructRagaGraph(raga)
    for size in range(20, 1, -1):
        i = 0
        while i < len(inputList)-2*size:
            subpartA = inputList[i+size:i+2*size]
            subpartB = inputList[i:i+size]
            diff = [distanceMatrix[subpartB[x]][subpartA[x]]
                    for x in range(len(subpartA))]
            cnt = 0
            currdiff = diff
            while i+2*size < len(inputList) and currdiff == diff:
                cnt += 1
                i += size
                subpartA = inputList[i+size:i+2*size]
                subpartB = inputList[i:i+size]
                currdiff = [distanceMatrix[subpartB[x]][subpartA[x]]
                            for x in range(len(subpartA))]
            if cnt > 1:
                print(diff, cnt)
            i += 1


if __name__ == "__main__":
    print("***** PROGRAM STARTED *****\n")
    inputString = "ggppppdpSSSSRSddppdpggrrgpdSdddpggrrggdpggpggrssggggrgpgppppggdpdddpSSSSdGRRSSSdSdddpgpdSdpdpggrssrgggggrpgrrsrsgrsggppppdpSSSS"
    arr = toNpArray(inputString)
    #findConstPatterns(arr, 'mohanam')
    findIncPatterns(arr, 'mohanam')
    print("\n***** PROGRAM ENDED *****")
