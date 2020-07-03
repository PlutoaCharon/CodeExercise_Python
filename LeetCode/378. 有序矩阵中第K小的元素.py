# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
#
#
#
#  示例：
#
#  matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
#
#
#
#
#  提示：
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
#  Related Topics 堆 二分查找
#  👍 350 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rec = sorted(sum(matrix, []))
        return rec[k - 1]