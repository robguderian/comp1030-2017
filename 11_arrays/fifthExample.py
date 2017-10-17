
listOfStrings = ["Nibbler", "Bender", "Fry", "Leela"]

del listOfStrings[0]

print listOfStrings

# delete nibbler
removedFromList = listOfStrings.pop(0)
print listOfStrings
print "we removed " + removedFromList

removedFromList = listOfStrings.pop()
print listOfStrings
print "we removed with no arguments: " + removedFromList
