

letters = "abcd something cool NOW WHAT?!?!?!?!?!?!"


# convert to upper case
newString = ""
for letter in letters:
    # convert it a number
    if letter >= "a" and letter <= "z":
        asNum = ord(letter)
        asNum = asNum - (ord('a') - ord('A'))
        asUpperCase = chr(asNum)
        newString = newString + asUpperCase
    else:
        newString = newString + letter
    
print newString
    