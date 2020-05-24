import numpy as np
from Dictionary import dictionary


def toNpArray(inputString, raga='mohanam'):
    toVal = dictionary[raga]
    arr = np.array([])
    for i in range(0, len(inputString)):
        arr = np.append(arr, [toVal[inputString[i]]])
    return arr.astype(int)
