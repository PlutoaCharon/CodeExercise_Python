class Solution:
    def numWays(self, n: int) -> int:
        a = 1
        b = 2
        c = 0
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        for _ in range(3, n+1):
            c = a + b
            a = b
            b = c
        return c % 1000000007