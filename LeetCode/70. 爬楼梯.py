# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划
#  👍 1106 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        a=1
        b=1
        c=0

        if n==1:
            return a
        elif n==2:
            return a+b
        else:
            for i in range(2, n+1):
                c=a+b
                a=b
                b=c
            return c

        """
        # 最优解
        lis = []
        lis.append(1)
        lis.append(2)
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(2, n):
            lis.append(lis[i - 1] + lis[i - 2])
        return lis[-1]
