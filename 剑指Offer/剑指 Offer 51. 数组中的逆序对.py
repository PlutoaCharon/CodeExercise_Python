class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        q = []
        res = 0
        for v in nums:
            i = bisect.bisect_left(q, -v)
            res += i
            q[i:i] = [-v]
        return res