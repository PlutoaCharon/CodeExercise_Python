class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = nums
        if k > len(arr) or k <= 0:
            return []
        start = 0
        end = len(arr) - 1
        index = self.quickSort(arr, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.quickSort(arr, start, end)
            if index < k-1:
                start = index + 1
                index = self.quickSort(arr, start, end)
        return arr[k - 1]

    def quickSort(self, arr, start, end):
        low = start
        high = end
        temp = arr[start]
        while low < high:
            while low < high and arr[high] <= temp:
                high -= 1
            arr[low] = arr[high]
            while low <high and arr[low] >= temp:
                low += 1
            arr[high] = arr[low]
        arr[low] = temp
        return low