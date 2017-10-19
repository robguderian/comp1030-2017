
# find an element

def find(theList, findThis):
    inList = False
    for element in theList:
        if findThis == element:
            inList = True
    return inList
            

someList = [22, 434, 23, 23 ,65987]


print find(someList, 22)
print find(someList, -1)
print find(someList, 65987)
