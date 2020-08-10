class Solution:
    def numWays(self, n: int) -> int:
        a = 1
        b = 2
        c = 0
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        for _ in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c % 1000000007


class Solution:
    def Fibonacci(self, n):
        # write code here
        a, b = 0, 1
        for i in range(0, n):
            a, b = b, a + b
        return a
