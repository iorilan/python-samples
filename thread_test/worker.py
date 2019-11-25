import os, math
from multiprocessing import Pool
def powers(x):
    #print(os.getpid()) # enable to watch children
    return 2 ** x
def sqrt (x):
    return math.sqrt(x)
if __name__ == '__main__':
    workers = Pool(processes=5)
    #results = workers.map(sqrt, [2]*50000000)
    #print(results[:16])
    #print(results[-2:])
    results = workers.map(sqrt, range(30000))
    print(results[:16])
    print(results[-2:])