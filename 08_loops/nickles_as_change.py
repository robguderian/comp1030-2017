
# yes, we could divide by five.....

# how many nickles are in 'target'
target = 24

current = 0  # current values we've added up to
tally = 0    # the loop counter

# do I want to give you another nickle?
# if I give you another nickle, have I given you
# too much?
while (current + 5 <= target):
    tally += 1
    current += 5

print "you need " + str(tally) + " nickles"

