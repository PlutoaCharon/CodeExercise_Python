arr = [1, 1, 2, 3, 4, 4, 3]
tmp = arr[0]
for i in range(1, len(arr)):
    tmp = tmp ^ arr[i]

print(tmp)