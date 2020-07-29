# 方法一： 开辟新数据去重
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

# 方法二：先排序 在回溯过程中遇到相同的字符则跳过
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        nums = sorted(nums)
        res = []
        backtrack(nums, [])
        return res