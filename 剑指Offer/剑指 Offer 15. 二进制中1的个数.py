class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
