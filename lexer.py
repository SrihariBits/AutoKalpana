from Past import constructRagaGraph
from Past import constructGrams

def findPatterns(inputList):
    for size in range(2,20):
        for i in range(0,len(inputList)-2*size):
            diff = inputList[i+size:i+2*size]-inputList[i:i+size]
            cnt=0
            while i+2*size<len(inputList) and inputList[i+size:i+2*size]-inputList[i:i+size]==diff:
                cnt+=1
                i+=size
            if cnt>1:
                print(diff)


if __name__== "__main__":
    pass