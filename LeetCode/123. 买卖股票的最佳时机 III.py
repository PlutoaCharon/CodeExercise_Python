# 一个方法团灭 6 道股票问题
# dp[i][k][0 or 1] 在i天还剩k次交易次数，1持有 0不持有
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) [不动，昨天持有 今天卖了 + prices[i]]
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) [不动，昨天没有 今天买入 - prices[i]]
def maxProfit(self, prices: List[int]) -> int:
    if len(prices) <= 1: return 0
    maxk = 2
    dp = [[[0, 0] for i in range(maxk + 1)] for i in range(len(prices))]
    dp[0][2][0] = 0  # 第0天，不管还剩几次交易次数，不持有收益是0，也不可能持有(一天内不能瞬间买入卖出)，所以设1为负数
    dp[0][2][1] = -prices[0]
    dp[0][1][0] = 0
    dp[0][1][1] = -prices[0]
    for i in range(1, len(prices)):
        for k in range(maxk, 0, -1):  # 这里必须倒着，base case中k是倒着的，这里正序会出现0，1，与前面的设定不同了，就会出错
            dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
    return dp[-1][maxk][0]


