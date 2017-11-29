# function that reads a file, returns a count
# of the words that match

def getWords(theWordToCheckFor):
    myFile = open("../16_try_join/Alice.txt")
    contents = myFile.read()
    parts = contents.split()
    for word in parts:
        if word == theWordToCheckFor:
            count += 1
    

theCount = getWords("Alice")
print(theCount)
