# 统计所有小于非负整数 n 的质数的数量。
#
#  示例:
#
#  输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#  Related Topics 哈希表 数学
#  👍 377 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPrimes(self, n):
        prime = []
        if n == 0 or n == 1 or n == 2:
            print(0)
        for i in range(n+1):
            prime.append(True)
        for i in range(2, n+1):
            if prime[i] == True:
                p = i
                j = 2
                while p*j <= n:
                    prime[p*j] = False
                    j += 1
        prime = prime[2:len(prime)-1]
        ans = prime.count(True)
        return ans