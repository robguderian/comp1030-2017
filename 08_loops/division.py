

strInput = raw_input("Gimme a numba! > ")
check = int (strInput)
count = 0

for i in range(1, check):
    print i
    if check % i == 0:
        count = count + 1

print "result : " + str(count)

