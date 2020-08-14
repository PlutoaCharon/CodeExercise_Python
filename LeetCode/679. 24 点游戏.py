class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if not nums:
            return False

        def helper(nums):
            if len(nums) == 1: return abs(nums[0] - 24) < 1e-6
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        newnum = [nums[k] for k in range(len(nums)) if i != k and j != k]
                        if helper(newnum + [nums[i] + nums[j]]): return True
                        if helper(newnum + [nums[i] - nums[j]]): return True
                        if helper(newnum + [nums[i] * nums[j]]): return True
                        if nums[j] != 0 and helper(newnum + [nums[i] / nums[j]]): return True
            return False

        return helper(nums)
