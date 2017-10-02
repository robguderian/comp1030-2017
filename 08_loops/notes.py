
x = 120

loopCounter = 1

# while this number is not 0
while x > 0:
    print "%d | %d" % (loopCounter, x)
    # keep dividing by 10
    x = x / 10
    
    # increment the loop count
    loopCounter = loopCounter + 1

print "Result is " + str(loopCounter)
