def increasingLetters(testString):
    testString = testString.lower()
    parts = testString.split()

    isIncreasing = True
    # prime the loop with the "letter" that is less than 'a'
    # I don't know what it is, so ....
    prev = chr(ord('a') - 1)

    for word in parts:
        # get the first letter
        curr = word[0]
        if prev > curr:
            isIncreasing = False
        prev = curr
    return isIncreasing

print(increasingLetters("apple bees goats zebra"))
print(increasingLetters("this that those"))
print(increasingLetters("Zebra ants"))
    