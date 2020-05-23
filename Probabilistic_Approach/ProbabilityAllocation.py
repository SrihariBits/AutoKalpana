import math
newGraph = {}


def probabilityAllocation(list):
    if len(list) == 1:
        for shingles in list[0]:
            for grams in list[0][shingles][1]:
                list[0][shingles][1][grams] /= list[0][shingles][0]
        return list[0]

    elif len(list) == 2:
        temporaryList = []
        for pairs in list[1]:
            if pairs[1] == 1:
                temporaryList.append(pairs[0])

        for shingles in list[0]:
            count = 0
            for grams in list[0][shingles][1]:
                if grams in temporaryList:
                    list[0][shingles][1][grams] += (
                        list[0][shingles][0]/10)
                    count += 1
            list[0][shingles][0] += (count*(list[0][shingles][0]/10))

        for shingles in list[0]:
            for grams in list[0][shingles][1]:
                list[0][shingles][1][grams] /= list[0][shingles][0]
        return list[0]

    else:
        raise Exception('Invalid length of arguments')


def cummulativeProbability(gramGraph):
    for shingles in gramGraph:
        sum = 0
        for grams in gramGraph[shingles][1]:
            # First 3 decimal places
            sum += int(round(gramGraph[shingles][1][grams], 3)*1000)
            # Assuming random numbers begining from 1
            gramGraph[shingles][1][grams] = sum

    return gramGraph
