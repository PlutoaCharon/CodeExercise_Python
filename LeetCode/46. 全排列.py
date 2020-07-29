class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        res = []
        backtrack(nums, [])
        return res
