arr = [1, 2, 3, 4, 5, 6, 7]
for i in range (0, int(len(arr) / 2)):
    temp = arr[len(arr) - 1 - i]
    arr[len(arr) - 1 - i] = arr[i]
    arr[i] = temp
print(arr)