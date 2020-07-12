class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        maxNum = 10**9
        n, m = len(dungeon), len(dungeon[0])
        dp = [[maxNum] * (m + 1) for _ in range(n + 1)]
        dp[n][m -1], dp[n - 1][m] = 1, 1 # 设立边界值为1
        for i in range(n - 1, -1 ,-1):
            for j in range(m - 1, -1, -1):
                minN = min(dp[i][j + 1], dp[i + 1][j]) # 取最小值右边或者下边
                dp[i][j] = max(minN - dungeon[i][j], 1)   # 如果为正数， 则最小健康点为1
        return dp[0][0]