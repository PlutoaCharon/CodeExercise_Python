def mergeSort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


if __name__ == '__main__':
    # arr = [2, 5, 3, 4, 1]
    # arr = [3, 2, 1, 9, 7, 8]
    arr = [12, 11, 13, 5, 6, 7]
    ans = mergeSort(arr)
    print(ans)
