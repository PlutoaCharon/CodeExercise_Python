def quickSort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quickSort(arr, left, mid - 1)
        quickSort(arr, mid + 1, right)
    return arr


def partition(arr, left, right):
    tmp = arr[left]
    while left < right:
        while left < right and arr[right] >= tmp:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= tmp:
            left += 1
        arr[right] = arr[left]
    arr[left] = tmp
    return left


if __name__ == '__main__':
    arr = [2, 5, 3, 4, 1]
    ans = quickSort(arr, 0, len(arr) - 1)
    print(ans)
