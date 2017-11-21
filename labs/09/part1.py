
try:
    myFile = open("testfile.txt")
    wordCount = 0
    lineCount = 0
    letterCount = 0
    for line in myFile:
        wordsInThisLine = line.split()
        wordCount += len(wordsInThisLine)

        lineCount += 1

        # count letters. Iterate through the array of letters
        for letter in line:
            if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
                letterCount += 1
except IOError as ioe:
    print ioe
    print "Everything has gone very wrong"


print "Word count " + str(wordCount)
print "Line count " + str(lineCount)
print "Letter count " + str(letterCount)
