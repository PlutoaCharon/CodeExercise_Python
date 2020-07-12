class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = float("inf")
        for price in prices:
            minprice = min(price, minprice)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit