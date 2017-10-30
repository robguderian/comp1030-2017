
firstString = raw_input("First number? > ")
secondString = raw_input("Second number? > ")
calcType = raw_input("calculation to do? > ")
calcType = calcType.lower()

first = int(firstString)
second = int(secondString)

if calcType == "addition":
    print firstString + " + " + secondString + " = " + str(first + second)
elif calcType == "subtraction":
    print firstString + " - " + secondString + " = " + str(first - second)
elif calcType == "division":
    print firstString + " / " + secondString + " = " + str(first / second)
elif calcType == "multiplcation":
    print firstString + " * " + secondString + " = " + str(first * second)
elif calcType == "modulo":
    print firstString + " % " + secondString + " = " + str(first % second)
else:
    print "I can't do that"
