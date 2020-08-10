class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[:] = list(map(list, zip(*(matrix[::-1]))))
        n = len(matrix)
        matrixNew = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrixNew[j][n - i - 1] = matrix[i][j]
        matrix[:] = matrixNew


# 原地置换：
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先转置 后镜像
        row, col = len(matrix), len(matrix[0])
        for i in range(row - 1):
            for j in range(i + 1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(row):
            matrix[i] = matrix[i][::-1]
