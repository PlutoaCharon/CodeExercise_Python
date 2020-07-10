class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0, dp_i_1 = 0, float("-inf")
        dp_pre_0 = 0
        for price in prices:
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, dp_pre_0 - price)
            dp_pre_0 = tmp
        return dp_i_0