import time

def wpm(words, seconds):
    charCount = 0
    for w in words:
        charCount += len (w)
    minutes = seconds / float(60)
    calc = charCount/minutes
    return calc


starttime = time.time()

lastInput = "something"
words = []
totalWords = 0

while lastInput != "":
    lastInput = raw_input("Gimme a word > ")
    words.append(lastInput)
    totalWords += 1

totaltime = time.time() - starttime

print "You typed at %d characters per minute" % wpm(words, totaltime)
