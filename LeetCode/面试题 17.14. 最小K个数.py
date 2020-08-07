class Solution:
    def smallestK(self, arr, k):
        if not arr or not k:
            return []

        def heapify(arr, i, n):
            left = 2 * i + 1
            right = 2 * i + 2

            minNum = i
            if left < n and arr[minNum] > arr[left]:
                minNum = left
            if right < n and arr[minNum] > arr[right]:
                minNum = right

            if minNum != i:
                arr[i], arr[minNum] = arr[minNum], arr[i]
                heapify(arr, minNum, n)

        def heapSort(arr):
            n = len(arr)
            tmp = []
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, i, n)

            for i in range(n - 1, -1, -1):
                arr[i], arr[0] = arr[0], arr[i]
                tmp.append(arr[i])
                if len(tmp) == k:
                    return tmp
                heapify(arr, 0, i)

        return heapSort(arr)


if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    k = 4
    ans = s.smallestK(arr, k)
    print(ans)
