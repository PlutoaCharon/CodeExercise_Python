class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = list(s)
        p = list(p)
        s.insert(0, '')
        p.insert(0, '')
        n, m = len(s), len(p)
        dp = [[False for _ in range(m)] for _ in range(n)]
        dp[0][0] = True

        # 如果p第一个字符为 *
        for i in range(1, m):
            if p[i] == "*":
                dp[0][i] = dp[0][i - 1]

        for i in range(1, n):
            for j in range(1, m):
                if s[i] == p[j] or p[j] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == "*":
                    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]