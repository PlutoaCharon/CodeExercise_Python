def selectSort(arr):
    for i in range(len(arr) - 1):
        minNum = i
        for j in range(i + 1, len(arr)):
            if arr[minNum] > arr[j]:
                minNum = j
        arr[i], arr[minNum] = arr[minNum], arr[i]
    return arr


if __name__ == '__main__':
    arr = [2, 5, 3, 4, 1]
    ans = selectSoft(arr)
    print(ans)
