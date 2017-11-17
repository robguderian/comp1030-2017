try:
    myFile = open("Alice.txt")
    
    theDoc = myFile.read()
    
    words = theDoc.split()
    print "done split..."
    
    i = 0
    print "going through words"
    while (i < len(words)):
        #if i % 10 == 0:
        #    print words[i]
        if words[i] == "Mr.":
            words[i] = "Mister"
            print "Mr"
        elif words[i] == "Mrs.":
            words[i] = "Misus"
            print "Mrs"
        elif words[i] == "Ms":
            words[i] = "Miz"
            print "Ms"
        elif words[i] == "Alice":
            words[i] ="Clarise"
            print "Alice"
        i += 1
except:
    print "DERP"
finally:
    print "done"

theNewDoc = ' '.join(words)
print theNewDoc








