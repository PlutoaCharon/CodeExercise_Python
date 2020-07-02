# 1.暴力
# 知识点： 二维数组转一维数组 sum([[1], [2]],[]) -> [1,2]
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rec = sorted(sum(matrix, []))
        return rec[k - 1]
