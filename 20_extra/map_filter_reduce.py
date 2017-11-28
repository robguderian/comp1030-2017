
# map
orig = [1, 2, 3, 4, 10, 42, 9001]

def multiplyByTen( numberIn ):
    return numberIn * 10

first = map(multiplyByTen, orig)

print first

def filterOdd( numberIn ):
    return numberIn % 2 == 0

filtered = filter(filterOdd, orig)
print filtered

def doASum(first, second):
    return first + second

reduced = reduce(doASum, orig)
print reduced
