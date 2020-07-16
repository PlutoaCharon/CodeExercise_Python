class Solution:
    def dfs(self, grid, colors, i, color, N):
        colors[i] = color
        for j in range(N):
            if grid[i][j] == 1:
                if colors[j] == color:
                    return False
                if colors[j] == 0 and not self.dfs(grid, colors, j, -1 * color, N):
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        grid = [[0] * N for _ in range(N)]
        colors = [0] * N
        for i in range(N):
            for j in graph[i]:
                grid[i][j] = 1
        for i in range(N):
            if colors[i] == 0 and not self.dfs(grid, colors, i, 1, N):
                return False
        return True
