def calcM(data,universe):
    universe_index = {x: i for i, x in enumerate(universe)}
    M = [[0 for x in range(len(data))] for y in range(len(universe))]

    for row, s in enumerate(data):
        for item in s:
            if item in universe_index:
                M[row][universe_index[item]] = 1
    return M

def calcMinI(L,index):
    min_i = -1
    SL = set(L)
    for i,item in enumerate(index):
        if item in SL: # could do this with a set..
            min_i = i
            break
    if min_i == -1:
        breakpoint()
    return min_i

def calcSig(L,indexes):
    return [calcMinI(L,i) for i in indexes]

def calcIndexM(universe_size,nhashes):
    indexes = [[0]*universe_size for _ in range(nhashes)]
    for i in range(nhashes):
        perm = list(range(universe_size))
        random.shuffle(perm)
        indexes[i] = perm
    return indexes
