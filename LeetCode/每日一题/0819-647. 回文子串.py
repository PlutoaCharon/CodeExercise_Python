# 双指针
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    ans += 1
        return ans


# 动态规划
"""
        （1）思路：动态规划
                我们以dp[i][j]表示区间[i, j]之间的子串是否为回文子串，这样可以思考这样三种情况的回文子串：
                    - 子串长度为1，例如 a 一定为回文子串，即 i=j 的情况
                    - 子串长度为2，且字符相同，例如 aa 一定为回文子串，即 s[i] = s[j] and j-i = 1
                    - 子串长度大于2，符合 abcba 形式的为回文子串，根据回文子串的定义，那么 abcba 去掉两边字符，仍为回文
                    子串，即bcb，转换成方程形式即 dp[i][j] = dp[i+1][j-1] and j-i > 1 and s[i] = s[j]
                剩下的均为不符合条件，即非回文子串。

        （2）复杂度：
            - 时间复杂度：O（N^2）
            - 空间复杂度：O（N^2）
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        ans = 0
        dp = [[False] * len(s) for _ in range(len(s))]
        for j in range(0, len(s)):
            for i in range(j, -1, -1):
                if i == j:
                    dp[i][j] = True
                    ans += 1
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
                elif j - i > 1 and s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans += 1
        return ans
