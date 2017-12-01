# has a bug of with empty string. You can fix that :)
def averageLength(theString):
    # question does not ask to clean. We could...
    words = theString.split()
    numberOfLetters = 0
    numberOfWords = 0
    # to get the average, we need the sum of letters, and the count of words
    for word in words:
        numberOfLetters += len(word)
        numberOfWords += 1
    
    return numberOfLetters/numberOfWords

print(averageLength("words words words"))
print(averageLength("a be the"))