class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while cur != 0 or high != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += high * digit + digit
            low += cur * digit
            cur = high % 10
            high = high // 10
            digit = digit * 10
        return res
