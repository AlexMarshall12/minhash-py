def closestList(L,data):
    """ uses list compare """
    return max(range(len(data)), key = lambda i: listCompare(L, data[i]))

def listCompareC(L,R):
    """ Uses fast C functions """ 
    setL = set(L)
    setR = set(R)
    return len(setL & setR)/len(setL | setR)

def listCompare(L, R):
    """Pure Python Jaccard similarity."""
    setL = set(L)
    setR = set(R)
    
    intersection = 0
    for x in setL:
        if x in setR:
            intersection += 1

    union = len(setL)
    for x in setR:
        if x not in setL:
            union += 1
    return intersection / union

def minHashCompare(L,R):
    total = 0.0
    assert len(L) == len(R)
    for h in range(len(L)): # this is capped by number of hashes...
        if L[h] == R[h]:
            total+=1.0
    return total/len(L)

def closestListMH(list_signature,signatures):
    """ uses MH compare """
    maxScore = -1.0
    maxI = -1

    for i,sig in enumerate(signatures):
        simScore = minHashCompare(list_signature,sig)
        if simScore > maxScore:
            maxI = i
            maxScore = simScore
    return maxI

