def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        if arr[i] >= arr[j]:
            tmp.append(arr[j])
            j += 1
    while i <= mid:
        tmp.append(arr[i])
        i += 1
    while j <= high:
        tmp.append(arr[j])
        j += 1
    for i in range(low, high + 1):
        arr[i] = tmp[i - low]


def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)
    return arr


if __name__ == '__main__':
    # arr = [2, 5, 3, 4, 1]
    # arr = [3, 2, 1, 9, 7, 8]
    arr = [12, 11, 13, 5, 6, 7]
    ans = mergeSort(arr, 0, len(arr) - 1)
    print(ans)
