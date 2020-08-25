class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        def backtrack(nums, tmp):
            if len(tmp) >= 2 and tmp not in res:
                res.append(tmp)
            if not nums:
                return
            for i in range(len(nums)):

                if not tmp or nums[i] >= tmp[-1]:
                    backtrack(nums[i + 1:], tmp + [nums[i]])

        res = []
        backtrack(nums, [])
        return res
