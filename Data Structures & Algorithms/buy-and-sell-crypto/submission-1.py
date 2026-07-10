class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_seen = float('inf')
        for price in prices:
            min_seen = min(price, min_seen)
            profit = price - min_seen
            max_profit = max(profit, max_profit)
        return max_profit

