class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        def track_back(i, tmp):
            res.append(tmp)
            if i == n:
                return
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                track_back(j + 1, tmp + [nums[j]])

        res = []
        track_back(0, [])
        return res
