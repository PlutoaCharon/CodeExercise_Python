class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col - 1, -1, -1):
            for j in range(row - 1, -1, -1):
                if matrix[j][i] < target:
                    break
                else:
                    if matrix[j][i] == target:
                        return True
        return False
