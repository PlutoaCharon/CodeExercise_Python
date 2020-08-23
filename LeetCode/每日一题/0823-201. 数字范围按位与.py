class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        t = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            t += 1
        return m << t
