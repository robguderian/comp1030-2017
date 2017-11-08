try:
    num = int(raw_input("Number > "))
    thing = 1/0
except ValueError as problem:
    print "there was a number problem!"
    print problem
except ZeroDivisionError as zde:
    print "you divided by zero"
    print zde