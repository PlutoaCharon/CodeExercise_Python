class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        res = []
        ans = []
        backtrack(nums, [])
        for i in res:
            if i not in ans:
                ans.append(i)
        return ans