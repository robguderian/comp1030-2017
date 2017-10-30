
oldStr = raw_input("Give me a sentence > ")

# solution 1
newStr1 = ""
for i in range( len(oldStr) -1, -1, -1 ):
    newStr1 = newStr1 + oldStr[i]
print newStr1


# solution2
newStr2 = ""
for i in reversed( range(0, len(oldStr))):
    newStr2 = newStr2 + oldStr[i]
print newStr2

# solution 3
newStr3 = reversed(oldStr)
print ''.join(reversed(oldStr))

# solution 4, and what I'd expect from most people
newStr4 = ""
curr = len(oldStr) - 1
while curr >= 0:
    newStr4 = newStr4 + oldStr[curr]
    curr = curr - 1
print newStr4