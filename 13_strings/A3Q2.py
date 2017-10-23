import random

def question(lowest, highest):
    inputStr = raw_input("Make a guess. %d < _ < %d :"% (lowest, highest))
    return int(inputStr)

lowest = 0
highest = 101
rando = random.randint(0, 100)
guess = -1
numGuesses = 0

while guess != rando:
    guess = question(lowest, highest)
    numGuesses += 1
    if guess > rando:
        print "too high"
        if guess < highest:
            highest = guess
    elif guess < rando:
        print "too low"
        if guess > lowest:
            lowest = guess
    
print "You got it in %d guesses!"%numGuesses