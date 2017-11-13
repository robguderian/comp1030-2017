
try:
    filename = raw_input("Gimme a filename: > ")

    myFile = open(filename)

    count = 0
    allTheText = myFile.read()
    
    for line in allTheText.split('\n'):
        print line
        count += 1
        if count >  5:
            # stop our for loop
            break
except IOError:
    print "IO ERROR!"