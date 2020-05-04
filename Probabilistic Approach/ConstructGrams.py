from BeautyScore import beautyScore_8, beautyScore_16


def constructGrams(inputNotes, distanceMatrix):
    print("input: " + inputNotes)
    twoGrams = []
    twoGramGraph = {}
    # NON-INTERSECTING
    #####################################################################################################
    shingle = ""
    prev_shingle = ""
    # Two grams
    for begin in range(2):  # two possible beginnings
        for i in range(begin, len(inputNotes)-1, 2):  # step=2
            shingle = inputNotes[i:i+2]
            if (len(shingle) == 2):
                if shingle not in twoGrams:
                    twoGrams.append(shingle)  # Required?
                    twoGramGraph[shingle] = []
                    # Counts number of occurences
                    twoGramGraph[shingle].append(1)
                    twoGramGraph[shingle].append({})
                    if i != begin:
                        # initialise with 1
                        twoGramGraph[prev_shingle][1][shingle] = 1
                else:
                    twoGramGraph[shingle][0] += 1
                    try:
                        if i != begin:
                            # Or add 1 if already exist
                            twoGramGraph[prev_shingle][1][shingle] += 1
                    except KeyError:
                        twoGramGraph[prev_shingle][1][shingle] = 1
            prev_shingle = shingle

    '''
    for shingle in twoGrams:
        print(twoGramGraph[shingle])
    '''
    #######################################################################################################
    fourGrams = []
    fourGramGraph = {}

    shingle = ""
    prev_shingle = ""
    # Four grams
    for begin in range(4):  # four possible beginnings
        for i in range(begin, len(inputNotes)-3, 4):  # step=4
            shingle = inputNotes[i:i+4]
            if (len(shingle) == 4):
                if shingle not in fourGrams:
                    fourGrams.append(shingle)
                    fourGramGraph[shingle] = []
                    # Counts number of occurences
                    fourGramGraph[shingle].append(1)
                    fourGramGraph[shingle].append({})
                    if i != begin:
                        # initialise with 1
                        fourGramGraph[prev_shingle][1][shingle] = 1
                else:
                    fourGramGraph[shingle][0] += 1
                    try:
                        if i != begin:
                            # Or add 1 if already exist
                            fourGramGraph[prev_shingle][1][shingle] += 1
                    except KeyError:
                        fourGramGraph[prev_shingle][1][shingle] = 1
            prev_shingle = shingle

    '''
    for shingle in fourGrams:
        print(fourGramGraph[shingle])
    '''
    #####################################################################################################
    eightGrams = []
    eightGramGraph = {}

    shingle = ""
    prev_shingle = ""
    # Eight grams
    for begin in range(8):  # eight possible beginnings
        for i in range(begin, len(inputNotes)-7, 8):  # step=8
            shingle = inputNotes[i:i+8]
            if (len(shingle) == 8):
                if (shingle,) not in eightGrams:
                    score = beautyScore_8(shingle)
                    eightGrams.append((shingle, score))
                    eightGramGraph[shingle] = []
                    # Counts number of occurences
                    eightGramGraph[shingle].append(1)
                    eightGramGraph[shingle].append({})
                    if i != begin:
                        # initialise with 1
                        eightGramGraph[prev_shingle][1][shingle] = 1
                else:
                    eightGramGraph[shingle][0] += 1
                    try:
                        if i != begin:
                            # Or add 1 if already exist
                            eightGramGraph[prev_shingle][1][shingle] += 1
                    except KeyError:
                        eightGramGraph[prev_shingle][1][shingle] = 1
            prev_shingle = shingle

    '''
    for shingle in eightGrams:
        print(eightGramGraph[shingle])
    '''
    ####################################################################################################
    sixteenGrams = []
    sixteenGramGraph = {}

    shingle = ""
    prev_shingle = ""
    # Sixteen grams
    for begin in range(16):  # sixteen possible beginnings
        for i in range(begin, len(inputNotes)-15, 16):  # step=16
            shingle = inputNotes[i:i+16]
            if (len(shingle) == 16):
                if (shingle,) not in sixteenGrams:
                    score = beautyScore_16(shingle, distanceMatrix)
                    sixteenGrams.append((shingle, score))
                    sixteenGramGraph[shingle] = []
                    # Counts number of occurences
                    sixteenGramGraph[shingle].append(1)
                    sixteenGramGraph[shingle].append({})
                    if i != begin:
                        # initialise with 1
                        sixteenGramGraph[prev_shingle][1][shingle] = 1
                else:
                    sixteenGramGraph[shingle][0] += 1
                    try:
                        if i != begin:
                            # Or add 1 if already exist
                            sixteenGramGraph[prev_shingle][1][shingle] += 1
                    except KeyError:
                        sixteenGramGraph[prev_shingle][1][shingle] = 1
            prev_shingle = shingle

    '''
    for shingle in sixteenGrams:
        print(sixtenGramGraph[shingle])
    '''
    return twoGrams, twoGramGraph, fourGrams, fourGramGraph, eightGrams, eightGramGraph, sixteenGrams, sixteenGramGraph
