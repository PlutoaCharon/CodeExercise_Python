# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
#  上图为 8 皇后问题的一种解法。
#
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#  示例:
#
#  输入: 4
# 输出: [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
#
#  提示：
#
#
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步
# ，可进可退。（引用自 百度百科 - 皇后 ）
#
#  Related Topics 回溯算法
#  👍 451 👎 0
class Solution(object):
    def solveNQueens(self, n):
        k = 0
        res, q = [], [None] * n   # q用于已经放的位置，例如q[2]=3 表示第3行的放到了第4个位置

        def dfs(k, n):
            if k == n:
                tmp = []
                for i in range(n):  # 输出一个结果
                    s = ""
                    for j in range(n):
                        s += "Q" if q[i] == j else '.'
                    tmp.append(s)
                res.append(tmp)
            else:
                for j in range(n):  # 一行一行的进行深度搜索 j为所在列
                    if self.place(k, j, q):
                        q[k] = j
                        dfs(k+1, n)
        dfs(k, n)
        return res

    def place(self, k, j, q):  # 判断该位置是否可以放一个棋子
        for i in range(k):
            if q[i] == j or abs(q[i]-j) == abs(i-k):  # 不同列，不同斜线
                return False
        return True