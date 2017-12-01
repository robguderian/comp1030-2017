def isPalndrome(testString):
    # first, clean
    testString = testString.lower()
    cleanString = ""
    for letter in testString:
        if 'a' <= letter and letter <= 'z':
            cleanString = cleanString + letter
    
    isPal = True
    for i in range(0, len(cleanString)):
        # test the first and the last,
        # then the second and secondlast
        if cleanString[i] != cleanString[ len(cleanString) - 1 - i]:
            isPal = False
    return isPal

print(isPalndrome("A man, a plan, a canal: Panama."))
print(isPalndrome("Civic."))
print(isPalndrome("Not even close."))