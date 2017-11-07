
# calculates x to the power of y
def power(x, y):
    result = 1
    for i in range(0, y):
        result = result * x

print power(2)
