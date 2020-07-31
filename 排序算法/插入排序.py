def insertSort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
    return arr


if __name__ == '__main__':
    arr = [2, 5, 3, 4, 1]
    ans = insertSort(arr)
    print(ans)
