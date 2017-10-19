
def findMax(theList):
    if len(theList) > 0:
        myMax = theList[0]
        for curr in theList:
            if curr > myMax:
                myMax = curr
    else:
        myMax = -1 # sentinel value saying "bad input"
    return myMax

someList = [1, 2, 3, 4, 100, 2]
theMax = findMax(someList)
print theMax

secondList = []
theMax = findMax(secondList)
print theMax
