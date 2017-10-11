
def check_valid(studnum):
    summation = 0
    count = 0
    curr = studnum
    while curr != 0:
        summation = summation + curr % 10
        curr = curr / 10
        count = count + 1

    # guilty until proven innocent
    if summation % 7 == 0 and count == 5:
        isValid = True
    else:
        isValid = False

    return isValid



wasValid = check_valid(12310)
print wasValid

wasValid = check_valid(12311)
print wasValid

wasValid = check_valid(00000)
print wasValid
















