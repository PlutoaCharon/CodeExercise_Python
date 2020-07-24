def bubbleSort(arr):
    for i in range(len(arr) - 1):
        exchange = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                exchange = True
        if not exchange:
            break
    return arr


if __name__ == '__main__':
    arr = [2, 5, 3, 4, 1]
    ans = bubbleSort(arr)
    print(ans)
