class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        # 特判
        if not nums:
            return 0
        if nums[size - 1] < target:
            return size

        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left