import time

def doAThing(i):
    time.sleep(i)
    

map(doAThing, range(10))
