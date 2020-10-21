from Probabilistic_Approach import constructRagaGraph
from Probabilistic_Approach import constructGrams
from ToNpArray import toNpArray
from helpers import rhythmPatternHelper, partitionHelper
import numpy as np

##########TODO##############
# compress commas (Y)      #
# Yatis  (Y)               #
# tala patterns  (Y)       #
# partition algorithm  (Y) #
# inc & dec len pattern (Y)#
# combo->const-inc patt    #
############################


def Compare(list1, list2):
    if(len(list1) != len(list2)):
        return False
    for i in range(len(list1)):
        if(list1[i] != list2[i]):
            return False
    return True

# replace commas with previous character


def compressCommas(inputString, raga='mohanam'):
    inputList = list(inputString)
    for i in range(len(inputList)):
        if(i == 0 and inputList[i] == ','):
            inputList[i] = 'S'
        elif(inputList[i] == ','):
            inputList[i] = inputList[i-1]
    outputString = ""
    return outputString.join(inputList)


# Gopuchha and Strotovaha Yati - starts from all positions in string, with fixed 2-6
# initial pattern string having fixed internal difference, also increasing
# in length in further patterns
def findIncPatterns(inputList, raga='mohanam'):
    distanceMatrix = constructRagaGraph(raga)
    retlist = []
    newlist = []
    found = False
    for size in range(2, 6, 1):
        newlist = []
        i = 0
        expand = 0
        while i + size + expand < len(inputList):
            subpart = inputList[i:i+size+expand]
            diff = [distanceMatrix[subpart[x-1]][subpart[x]]
                    for x in range(1, len(subpart))]
            cnt = 0
            diff = np.array(diff)
            diff.astype(int)
            start = i
            if np.min(diff) == np.max(diff) and i+2*(size+expand)+1 < len(inputList):
                while (Compare(inputList[i+size+expand:i+2*(size+expand)], inputList[i:i+size+expand]) and distanceMatrix[inputList[i+2*(size+expand)]-1][inputList[i+2*(size+expand)]] == diff[0]) or (Compare(inputList[i+size+expand+1:i+2*(size+expand)+1], inputList[i:i+size+expand]) and distanceMatrix[inputList[i+size+expand]][inputList[i+size+expand+1]] == diff[0]):
                    cnt += 1
                    i = i + size + expand
                    expand += 1
                    if i+2*(size+expand)+1 >= len(inputList):
                        break
            if cnt > 0:
                if newlist:
                    retlist.append(newlist)
                i = i + size + expand
                newlist = list(inputList[start:i])
                newlist.append(-1)
                newlist.insert(0, -1)
                retlist.append(newlist)
                newlist = []
                found = True
                # (Initial diff, number of increments in len, type)
                # print(diff, cnt, 1)
            if found and i >= len(inputList):
                return retlist
            if cnt > 0:
                expand = 0
                continue
            newlist.append(inputList[i])
            i += 1
            expand = 0
        if found:
            if newlist:
                retlist.append(newlist)
            return retlist
    return retlist


# Gopuchha and Strotovaha Yati - starts from all positions in string, with fixed 6-2
# initial pattern string having fixed internal difference, also decreasing
# in length in further patterns
def findDecPatterns(inputList, raga='mohanam'):
    distanceMatrix = constructRagaGraph(raga)
    retlist = []
    newlist = []
    found = False
    for size in range(6, 2, -1):
        i = 0
        expand = 0
        newlist = []
        while i + size - expand < len(inputList):
            subpart = inputList[i:i+size-expand]
            diff = [distanceMatrix[subpart[x-1]][subpart[x]]
                    for x in range(1, len(subpart))]
            cnt = 0
            diff = np.array(diff)
            diff.astype(int)
            start = i
            if np.min(diff) == np.max(diff) and i+2*(size-expand)-1 < len(inputList):
                while Compare(inputList[i+size-expand:i+2*(size-expand)-1], inputList[i:i+size-expand-1]) or Compare(inputList[i+size-expand:i+2*(size-expand)-1], inputList[i+1:i+size-expand]):
                    cnt += 1
                    i = i + size - expand
                    expand += 1
                    if i+2*(size-expand)-1 >= len(inputList):
                        break
            if cnt > 0:
                if newlist:
                    retlist.append(newlist)
                i = i + size - expand
                newlist = list(inputList[start:i])
                newlist.append(-1)
                newlist.insert(0, -1)
                retlist.append(newlist)
                newlist = []
                found = True
                # (Initial diff, number of increments in len, type)
                # print(diff, cnt, 1)
            if found and i >= len(inputList):
                return retlist
            if cnt > 0:
                expand = 0
                continue
            newlist.append(inputList[i])
            i += 1
            expand = 0
        if found:
            if newlist:
                retlist.append(newlist)
            return retlist
    return retlist


# Current pattern and next pattern have same CORRESPONDING difference (automatic internal pattern)
def findConstPatterns(inputList, raga='mohanam'):
    distanceMatrix = constructRagaGraph(raga)
    retlist = []
    newlist = []
    found = False
    for size in range(20, 2, -1):
        i = 0
        newlist = []
        while i < len(inputList)-2*size:
            subpartA = inputList[i+size:i+2*size]
            subpartB = inputList[i:i+size]
            diff = [distanceMatrix[subpartB[x]][subpartA[x]]
                    for x in range(len(subpartA))]
            cnt = 0
            currdiff = diff
            start = i
            while i+2*size < len(inputList) and currdiff == diff:
                cnt += 1
                i += size
                subpartA = inputList[i+size: i+2*size]
                subpartB = inputList[i: i+size]
                currdiff = [distanceMatrix[subpartB[x]][subpartA[x]]
                            for x in range(len(subpartA))]
            if cnt > 1:
                if newlist:
                    retlist.append(newlist)
                i += size
                newlist = list(inputList[start:i])
                newlist.append(-1)
                newlist.insert(0, -1)
                retlist.append(newlist)
                newlist = []
                found = True
                # (fixed diff, number of such patterns, type)
                #print(diff, cnt, 2)
            else:
                i -= size
            if found and i >= len(inputList):
                return retlist
            if cnt > 1:
                continue
            newlist.append(inputList[i])
            i += 1
        if found:
            if newlist:
                retlist.append(newlist)
            return retlist
    return retlist


# Internal pattern with respect to rhythms (tabla/mridangam)
def findRhythmPatterns(inputList, raga='mohanam'):
    distanceMatrix = constructRagaGraph(raga)
    size = 8
    i = 0
    while i < len(inputList)-size:
        subpart = inputList[i: i+size]
        diff = [distanceMatrix[subpart[x-1]][subpart[x]]
                for x in range(1, len(subpart), 1)]
        if rhythmPatternHelper(subpart):
            print(diff, 0, 3)
        i += 1


# Patterns formed as a partition of number (5,6,7 or 8 for now)
def findPartitionPatterns(inputList, raga='mohanam'):
    for n in range(8, 4, -1):
        distanceMatrix = constructRagaGraph(raga)
        p_list = partitionHelper(n)
        i = 0
        sol = []
        while i < len(inputList)-n:
            subpart = inputList[i: i+n]
            found = True
            last = 0
            for parts in p_list:
                for part in parts:
                    subsubpart = subpart[last: last+part]
                    diff = [distanceMatrix[subsubpart[x-1]][subsubpart[x]]
                            for x in range(1, len(subsubpart), 1)]
                    if np.min(diff) >= -1 and np.max(diff) <= 1:
                        last += part
                    else:
                        found = False
                        break
                if found:
                    sol.append([distanceMatrix[subpart[x-1]][subpart[x]]
                                for x in range(1, len(subpart), 1)])
                    i += n
                    break
            if not found:
                i += 1


if __name__ == "__main__":
    print("***** PROGRAM STARTED *****\n")
    # inputString = "ggp,p,dpS,S,RSd,d,p,d,pg,g,r,gpdSd,,pg,rrggdpg,pggrs,ggggrgpgp,p,ggdpd,dpS,S,dGRRS,SdSdddpgpdSdpdpggrssrg,g,grpgrrsrsgrsggp,p,dpS,S,"
    inputString = "srgpdrgpdgpdpdSdpgrSdpgSdpSdsrgrgpgpdpdS"
    inputString = compressCommas(inputString, 'mohanam')
    print(inputString)
    arr = toNpArray(inputString)
    # findConstPatterns(arr, 'mohanam')
    print(findIncPatterns(arr, 'mohanam'))
    print(findConstPatterns(arr, 'mohanam'))
    # findRhythmPatterns(arr, 'mohanam')
    print("\n***** PROGRAM ENDED *****")
