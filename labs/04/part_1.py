

heightString = raw_input("How tall? > ")
height = int(heightString)

# this actually doubles it, but was the accepted answer

for i in range (0, height):
    for j in range (0, i + 1):
        print "*",
    print

for i in range (0, height):
    for j in range (i, height):
        print "*",
    print
        


# now for half height
# get around integer division
half = height / 2 + height % 2
for i in range (0, half):
    for j in range (0, i + 1):
        print "*",
    print

for i in range (0, height / 2):
    for j in range (i, height/2):
        print "*",
    print
        


