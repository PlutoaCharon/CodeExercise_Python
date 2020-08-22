class Solution:
    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), -1, -1):
            for index in range(0, len(s) - length + 1):
                sub_string = s[index:length + index]
                if sub_string == sub_string[::-1]:
                    return sub_string
# 动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        maxLen, dp = 0, [[False]*len(s) for _ in range(len(s))]
        for j in range(len(s)):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    res = s[i:j + 1]
        return res