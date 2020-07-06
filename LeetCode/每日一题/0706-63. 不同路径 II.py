'''
class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # @lru_cache(None)
        def dfs(n1, m1):
            if n1 < 0 or m1 < 0 or n1 > self.n - 1 or m1 > self.m - 1 or dp[n1][m1] == 1 or obstacleGrid[n1][m1] == 1:
                return

            if obstacleGrid[n1][m1] == "F":
                self.ans += 1
                return

            dp[n1][m1] = 1
            dfs(n1 + 1, m1)
            dfs(n1, m1 + 1)
            dp[n1][m1] = 0

        self.ans = 0
        self.n, self.m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(self.m)] for _ in range(self.n)]
        obstacleGrid[self.n - 1][self.m - 1] = "F"
        dfs(0, 0)
        return self.ans
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i - 1][j - 1] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[m][n]
