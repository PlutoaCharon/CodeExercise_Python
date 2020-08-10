class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1: i += 1
            while i < j and nums[j] & 1 == 0: j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


# 不改变顺序
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        lo = []
        le = []
        for d in nums:
            if d % 2 == 1:
                lo.append(d)
            else:
                le.append(d)
        return lo + le
