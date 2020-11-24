from collections import deque
from Probabilistic_Approach import constructRagaGraph
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

'''
def accepted(function, inputList, raga):
    if function == 'increasing':
        outputList = findIncPatterns(inputList, raga)
        if len(outputList) == 1 and outputList[0][0] == -1:
            return True
        else:
            return False
    elif function == 'decreasing':
        outputList = findDecPatterns(inputList, raga)
        if len(outputList) == 1 and outputList[0][0] == -1:
            return True
        else:
            return False
    elif function == 'constant':
        outputList = findConstPatterns(inputList, raga)
        if len(outputList) == 1 and outputList[0][0] == -1:
            return True
        else:
            return False
    elif function == 'rhythm':
        outputList = findRhythmPatterns(inputList, raga)
        if len(outputList) == 1 and outputList[0][0] == -1:
            return True
        else:
            return False
    elif function == 'partition':
        outputList = findPartitionPatterns(inputList, raga)
        if len(outputList) == 1 and outputList[0][0] == -1:
            return True
        else:
            return False
'''


def value(inputlist, raga):
    l = len(inputlist)
    if l > 20:
        return l
    if isIncreasing(inputlist, raga):
        return 1.5*(l**1.5)
    elif isDecreasing(inputlist, raga):
        return 1.5*(l**1.5)
    elif isConstant(inputlist, raga):
        return 1.4*(l**1.5)
    elif isRhythm(inputlist, raga):
        return 1.3*(l**1.5)
    elif isPartition(inputlist, raga):
        return 1.2*(l**1.5)
    else:
        return l


def Compare(list1, list2):
    if(len(list1) != len(list2)):
        return False
    for i in range(len(list1)):
        if(list1[i] != list2[i]):
            return False
    return True

# replace commas with previous character


def compressCommas(inputString, raga):
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
def findIncPatterns(inputList, raga):
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
            diff = [distanceMatrix[subpart[x-1]-1][subpart[x]-1]
                    for x in range(1, len(subpart))]
            cnt = 0
            diff = np.array(diff)
            try:
                diff.astype(int)
            except:
                print(diff, i, size, expand, subpart)
            start = i
            if np.min(diff) == np.max(diff):
                while (i+2*(size+expand) < len(inputList) and i+size+expand < len(inputList) and Compare(inputList[i+size+expand:i+2*(size+expand)], inputList[i:i+size+expand]) and distanceMatrix[inputList[i+2*(size+expand)-1]-1][inputList[i+2*(size+expand)]-1] == diff[0]) or (i+2*(size+expand)+1 <= len(inputList) and i+size+expand+1 < len(inputList) and Compare(inputList[i+size+expand+1:i+2*(size+expand)+1], inputList[i:i+size+expand]) and distanceMatrix[inputList[i+size+expand]-1][inputList[i+size+expand+1]-1] == diff[0]):
                    cnt += 1
                    i = i + size + expand
                    expand += 1
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
            newlist = list(inputList[i:])
            if newlist:
                retlist.append(newlist)
            return retlist
    if not retlist:
        return [inputList]
    return retlist


def isIncreasing(inputList, raga):
    if len(inputList) <= 2:
        return False
    distanceMatrix = constructRagaGraph(raga)
    for size in range(2, 6, 1):
        i = 0
        expand = 0
        if i + size + expand <= len(inputList):
            subpart = inputList[i:i+size+expand]
            diff = [distanceMatrix[subpart[x-1]-1][subpart[x]-1]
                    for x in range(1, len(subpart))]
            diff = np.array(diff)
            diff.astype(int)
            while (i+2*(size+expand) < len(inputList) and i+size+expand < len(inputList) and Compare(inputList[i+size+expand:i+2*(size+expand)], inputList[i:i+size+expand]) and distanceMatrix[inputList[i+2*(size+expand)-1]-1][inputList[i+2*(size+expand)]-1] == diff[0]) or (i+2*(size+expand)+1 <= len(inputList) and i+size+expand+1 < len(inputList) and Compare(inputList[i+size+expand+1:i+2*(size+expand)+1], inputList[i:i+size+expand]) and distanceMatrix[inputList[i+size+expand]-1][inputList[i+size+expand+1]-1] == diff[0]):
                i = i + size + expand
                expand += 1
            if i+size+expand == len(inputList):
                return True
    return False


# Gopuchha and Strotovaha Yati - starts from all positions in string, with fixed 6-2
# initial pattern string having fixed internal difference, also decreasing
# in length in further patterns
def findDecPatterns(inputList, raga):
    distanceMatrix = constructRagaGraph(raga)
    retlist = []
    newlist = []
    found = False
    for size in range(6, 2, -1):
        i = 0
        expand = 0
        newlist = []
        while i + size - expand <= len(inputList):
            subpart = inputList[i:i+size-expand]
            diff = [distanceMatrix[subpart[x-1]-1][subpart[x]-1]
                    for x in range(1, len(subpart))]
            cnt = 0
            diff = np.array(diff)
            try:
                diff.astype(int)
            except:
                print(diff)
            start = i
            if np.min(diff) == np.max(diff) and i+2*(size-expand)-1 <= len(inputList):
                while Compare(inputList[i+size-expand:i+2*(size-expand)-1], inputList[i:i+size-expand-1]) or Compare(inputList[i+size-expand:i+2*(size-expand)-1], inputList[i+1:i+size-expand]):
                    cnt += 1
                    i = i + size - expand
                    expand += 1
                    if expand >= size or i+2*(size-expand)-1 > len(inputList):
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
            newlist = list(inputList[i:])
            if newlist:
                retlist.append(newlist)
            return retlist
    if not retlist:
        return [inputList]
    return retlist


def isDecreasing(inputList, raga):
    if len(inputList) <= 2:
        return False
    distanceMatrix = constructRagaGraph(raga)
    for size in range(6, 2, -1):
        i = 0
        expand = 0
        if i + size - expand <= len(inputList):
            subpart = inputList[i:i+size-expand]
            diff = [distanceMatrix[subpart[x-1]-1][subpart[x]-1]
                    for x in range(1, len(subpart))]
            diff = np.array(diff)
            diff.astype(int)
            if i+2*(size-expand)-1 <= len(inputList):
                while Compare(inputList[i+size-expand:i+2*(size-expand)-1], inputList[i:i+size-expand-1]) or Compare(inputList[i+size-expand:i+2*(size-expand)-1], inputList[i+1:i+size-expand]):
                    i = i + size - expand
                    expand += 1
                    if expand >= size or i+2*(size-expand)-1 > len(inputList):
                        break
                if i+size-expand == len(inputList):
                    return True
    return False


# Current pattern and next pattern have same CORRESPONDING difference (automatic internal pattern)
def findConstPatterns(inputList, raga):
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
            diff = [distanceMatrix[subpartB[x]-1][subpartA[x]-1]
                    for x in range(len(subpartA))]
            cnt = 0
            currdiff = diff
            start = i
            while i+2*size <= len(inputList) and currdiff == diff:
                cnt += 1
                i += size
                subpartA = inputList[i+size: i+2*size]
                subpartB = inputList[i: i+size]
                currdiff = [distanceMatrix[subpartB[x]-1][subpartA[x]-1]
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
            newlist = list(inputList[i:])
            if newlist:
                retlist.append(newlist)
            return retlist
    if not retlist:
        return [inputList]
    return retlist


def isConstant(inputList, raga):
    if len(inputList) <= 2:
        return False
    distanceMatrix = constructRagaGraph(raga)
    for size in range(6, 2, -1):
        i = 0
        if i <= len(inputList)-2*size:
            subpartA = inputList[i+size:i+2*size]
            subpartB = inputList[i:i+size]
            diff = [distanceMatrix[subpartB[x]-1][subpartA[x]-1]
                    for x in range(len(subpartA))]
            currdiff = diff
            cnt = 0
            while i+2*size <= len(inputList) and currdiff == diff:
                cnt += 1
                i += size
                subpartA = inputList[i+size: i+2*size]
                subpartB = inputList[i: i+size]
                currdiff = [distanceMatrix[subpartB[x]-1][subpartA[x]-1]
                            for x in range(len(subpartA))]
            if i+size == len(inputList) and cnt > 1:
                return True
    return False


# Internal pattern with respect to rhythms (tabla/mridangam)
def findRhythmPatterns(inputList, raga):
    retlist = []
    newlist = []
    size = 8
    i = 0
    while i <= len(inputList)-size:
        subpart = inputList[i: i+size]
        #diff = [distanceMatrix[subpart[x-1]-1][subpart[x]-1] for x in range(1, len(subpart), 1)]
        if rhythmPatternHelper(subpart):
            if newlist:
                retlist.append(newlist)
            newlist = list(inputList[i:i+8])
            newlist.append(-1)
            newlist.insert(0, -1)
            retlist.append(newlist)
            newlist = []
            i += 8
            continue
        newlist.append(inputList[i])
        i += 1
    newlist = list(inputList[i:])
    if newlist:
        retlist.append(newlist)
    if not retlist:
        return [inputList]
    return retlist


def isRhythm(inputList, raga):
    if len(inputList) == 8:
        return rhythmPatternHelper(inputList)
    else:
        return False


# Patterns formed as a partition of number (5,6,7 or 8 for now)
def findPartitionPatterns(inputList, raga):
    retlist = []
    newlist = []
    p_found = False
    for n in range(8, 4, -1):
        distanceMatrix = constructRagaGraph(raga)
        p_list = partitionHelper(n)
        i = 0
        sol = []
        while i <= len(inputList)-n:
            subpart = inputList[i: i+n]
            last = 0
            pat_found = False
            for partitions in p_list:
                found = True
                for partition in partitions:
                    subsubpart = subpart[last: last+partition]
                    diff = [distanceMatrix[subsubpart[x-1]-1][subsubpart[x]-1]
                            for x in range(1, len(subsubpart), 1)]
                    if np.min(diff) >= -1 and np.max(diff) <= 1:
                        last += partition
                    else:
                        found = False
                        last = 0
                        break
                if found:
                    if newlist:
                        retlist.append(newlist)
                    newlist = list(inputList[i:i+n])
                    newlist.append(-1)
                    newlist.insert(0, -1)
                    retlist.append(newlist)
                    newlist = []
                    i += n
                    p_found = True
                    pat_found = True
                    break
            if p_found and i > len(inputList)-n:
                if newlist:
                    retlist.append(newlist)
                newlist = list(inputList[i:])
                if newlist:
                    retlist.append(newlist)
                return retlist
            if pat_found:
                continue
            newlist.append(inputList[i])
            i += 1
    if not retlist:
        return [inputList]
    return retlist


def isPartition(inputList, raga):
    distanceMatrix = constructRagaGraph(raga)
    n = len(inputList)
    if n > 8 or n < 5:
        return False
    p_list = partitionHelper(n)
    subpart = inputList
    last = 0
    for partitions in p_list:
        found = True
        for partition in partitions:
            subsubpart = subpart[last: last+partition]
            diff = [distanceMatrix[subsubpart[x-1]-1][subsubpart[x]-1]
                    for x in range(1, len(subsubpart), 1)]
            if np.min(diff) >= -1 and np.max(diff) <= 1:
                last += partition
            else:
                found = False
                last = 0
                break
        if found:
            return True
    return False


def lexerDP(inputString, raga, printPat=False):
    inputString = compressCommas(inputString, raga)
    arr = toNpArray(inputString, raga)
    lookup = {}

    dp = [[0, -1] for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = value(arr[0:i+1], raga)
    for i in range(len(arr)):
        if i % 50 == 0:
            print('check: ', i)
        for j in range(i-20, i):
            if j < 0:
                continue
            val = 0
            string = str(arr[j+1:i+1])
            if string in lookup:
                val = lookup[string]
            else:
                val = value(arr[j+1:i+1], raga)
                lookup[string] = val
            if dp[j][0] + val > dp[i][0]:
                dp[i][0] = dp[j][0] + val
                dp[i][1] = j
    p = len(arr)-1
    result = []
    while p != -1:
        newp = dp[p][1]
        result.insert(0, list(arr[newp+1:p+1]))
        p = newp
    print(result)
    return result


def lexer(inputString, raga, printPat=False):
    '''
    print("***** PROGRAM STARTED *****\n")
    inputString = "ggp,p,dpS,S,RSd,d,p,d,pg,g,r,gpdSd,,pg,rrggdpg,pggrs,ggggrgpgp,p,ggdpd,dpS,S,dGRRS,SdSdddpgpdSdpdpggrssrg,g,grpgrrsrsgrsggp,p,dpS,S,"
    inputString = "srgpdrgpdgpdpdSdpgrSdpgSdpSdsrgrgpgpdpdS"
    '''
    inputString = compressCommas(inputString, raga)
    arr = toNpArray(inputString, raga)

    '''
    print(arr)
    print()
    print(inputString)
    print()
    '''
    stack = deque()
    stack.append(arr)
    result = []
    while stack:
        top = stack.pop()
        if top[0] == -1:
            result.append(top)
        else:
            ret_list = findIncPatterns(top, raga)
            if len(ret_list) == 1 and ret_list[0][0] != -1:
                ret_list = findDecPatterns(top, raga)
                if len(ret_list) == 1 and ret_list[0][0] != -1:
                    ret_list = findConstPatterns(top, raga)
                    if len(ret_list) == 1 and ret_list[0][0] != -1:
                        ret_list = findRhythmPatterns(top, raga)
                        if len(ret_list) == 1 and ret_list[0][0] != -1:
                            ret_list = findPartitionPatterns(top, raga)
                            if len(ret_list) == 1 and ret_list[0][0] != -1:
                                top.append(-1)
                                top.insert(0, -1)
                                ret_list = [top]
                                if printPat:
                                    print("6", end=' ')
                            else:
                                if printPat:
                                    print("5", end=' ')
                        else:
                            if printPat:
                                print("4", end=' ')
                    else:
                        if printPat:
                            print("3", end=' ')
                else:
                    if printPat:
                        print("2", end=' ')
            else:
                if printPat:
                    print("1", end=' ')
            ret_list.reverse()
            for l in ret_list:
                stack.append(l)
    return result
    #print("\n***** PROGRAM ENDED *****")


if __name__ == "__main__":
    ragam = "kalyani"
    inputString = "ggp,p,dpS,S,RSd,d,p,d,pg,g,r,gpdSd,,pg,rrggdpg,pggrs,ggggrgpgp,p,ggdpd,dpS,S,dGRRS,SdSdddpgpdSdpdpggrssrg,g,grpgrrsrsgrsggp,p,dpS,S,"
    #inputString = "Sndpm,g,rnSdnSndpm,pmgmrS,SndpmpmgmrgnnS,SSnSRRSn,,,SRGGRSndGRSnRSndnSndpm,ndpmgmp,pmpdnS,Snndpmp,dmdnsgrsn,snsndpm,,GRS,RSn,Snd,ndp,gmpgmp,,mpd,,dnd,,g,mpdnSndpmpdnSRGR,SndGRSndNRSndnsndpms,,sndpmpdnsGRSN,nSRSndpmgmpdn,,SRGRSndpmpdnSRGRSndpmgmpdnSnSndpmgmpdnS,GRSndn,RSndpd,Sndpmp,ndpdnS,GRSnd,RSndp,S,Sndpmgr,gmpdnS,d,nSRGRSn,SRSndpd,P,dnSGRSn,D,nSRGMGRn,GRSnSGRS,GRSnSRSndn"
    #inputString = "srsrgsrgm,"
    print(lexerDP(inputString, ragam, True))
