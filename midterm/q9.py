def summer(num):
    total = 0
    while num > 0:
        if num % 2 == 0:
            total += num
        num -= 1
    return total

print summer(4)
print summer(10)
