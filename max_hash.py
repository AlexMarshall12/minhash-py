import random

def gen_list(low,high,size):
    return [random.randint(low,high) for _ in range(size)]

# Generate Random Data
def gen_data(universe,list_size,data_size):
    data = [[] for _ in range(data_size)]
    u_min = min(universe)
    u_max = max(universe)
    for i in range(data_size):
        data[i] = gen_list(u_min,u_max,list_size)
    return data

def gen_index(l):
    return random.shuffle(l.copy()) 

def calcM(data,universe):
    universe_index = {x: i for i, x in enumerate(universe)}
    M = [[0 for x in range(len(data))] for y in range(len(universe))]

    for row, s in enumerate(data):
        for item in s:
            if item in universe_index:
                M[row][universe_index[item]] = 1
    return M

def calcMaxI(L,index):
    max_i = -1
    SL = set(L)
    for i,item in enumerate(reversed(index)):
        if item in SL:
            max_i = i
            break
    if max_i == -1:
        raise Exception("Could not find MaxIndex in given list")
    return max_i

def calcSig(L,indexes):
    return [calcMaxI(L,i) for i in indexes]

def calcIndexM(universe_size,nhashes):
    indexes = [[0]*universe_size for _ in range(nhashes)]
    for i in range(nhashes):
        perm = list(range(universe_size))
        random.shuffle(perm)
        indexes[i] = perm
    return indexes

def listCompare(L,R):
    """ Naive Comparison """
    setL = set(L)
    setR = set(R)
    return len(setL & setR)/len(setL | setR)

def closestList(L,data):
    """ uses list compare """
    return max(range(len(data)), key = lambda i: listCompare(L, data[i]))

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

def gen_universe(size):
    return list(range(size))

import time
if __name__=="__main__":
    UNIVERSE_SIZE = 100
    DATA_SIZE = 1000
    LIST_SIZE = 12
    N_HASHES = 128
    universe = gen_universe(UNIVERSE_SIZE)
    data = gen_data(universe,LIST_SIZE,DATA_SIZE)
    indexM = calcIndexM(UNIVERSE_SIZE,N_HASHES)
    signatures = [calcSig(d,indexM) for d in data]
    
    newList = gen_list(0,UNIVERSE_SIZE-1,LIST_SIZE)
    newListSig = calcSig(newList,indexM)
    
    start = time.perf_counter()
    closestList = closestList(newList,data)
    mid = time.perf_counter()
    closestList2 = closestListMH(newListSig,signatures)
    end = time.perf_counter()
    print(f"list compare time: {mid-start:.6f} seconds")
    print(f"minHash compare time: {end-mid:.6f} seconds")

    print(closestList)
    print(closestList2)

    
    
    



