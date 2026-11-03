from .listr import calcSigM,calcM
from .gen import gen_data

def lsh(data_size,sigM,band_size,bucket_size):
    for i in range(0,data_size,band_size):
        # use a single hash func for entire band.
        buckets = [None]*bucket_size
        a = random.randrange(1,band_size)
        b = random.randrange(0,band_size)
        for row in range(i,i+band_size):
            
if __name__=='__main__':
    dataM = calcM(data)
    sigM = calcSigM()
    
