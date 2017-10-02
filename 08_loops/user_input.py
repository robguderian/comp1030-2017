

# pre-load a loop
text = raw_input("what do you want to do? > ")

# while they have not said quit, echo
while text != "quit" :
    print text
    text = raw_input("what do you want to do? > ")

    
print "Bye!"

####
# booleans
####

done = False
while not done:
    text = raw_input("what do you want to do? > ")
    if text == "quit":
        done = True
    else:
        print text

print "Bye #2"
    




    
