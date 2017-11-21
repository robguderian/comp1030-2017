
def makeWord(charArray):
    word = ""
    for letter in charArray:
        word = word + chr(letter)
    return word

testArray = [112,121,116,104,111,110]
print makeWord(testArray)
