# 第一种
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second


# 第二种
class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        for num in nums:
            second, first = max(num + first, second), second
        return second
