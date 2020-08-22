class Solution:
    def findContinuousSequence(self, tsum: int) -> List[List[int]]:
        # 根据等差数列
        # https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shu-xue-wen-ti-shu-xue-jie-jue-by-erik_chen/
        res = []
        for n in range(2, tsum + 1):
            temp = tsum - n * (n - 1) // 2
            if temp <= 0:
                break
            if not temp % n:
                a1 = temp // n
                res.append([a1 + i for i in range(n)])
        return res[::-1]