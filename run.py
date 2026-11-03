from . import *

def run_permutation_mh():
    UNIVERSE_SIZE = 100
    DATA_SIZE = 1000
    LIST_SIZE = 12
    N_HASHES = 256
    universe = gen_universe(UNIVERSE_SIZE)
    data = gen_data(universe,LIST_SIZE,DATA_SIZE)
    dataM = calcM(data,universe)

def run_hash_mh():
    data = gen_data(universe,LIST_SIZE,DATA_SIZE)
    dataM = calcM(data,universe)    

def run_lsh():
    data = gen_data(universe,LIST_SIZE,DATA_SIZE)
    dataM = calcM(data,universe)    
    dataM = calcM(data)
    sigM = calcSigM(dataM)
    

if __name__=="__main__":




