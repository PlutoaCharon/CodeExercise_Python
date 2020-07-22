class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < n or not 0 <= j < m or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
            board[i][j] = tmp
            return res

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
