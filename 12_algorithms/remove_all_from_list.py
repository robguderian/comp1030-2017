
theList = [ 1, 1, 1, 1, 1, 2, 3, 1, 100]

toRemove = 1

print "Beginning: ",
print theList

while toRemove in theList:
    theList.remove(toRemove)
    print theList

print "final: " + str(theList)
