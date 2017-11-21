
def sumOfLetters(theString):
    total = 0
    for letter in theString:
        total += ord(letter)
    return total

print sumOfLetters("a")
print sumOfLetters("Some words")

# prints 49, because that's the ascii value of the 
# character "1"
print sumOfLetters("1")
