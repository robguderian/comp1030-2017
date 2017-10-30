import random
myRandomNumber = random.randint(1, 100)
guess = -1 # out-of-range, will run loop

# cheat....
print myRandomNumber

numberGuesses = 0

while (guess != myRandomNumber):
    guessString = raw_input("Guess the number? > ")
    guess = int(guessString)
    numberGuesses += 1
    if guess > myRandomNumber:
        print "Too high"
    elif guess < myRandomNumber:
        print "Too low"
    else:
        print "Winner!"

print "took %d turns"%numberGuesses
