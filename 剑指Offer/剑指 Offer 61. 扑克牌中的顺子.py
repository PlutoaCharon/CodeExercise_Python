class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if not nums:
            return False
        tmp = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue
            ma = max(ma, num)
            mi = min(mi, num)
            if num in tmp: return False
            tmp.add(num)
        return ma - mi < 5
