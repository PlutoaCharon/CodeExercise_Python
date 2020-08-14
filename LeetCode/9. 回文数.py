# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
#  示例 1:
#
#  输入: 121
# 输出: true
#
#
#  示例 2:
#
#  输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
#  示例 3:
#
#  输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        while x >= 0:
            if str(x) == str(x)[::-1]:
                return True
            else:
                return False
        else:
            return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        tmp = 0
        while x > tmp:
            tmp = tmp * 10 + x % 10
            x = x // 10
        # 如果是奇数则去掉最后一位与x进行比较
        return x == tmp or x == tmp // 10
