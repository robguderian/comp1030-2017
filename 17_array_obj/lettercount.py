
try:
    myFile = open("Alice.txt")
    
    alice = myFile.read()
    
    print len(alice)
    
    letters = []
    freq = []
    
    for letter in alice:
        if letter in letters:
            # letter is inside our letters array
            # find its index, and increment the freq of that letter
            index = letters.index(letter)
            freq[index] += 1
        else:
            # we don't know about this letter
            letters.append(letter)
            freq.append(1)
            
        
    
except:
    print "crashy crash"
    

for i in range( 0, len( letters) ):
    print letters[i] + " " + str(freq[i])
    
    
    
    
    
    
    
    
    




