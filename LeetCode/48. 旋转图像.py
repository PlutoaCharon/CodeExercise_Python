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
