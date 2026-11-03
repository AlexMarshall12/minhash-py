import random

def gen_universe(size):
    return list(range(size))

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
