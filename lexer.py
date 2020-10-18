from Probabilistic_Approach import constructRagaGraph
from Probabilistic_Approach import constructGrams
from ToNpArray import toNpArray
import numpy as np

##########TODO###########
# compress commas (Y)   #
# Yatis  (Y)            #
# tala patterns  (Y)    #
# partition algorithm   #
# combo->const-inc patt #
#########################


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
                while np.all(inputList[i+size+expand:i+2*(size+expand)] == inputList[i:i+size+expand]) and distanceMatrix[inputList[i+2*(size+expand)]][inputList[i+2*(size+expand)+1]] == diff[0]:
                    cnt += 1
                    i = i + size + expand
                    expand += 1
                    if i+2*(size+expand)+1 >= len(inputList):
                        break
            if cnt > 1:
                # (Initial diff, number of increments in len, type)
                print(diff, cnt, 1)
            i += 1
            expand = 0


# Current pattern and next pattern have same CORRESPONDING difference (automatic internal pattern)
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
                # (fixed diff, number of such patterns, type)
                print(diff, cnt, 2)
            i += 1


def rhythmPatternHelper(s):
    # Tha Tha Kita Thi Thi Kita
    if s[0] == s[1] and s[4] == s[5]:
        return True

    # Tha Tha Tha Tha Ki Ta Tha Ka
    elif s[0] == s[1] == s[2] == s[3]:
        return True

    # Tha Tha Ki Ta Ki Ta Tha Ka
    elif s[0] == s[1] and s[2] == s[4] and s[3] == s[5]:
        return True

    # Tha Ka Tha Ri Ki Ta Tha Ka
    elif s[0] == s[2] and s[1] != s[3]:
        return True

    # Tha Ka Thi Mi Tha Ka Ju Nu
    elif s[0] == s[4] and s[1] == s[5]:
        return True

    # Tha Din Din Ki Ki Tha Tha Thom
    elif s[1] == s[2] and s[3] == s[4] and s[5] == s[6]:
        return True

    # Tha Tha Ka Tha Thi Ki Na Thom
    elif s[0] == s[1] == s[3] and s[0] != s[2]:
        return True

    # Tha Ki Ta Tha Ka Tha Ki Ta
    elif s[0] == s[5] and s[1] == s[6] and s[2] == s[7]:
        return True

    # Tha Ki Ta Tha Ki Ta Tha Ka
    elif s[0] == s[3] and s[1] == s[4] and s[2] == s[5]:
        return True

    else:
        return False


# Internal pattern with respect to rhythms (table/mridangam)
def findRhythmPatterns(inputList, raga='mohanam'):
    distanceMatrix = constructRagaGraph(raga)
    size = 8
    i = 0
    while i < len(inputList)-size:
        subpart = inputList[i:i+size]
        diff = [distanceMatrix[subpart[x-1]][subpart[x]]
                for x in range(1, len(subpart), 1)]
        if rhythmPatternHelper(subpart):
            print(diff, 0, 3)
        i += 1


if __name__ == "__main__":
    print("***** PROGRAM STARTED *****\n")
    #inputString = "ggp,p,dpS,S,RSd,d,p,d,pg,g,r,gpdSd,,pg,rrggdpg,pggrs,ggggrgpgp,p,ggdpd,dpS,S,dGRRS,SdSdddpgpdSdpdpggrssrg,g,grpgrrsrsgrsggp,p,dpS,S,"
    inputString = "ssrsrgsrgpsrgpdsrgpds"
    inputString = compressCommas(inputString, 'mohanam')
    print(inputString)
    arr = toNpArray(inputString)
    #findConstPatterns(arr, 'mohanam')
    findIncPatterns(arr, 'mohanam')
    findRhythmPatterns(arr, 'mohanam')
    print("\n***** PROGRAM ENDED *****")
