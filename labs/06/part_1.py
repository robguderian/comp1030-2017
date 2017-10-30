import time

def wpm(words, seconds):
    minutes = seconds / float(60)
    calc = words/minutes
    return calc


starttime = time.time()

lastInput = "something"
totalWords = 0

while lastInput != "":
    lastInput = raw_input("Gimme a word > ")
    totalWords += 1

totaltime = time.time() - starttime

print "You typed at %d words per minute" % wpm(totalWords, totaltime)
