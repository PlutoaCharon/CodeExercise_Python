class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i, j):
            if vis[i][j]:
                return vis[i][j]
            max_l = 1
            if i + 1 < len(matrix) and matrix[i][j] < matrix[i + 1][j]:
                max_l = max(max_l, 1 + dfs(i + 1, j))
            if j + 1 < len(matrix[0]) and matrix[i][j] < matrix[i][j + 1]:
                max_l = max(max_l, 1 + dfs(i, j + 1))
            if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                max_l = max(max_l, 1 + dfs(i - 1, j))
            if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                max_l = max(max_l, 1 + dfs(i, j - 1))
            vis[i][j] = max_l
            return vis[i][j]

        if not matrix:
            return 0
        ans = 0
        n = len(matrix)
        m = len(matrix[0])
        vis = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        return ans


'''
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            max_l = 1
            if i + 1 < len(matrix) and matrix[i][j] < matrix[i + 1][j]:
                max_l = max(max_l, 1 + dfs(i + 1, j))
            if j + 1 < len(matrix[0]) and matrix[i][j] < matrix[i][j + 1]:
                max_l = max(max_l, 1 + dfs(i, j + 1))
            if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                max_l = max(max_l, 1 + dfs(i - 1, j))
            if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                max_l = max(max_l, 1 + dfs(i, j - 1))
            return max_l

        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i, j))
        return ans
    
'''
