def right_side_triangle():
    heightStr = raw_input("How tall?")
    height = int(heightStr)
    
    for i in range(0, height):
        for j in range(0, height):
            if j < height - i - 1:
                print " ",
            else:
                print '*',

        # print nothing, then a new line
        print
    
    
def left_side_triange():
    strSize = raw_input("what size? > ")
    intSize = int(strSize)

    for i in range(0, intSize):
        for j in range(0, intSize):
            print "*",

        # print nothing, then a new line
        print
    
def rectangle():
    strSizeX = raw_input("what size for x? > ")
    intSizeX = int(strSizeX)

    strSizeY = raw_input("what size for y? > ")
    intSizeY = int(strSizeY)

    for i in range(0, intSizeX):
        for j in range(0, intSizeY):
            print "*",

        # print nothing, then a new line
        print
    

userInput = raw_input("What would you like to do? Options: rst, lst, rect > ")
while userInput != "quit":
    if userInput == 'rst':
        right_side_triangle()
    elif userInput == 'lst':
        left_side_triange()
    elif userInput == 'rect':
        rect()
    userInput = raw_input("What would you like to do? Options: rst, lst, rect > ")