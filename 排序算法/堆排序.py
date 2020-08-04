def heapify(arr, i, n):
    left = 2 * i + 1  # 左子树
    right = 2 * i + 2  # 右子树
    max = i
    if left < n and arr[left] > arr[max]:
        max = left
    if right < n and arr[right] > arr[max]:
        max = right

    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        heapify(arr, max, n)


def heapSort(arr):
    n = len(arr)
    # 这里n // 2 - 1求最后一个非叶节点
    # 1. 构造堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    # 2. 挨个出数
    for length in range(n - 1, -1, -1):
        arr[length], arr[0] = arr[0], arr[length]
        heapify(arr, 0, length)
        # heapify(arr, 0, length - 1)  错误！

    return arr


if __name__ == '__main__':
    # arr = [2, 5, 3, 4, 1]
    # arr = [3, 2, 1, 9, 7, 8]
    arr = [12, 11, 13, 5, 6, 7]
    ans = heapSort(arr)
    print(ans)
