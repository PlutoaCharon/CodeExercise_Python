# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
#
#  F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
#
#
#  给定 N，计算 F(N)。
#
#
#
#  示例 1：
#
#  输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
#
#
#  示例 2：
#
#  输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
#
#
#  示例 3：
#
#  输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
#
#
#
#
#  提示：
#
#
#  0 ≤ N ≤ 30
#
#  Related Topics 数组
#  👍 132 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 方法1
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n<2:
            return n
        return (self.fib(n-1)+self.fib(n-2))

# 方法2
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        a=1
        b=1
        c=0
        if N == 0 :
            return 0
        elif N==1 or N==2:
            return 1
        else:
            for i in range(3,N+1):
                c=a+b
                a=b
                b=c
            return c
        """
        ## 最优解
        if N in (0, 1):
            return N

        a = 0
        b = 1
        for i in range(2, N + 1):
            temp = a
            a = b
            b = temp + a
        return b