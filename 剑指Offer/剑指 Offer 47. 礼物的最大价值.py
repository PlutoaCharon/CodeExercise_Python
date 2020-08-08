class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        # 初始化第一行
        for i in range(1, m):
            grid[0][i] += grid[0][i - 1]
        # 初始化第一列
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
