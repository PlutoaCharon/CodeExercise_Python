class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_i_0, dp_i_1 = 0, float("-inf")
        for price in prices:
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, tmp - price - fee)
        return dp_i_0