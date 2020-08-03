# 方法一 位运算
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        n = 1 << size
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res

# 方法二
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def track_back(i, tmp):
            res.append(tmp)
            if i == n:
                return
            for j in range(i, n):
                track_back(j + 1, tmp + [nums[j]])

        n = len(nums)
        nums.sort()
        res = []
        track_back(0, [])
        return res
