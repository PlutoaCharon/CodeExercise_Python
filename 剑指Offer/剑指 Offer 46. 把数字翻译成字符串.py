class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a, b = 1, 1
        for i in range(len(s) - 2, -1, -1):
            a, b = (a + b if "10"<= s[i:i+2]<="25" else a), a
        return a