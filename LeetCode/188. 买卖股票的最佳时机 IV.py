class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 如果prices小于1个值：
        if len(prices) <= 1:
            return 0

        # 如果k大于n//2
        if k > len(prices) // 2:
            profit = 0
            for i in range(1, len(prices)):
                tmp = prices[i] - prices[i - 1]
                if tmp > 0: profit += tmp
            return profit

        else:
            max_k = k
            dp = [[[0, 0] for _ in range(max_k + 1)] for _ in range(len(prices))]

            for i in range(len(prices)):
                for k in range(max_k, 0, -1):
                    if i - 1 == -1:
                        dp[i][k][0] = 0
                        dp[i][k][1] = -prices[i]
                    else:
                        dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                        dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
            return dp[-1][max_k][0]