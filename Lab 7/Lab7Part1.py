import time

def cpm(words, secs):
    charCount = 0
    for line in lines:
        charCount += len(line)
    minutes = secs/60
    return charCount/minutes
    
    

print("Type! Blank line to quit!")
lines = []
lastLine = " "
startTime = time.time()
while lastLine != "":
    lastLine = raw_input("> ")
    lines.append(lastLine)
		
secs = time.time() - startTime


print ("You typed %f chars per minute"%(cpm(lines, secs)))