import multiprocessing
import time

def doAThing(i):
    time.sleep(i)
    

pool = multiprocessing.Pool()

print pool.map(doAThing, range(10))
