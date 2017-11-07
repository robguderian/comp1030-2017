def ordinal(inputNumber):
    last = inputNumber % 10
    lastTwo = inputNumber % 100
    suffix = "th"

    # special cases
    if lastTwo == 11 or lastTwo == 12 or lastTwo == 13:
        suffix = "th"
    elif last == 2:
        suffix = "nd"
    elif last == 3:
        suffix = "rd"
    return "%i%s" % (inputNumber, suffix)

# test
print ordinal(3)
print ordinal(99)
print ordinal(100)
print ordinal(12)