# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
#
#
#  示例：
#
#  输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
# 解释：
# 长度最长的公共子数组是 [3, 2, 1] 。
#
#
#
#
#  提示：
#
#
#  1 <= len(A), len(B) <= 1000
#  0 <= A[i], B[i] < 100
#
#  Related Topics 数组 哈希表 二分查找 动态规划
#  👍 275 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, A, B):
        m, n = len(A), len(B)
        ans = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans