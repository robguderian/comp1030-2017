startStr = raw_input("Where to start? > ")
endStr = raw_input("Where to end? > ")
byStr = raw_input("Count by > ")

start = int(startStr)
end = int (endStr)
by = int(byStr)

# awesome solution
print range(start, end, by)

# actual solution
curr = start
while curr < end:
    print curr
    curr += by