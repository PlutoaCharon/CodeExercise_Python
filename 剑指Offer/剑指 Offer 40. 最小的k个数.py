class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k > len(arr) or k <= 0:
            return []
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k - 1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[:k]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] >= temp:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] < temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low


# 堆排序
class Solution:
    def GetLeastNumbers_Solution(self, arr, k):
        # write code here
        if not arr or not k or k > len(arr):
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
            # 构建最小堆
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, i, n)
            # 挨个出数
            for i in range(n - 1, -1, -1):
                arr[i], arr[0] = arr[0], arr[i]
                tmp.append(arr[i])
                if len(tmp) == k:
                    return tmp
                heapify(arr, 0, i)

        return heapSort(arr)
