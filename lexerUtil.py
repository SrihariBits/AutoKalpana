
#Copies the string n times
def copier(str,n):
    string=""
    for i in range(0,n):
        string+=str
    return string

# If constant difference sequence is formed, returns next in sequence, else returns same string
def nextConstDiffSeq(str):
    diff=0
    if len(str)>=2:
        diff=int(str[1]-str[0])
        for i in range(2,len(str)):
            if abs(int(str[i]-str[i-1])) != diff:
                return str
    c = str[len(str)-1] + diff